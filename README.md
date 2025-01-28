# LLM Fine-Tuning Projesi

Bu proje, Llama modelini özel dokümanlarınızla fine-tune etmenizi sağlar.

## Kurulum

1. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

2. `documents` klasörü oluşturun ve fine-tune etmek istediğiniz PDF dosyalarını bu klasöre kopyalayın.

## Kullanım

1. Önce dokümanları işleyin:

```bash
python prepare_data.py
```

2. Modeli fine-tune edin:

```bash
python train_model.py
```

3. Fine-tune edilmiş model `fine_tuned_model` klasöründe saklanacaktır.

## Notlar

- PDF dosyalarınızı `documents` klasörüne yerleştirdiğinizden emin olun
- Eğitim süresi doküman sayısına ve boyutuna göre değişebilir
- GPU'nuz varsa eğitim daha hızlı olacaktır
- Eğitim parametrelerini `train_model.py` dosyasından ayarlayabilirsiniz
