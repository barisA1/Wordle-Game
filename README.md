# 🌟 Wordle Oyunu 🎮

Bu Python programı, kullanıcıların 5 harfli kelimeleri tahmin etmelerine dayanan interaktif bir Wordle oyununu uygular. Oyun, tkinter kütüphanesi kullanılarak GUI (Grafiksel Kullanıcı Arayüzü) ile birlikte gelir.

https://github.com/barisA1/Wordle-Game/assets/69991160/c33c9205-ecbb-47de-b16e-ea7d84c6be9c

## 📄 İçindekiler

- **[Nasıl Oynanır?](#-nasıl-oynanır)**
- **[Kurulum](#️-kurulum)**
- **[Ek Bilgiler](#-ek-bilgiler)**
- **[🤝 Katılım](#-katılım)**

## 🎯 Nasıl Oynanır?

1. **Başlangıç:**
   - Oyun başladığında, kullanıcıdan 5 harfli bir kelime tahmini girmesi istenir.

2. **Kelime Tahmini:**
   - Tahmin edilecek kelime, sadece Türk alfabesindeki harflerden oluşmalıdır.
   - Girilen harfler doğruysa ve doğru konumlardaysa ✅ yeşil renkte işaretlenir.
   - Girilen harfler doğruysa ancak yanlış konumlardaysa ⚠️ sarı renkte işaretlenir.
   - Yanlış harfler ➖ gri renkte işaretlenir.

3. **Tahmin Kontrolü:**
   - Kullanıcının tahmini, oyun içindeki geçerli kelimeler listesinde bulunmalıdır.
   - Geçerli bir tahmin yapıldığında, tahmin hakkı azalır.

4. **Oyun Sonucu:**
   - Doğru kelimeyi bulan kullanıcıya tebrikler mesajı gösterilir.
   - Tahmin hakkı kalmayan kullanıcıya doğru kelime ve oyunun sonucunu gösteren bir mesaj verilir.

5. **Yeniden Oyna:**
   - Oyun bittiğinde "Yeniden Oyna" düğmesine tıklayarak yeni bir oyun başlatılabilir.

## 🛠️ Kurulum

1. **Python Kurulumu:**
   - Python'u bilgisayarınıza yükleyin (eğer yüklü değilse): [Python İndirme Sayfası](https://www.python.org/downloads/)

2. **Projeyi Başlatma:**
   - Projeyi bilgisayarınıza indirin veya kopyalayın.
   - Terminal veya komut istemcisinde projenin bulunduğu dizine gidin.

3. **Gerekli Kütüphanenin Kurulumu:**
   - `tkinter` kütüphanesi genellikle Python kurulumuyla gelir. Ancak eksikse şu komutla yükleyebilirsiniz:
     ```bash
     pip install tk
     ```

4. **Oyunu Başlatma:**
   - Terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:
     ```bash
     python wordle_game.py
     ```

## ℹ️ Ek Bilgiler

- Oyunun geliştirilmesi sırasında `kelimeler.txt` dosyası üzerinde değişiklik yaparak oyunun kullanacağı kelime listesini özelleştirebilirsiniz.
- Oyun içindeki tuş takımıyla (klavye veya fareyle) kelime tahminlerinizi yapabilirsiniz.

## 🤝 Katılım

- Bu depoyu çatallayın (fork) ve geliştirmelerinizi yapın.
- Yeni özellikler eklemek veya hataları düzeltmek için Pull Talepler (Pull Requests) gönderin.
- Hataları bildirmek veya önerilerde bulunmak için konu (issue) açın.
