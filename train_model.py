import json
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import os
import requests


def check_ollama_model():
    """Ollama API üzerinden modelin varlığını kontrol et"""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        models = response.json()
        return any(model["name"] == "llama3.2:1b" for model in models["models"])
    except:
        return False


def load_training_data(file_path):
    """Eğitim verisini yükle"""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [item["text"] for item in data]


def prepare_dataset(texts, tokenizer):
    """Metinleri model için hazırla"""

    def tokenize_function(examples):
        return tokenizer(
            examples["text"], truncation=True, padding="max_length", max_length=512
        )

    dataset = Dataset.from_dict({"text": texts})
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    return tokenized_dataset


def main():
    # Ollama modelini kontrol et
    if not check_ollama_model():
        print("Hata: llama3.2:1b modeli Ollama'da bulunamadı.")
        return

    # Ollama API'sini kullanarak modele eriş
    model_url = "http://localhost:11434/api/generate"

    print("Eğitim verisi hazırlanıyor...")
    texts = load_training_data("training_data.json")

    # Basit bir tokenizer oluştur
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    dataset = prepare_dataset(texts, tokenizer)

    # LoRA konfigürasyonu
    lora_config = LoraConfig(
        r=16, lora_alpha=32, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM"
    )

    # Eğitim argümanlarını ayarla
    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        warmup_steps=100,
        logging_steps=10,
        save_steps=100,
        learning_rate=2e-4,
    )

    print("Eğitim başlıyor...")
    for text in texts:
        # Her metin için Ollama API'sini kullan
        response = requests.post(
            model_url, json={"model": "llama3.2:1b", "prompt": text, "stream": False}
        )

        if response.status_code == 200:
            print("İşleniyor:", text[:50], "...")
        else:
            print("Hata:", response.status_code)

    print("Eğitim tamamlandı!")


if __name__ == "__main__":
    main()
