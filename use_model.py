import requests
import time
import sys


def generate_text(prompt):
    """Eğitilmiş model ile metin üret"""
    # Ollama API'sine istek gönder
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "deepseek-r1:8b", "prompt": prompt, "stream": False},
    )

    if response.status_code == 200:
        yanit = response.json()["response"]
        # Yanıtı karakter karakter yazdır
        for karakter in yanit:
            sys.stdout.write(karakter)
            sys.stdout.flush()  # Tamponu hemen boşalt
            time.sleep(0.02)  # Her karakter arasında küçük bir bekleme
        print()  # En sonda yeni satıra geç
        return yanit
    else:
        return f"Hata oluştu: {response.status_code}"


# Modeli nasıl kullanacağımızı gösteren örnek
if __name__ == "__main__":
    # Bir örnek metin yazalım
    ornek_prompt = """Makne Örenmes Teknkler le Banka Hsse Senetlernn Fyat Tahmn makaleye bakarak bir hisse ne zaman artar acikla"""

    print("Prompt:", ornek_prompt)
    print("\nModel yanıtı:")
    yanit = generate_text(ornek_prompt)
    print(yanit)
