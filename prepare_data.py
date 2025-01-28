import os
import PyPDF2
from pathlib import Path
import json


def extract_text_from_pdf(pdf_path):
    """PDF dosyasından metin çıkarır."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


def process_documents(docs_dir):
    """Belirtilen dizindeki tüm PDF'leri işler."""
    training_data = []

    # PDF dosyalarını bul ve işle
    for pdf_file in Path(docs_dir).glob("**/*.pdf"):
        try:
            text = extract_text_from_pdf(pdf_file)
            # Metni uygun uzunlukta parçalara böl
            chunks = [text[i : i + 512] for i in range(0, len(text), 512)]

            for chunk in chunks:
                if len(chunk.strip()) > 100:  # Çok kısa parçaları atla
                    training_data.append({"text": chunk, "source": str(pdf_file)})
        except Exception as e:
            print(f"Hata: {pdf_file} işlenirken hata oluştu - {str(e)}")

    return training_data


def save_training_data(data, output_file):
    """İşlenmiş veriyi JSON formatında kaydeder."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # PDF'lerin bulunduğu dizin
    DOCS_DIR = "documents"
    # Eğer dizin yoksa oluştur
    os.makedirs(DOCS_DIR, exist_ok=True)

    print("Dokümanlar işleniyor...")
    training_data = process_documents(DOCS_DIR)

    # İşlenmiş veriyi kaydet
    save_training_data(training_data, "training_data.json")
    print(f"İşlem tamamlandı. {len(training_data)} adet eğitim örneği oluşturuldu.")
