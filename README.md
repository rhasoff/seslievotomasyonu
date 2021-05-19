# seslievotomasyonu
Flask server üzerinde çalışan, sesli komutlarla (sanal) servisleri açıp kapatan ev otomasyon sistemi.


### 1 Bu repoyu indir
`git clone https://github.com/rhasoff/seslievotomasyonu.git`

### 2 Python sanal ortam yarat. Örneğin:
`python3 -m venv venv`

### 3 Sanal ortamı aktif et. `venv` dosyasının olduğu klasör içerisinde:
Linux:
`source venv/bin/activate`
Windows: 
`venv\Scripts\activate`

### 4 Bağımlılıkları yükle
`python3 install -r requirements.txt`

### 5 Veritabanını kur (veya sıfırla):
`python3 resetdb.py`

### 6 Flac okuyucu yükle:
`sudo apt-get install flac`


### 7 Çalıştır:
`flask run --cert=adhoc`


Uygulama hatasız çalıştığında console'da aşağıdaki gibi bir çıktı alacaksın:
```shell
 * Serving Flask app "run.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on https://192.168.0.105:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 ```

Burada yazan ip adresini ve portunu (`https://192.168.0.105:5000/`)birebir aynı şekilde mobil veya PC farketmez, herhangi bir tarayıcıya girdiğinde web uygulamasının sayfası açılacak.
*Not: Mobilden girmeye çalıştığında muhtemelen tarayıcın "bu ssl sertifikasi güvenilir değil" uyarısı verecek. "Gelişmiş" veya "Advanced" gibi bir button'a tıklayarak devam edebilmen lazım. Firefox, Google Chrome ve Brave tarayıcılarında denendi & çalışıyor.*

Sayfa açıldığında, uygulamanın mikrofondan ses kaydı alabilmesi için mikrofon iznini vermiş olman gerek. Aksi halde tarayıcından ses komutu gönderemezsin.

*Not(2): Eğer ip adresi yukarıdaki şekilde görünmezse, linux'de `ifconfig` komutu ile ya da basitçe `hostname -I` ile local IP adresini alabilirsin. Port olarak yine sonuna `:5000` eklemen yetecektir.


