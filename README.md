# Khas Kulüp Tavsiye

Khas Kulüp Tavsiye, Koç Üniversitesi öğrencilerine kişiselleştirilmiş kulüp önerileri sunan bir web uygulamasıdır. Google'ın Gemini AI modelini kullanarak, öğrencilerin ilgi alanları, hobileri ve bölümlerine göre en uygun kulüpleri önerir.

## Özellikler

- Kişiselleştirilmiş kulüp önerileri
- Öğrenci bilgilerine göre akıllı eşleştirme
- E-posta ile kulüp başvuru sistemi
- Kullanıcı dostu arayüz
- Güvenli oturum yönetimi

## Teknolojiler

- Python 3.x
- Flask (Web Framework)
- Flask-Mail (E-posta gönderimi)
- Google Gemini AI
- HTML/CSS
- JavaScript

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [repository-url]
cd khaskuluptavsiye
```

2. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

3. Gerekli API anahtarlarını ayarlayın:
   - Google Gemini API anahtarı
   - Gmail SMTP ayarları

4. Uygulamayı çalıştırın:
```bash
python app.py
```

Uygulama varsayılan olarak `http://localhost:5001` adresinde çalışacaktır.

## Kullanım

1. Ana sayfada öğrenci bilgilerinizi girin:
   - İsim ve Soyisim
   - Bölüm
   - Hobiler
   - İlgi Alanları

2. "Tavsiye Al" butonuna tıklayın

3. Size önerilen kulüpler listelenecektir

4. İstediğiniz kulübe başvurmak için e-posta adresinizi girin

## Güvenlik

- Oturum yönetimi için güvenli rastgele anahtar kullanımı
- E-posta gönderimi için güvenli SMTP bağlantısı
- Kullanıcı verilerinin güvenli işlenmesi

## Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

Proje Sahibi - [@your-username](https://github.com/your-username)

Proje Linki: [https://github.com/your-username/khaskuluptavsiye](https://github.com/your-username/khaskuluptavsiye) 