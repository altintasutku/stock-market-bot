import requests
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd


def get_crypto_data():
    """Ethereum verilerini Yahoo Finance'den çek"""
    try:
        print("Yahoo Finance'e bağlanılıyor...")
        # Ethereum'un Yahoo Finance'deki sembolü
        crypto = yf.Ticker("ETH-USD")

        print("Geçmiş veriler alınıyor...")
        # Son bir aylık verileri al
        hist = crypto.history(period="1mo")
        print(f"Veri sayısı: {len(hist)}")

        if not hist.empty:
            # Son işlem gününün kapanış fiyatını al
            current_price = hist.iloc[-1]["Close"]
            print(f"Son kapanış fiyatı: ${current_price:.2f}")

            trend_info = {
                "current_price": current_price,
                "month_start": hist.iloc[0]["Close"],
                "month_high": hist["High"].max(),
                "month_low": hist["Low"].min(),
                "avg_volume": hist["Volume"].mean(),
                "price_change": (
                    (current_price - hist.iloc[0]["Close"]) / hist.iloc[0]["Close"]
                )
                * 100,  # Aylık yüzde değişim
            }
            return trend_info
        else:
            print("Hata: Geçmiş veriler alınamadı")
            return None
    except Exception as e:
        print(f"Veri çekerken detaylı hata: {str(e)}")
        print("Hata türü:", type(e).__name__)
        return None


def analyze_crypto(trend_info):
    """Ethereum analizi yap ve modele sor"""
    from use_model import generate_text

    prompt = f"""
    Ethereum (ETH-USD) Kripto Analizi:
    
    Mevcut Durum:
    - Son Kapanış: ${trend_info['current_price']:.2f}
    - Ay Başı Fiyat: ${trend_info['month_start']:.2f}
    - Aylık En Yüksek: ${trend_info['month_high']:.2f}
    - Aylık En Düşük: ${trend_info['month_low']:.2f}
    - Aylık Değişim: %{trend_info['price_change']:.2f}
    - Ortalama İşlem Hacmi: {trend_info['avg_volume']:,.0f}
    
    Bu verilere dayanarak:
    1. Mevcut fiyat seviyesini değerlendir
    2. Son bir aydaki trend yönünü analiz et
    3. Hacim bazlı analiz yap
    4. Bir ay sonraki muhtemel fiyat aralığını tahmin et
    
    Lütfen detaylı bir analiz ve tahmin paylaş.
    """

    return generate_text(prompt)


def main():
    print("Ethereum Kripto Analizi")
    print("-" * 40)

    # Verileri al
    trend_info = get_crypto_data()

    if trend_info:
        print(f"Son Kapanış: ${trend_info['current_price']:.2f}")
        print(f"Aylık En Yüksek: ${trend_info['month_high']:.2f}")
        print(f"Aylık En Düşük: ${trend_info['month_low']:.2f}")
        print(f"Aylık Değişim: %{trend_info['price_change']:.2f}")
        print("\nAnaliz yapılıyor...")
        print("-" * 40)

        # Analiz yap ve tahmin al
        prediction = analyze_crypto(trend_info)
        print("\nModel Tahmini ve Analizi:")
        print(prediction)
    else:
        print("Veri alınamadı. Lütfen daha sonra tekrar deneyin.")


if __name__ == "__main__":
    main()
