# Flask Code Review API with ChatGPT

Bu proje, Flask kullanarak kullanıcı tarafından gönderilen kodları analiz eden ve OpenAI'nin ChatGPT modelini kullanarak geri bildirim sağlayan bir API içerir. Proje, Vercel üzerinde deploy edilebilir ve çevresel değişkenleri `.env` dosyasından alır.

## Kurulum

1. Projeyi klonlayın:

    ```bash
    git clone <proje_linki>
    cd <proje_klasörü>
    ```

2. Gerekli Python paketlerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

## Çevresel Değişkenlerin Ayarlanması

Bu projede, OpenAI API anahtarınızı güvende tutmak için `.env` dosyasını kullanıyoruz.

1. Projenin ana dizininde `.env` adında bir dosya oluşturun:

    ```bash
    touch .env
    ```

2. `.env` dosyasına OpenAI API anahtarınızı ekleyin:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

### OpenAI API Anahtarı Nasıl Alınır?

1. [OpenAI](https://platform.openai.com/) hesabınıza giriş yapın veya bir hesap oluşturun.
2. Hesabınıza giriş yaptıktan sonra, sağ üst köşedeki profil resminize tıklayın ve **API keys** seçeneğini bulun.
3. "Create new secret key" butonuna tıklayarak yeni bir API anahtarı oluşturun.
4. Bu anahtarı kopyalayın ve `.env` dosyasındaki `OPENAI_API_KEY` değişkeninin yanına yapıştırın.

## Projeyi Çalıştırma

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Çevresel değişkenlerin `.env` dosyasından yüklendiğinden emin olun. Eğer `python-dotenv` kütüphanesi yüklenmediyse şu komutla yükleyin:

    ```bash
    pip install python-dotenv
    ```

2. Uygulamayı başlatın:

    ```bash
    python app.py
    ```

3. Uygulama çalıştığında, [http://localhost:5000](http://localhost:5000) adresine giderek ana sayfaya erişebilirsiniz.

## Proje Yapısı

- `app.py`: Flask uygulamasının ana dosyasıdır.
- `requirements.txt`: Projede kullanılan bağımlılıkları içerir.
- `.env`: OpenAI API anahtarınızı sakladığınız dosyadır. **Bu dosya güvenlik amacıyla paylaşılmamalıdır.**
- `vercel.json`: Projenin Vercel üzerinde nasıl çalıştırılacağını belirler.

## Deployment (Vercel Üzerinde Yükleme)

1. Proje dizininde `.env` dosyasının doğru ayarlandığından emin olun.
2. `vercel.json` dosyasını yapılandırın. Örnek yapılandırma dosyası aşağıdaki gibidir:

    ```json
    {
      "version": 2,
      "builds": [
        {
          "src": "app.py",
          "use": "@vercel/python"
        }
      ],
      "routes": [
        {
          "src": "/(.*)",
          "dest": "app.py"
        }
      ]
    }
    ```

3. Projeyi Vercel üzerinden deploy edin. Deploy sonrası, proje URL'sini alarak projenizi canlı olarak kullanabilirsiniz.

---

Bu README dosyası, projenin kurulum, çalıştırma ve deploy süreçleriyle ilgili temel bilgileri içermektedir. Ekstra sorularınız için lütfen belgelere başvurun veya proje sorumlusuyla iletişime geçin.
