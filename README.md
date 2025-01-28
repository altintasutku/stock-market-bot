# Stock Market Bot

Bu proje, makine öğrenmesi teknikleri kullanarak borsa tahminleri yapan bir Python uygulamasıdır.

## Özellikler

- Geçmiş borsa verilerini kullanarak tahminler yapar
- Farklı makine öğrenmesi modelleri kullanır
- Tahmin sonuçlarını görselleştirir

## Kurulum

1. Projeyi klonlayın:

```bash
git clone https://github.com/altintasutku/stock-market-bot.git
cd stock-market-bot
```

2. Sanal ortam oluşturun ve aktif edin:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
# veya
venv\Scripts\activate  # Windows için
```

3. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

1. Model eğitimi için:

```bash
python train_model.py
```

2. Tahmin yapmak için:

```bash
python predict_stock.py
```

## Dosya Yapısı

- `train_model.py`: Model eğitimi için ana script
- `predict_stock.py`: Tahmin yapmak için kullanılan script
- `prepare_data.py`: Veri hazırlama işlemleri
- `requirements.txt`: Gerekli Python paketleri
- `training_data.json`: Eğitim verileri

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun
