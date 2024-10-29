
# Protesq Voice Assistant

Bu proje, Python ve Tkinter kullanılarak geliştirilen bir sesli asistan uygulamasıdır. Uygulama, mikrofon aracılığıyla kullanıcının sesli komutlarını dinler ve çeşitli görevleri yerine getirir. Örneğin, Google’da arama yapma, çöp kutusunu boşaltma veya masaüstündeki belirli bir uygulamayı açma işlemlerini gerçekleştirebilir.

## Gereksinimler

Proje aşağıdaki Python kütüphanelerine ihtiyaç duyar. Python 3.x sürümünü kullanmanız önerilir.

### Kurulum

Gerekli kütüphaneleri yüklemek için aşağıdaki komutları terminal veya komut satırına girin:

```bash
pip install SpeechRecognition
pip install pyaudio
```

> **Not**: `pyaudio` kütüphanesi bazı sistemlerde doğrudan yüklenemeyebilir. Yüklemekte sorun yaşarsanız `pyaudio` için uyumlu bir tekerlek (`.whl` dosyası) indirip kurulum yapabilirsiniz. [PyAudio tekerlek dosyalarını buradan indirebilirsiniz.](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

## Kullanım

Uygulama, sesli komutlar aracılığıyla çalışır. Tkinter GUI’sinde "Dinle" butonuna tıkladığınızda, uygulama mikrofon üzerinden sesli komutları dinlemeye başlar.

### Desteklenen Komutlar

1. **Google Arama**: `"Google'da ara X"` komutuyla `"X"` kelimesi veya cümlesi Google’da aratılır. Örneğin, `Google'da ara Python nedir` komutuyla Python hakkında Google araması yapılır.

2. **Çöp Kutusunu Boşaltma (Windows)**: `"çöp kutusunu boşalt"` komutuyla Windows çöp kutusu boşaltılır.

3. **Masaüstündeki Uygulamaları Açma**: `"masaüstünde X aç"` komutuyla masaüstünde `"X"` adında bir kısayol (.lnk dosyası) varsa bu dosya açılır. Örneğin, masaüstünde `"Spotify.lnk"` dosyası varsa `masaüstünde Spotify aç` komutuyla Spotify uygulaması açılacaktır.

### Uygulamayı Çalıştırma

1. Python kodunu çalıştırın:

   ```bash
   python protesq_voice.py
   ```

2. Uygulama açıldığında, `Dinle` butonuna tıklayın.
3. Mikrofonunuza sesli komutlar vererek uygulamayı kontrol edin.

