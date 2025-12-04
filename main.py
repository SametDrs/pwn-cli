import requests, hashlib, os, time

BASE_URL = "https://api.pwnedpasswords.com/range/"
UA = "SD-PwnedCheck/1.0"

def get_pwned_passwords_count(password):
    password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = password[:5]
    suffix = password[5:]
    try:
        response = requests.get(BASE_URL + prefix, headers={"User-Agent": UA})
        if response.status_code != 200:
            print("Hata: API isteği başarısız oldu.")
            return None
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
        return 0
    except requests.RequestException as e:
        print(f"Hata: API isteği sırasında bir hata oluştu: {e}")
        return None
    

def main():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\nSD Parola Sızıntı Kontrolü")
            print("Çıkmak için Ctrl+C tuşlarına basınız.")
            print("Web sitem: sametdursun.xyz")
            print("------------------------------")

            password = input("Parolanızı giriniz: ")

            os.system('cls' if os.name == 'nt' else 'clear')
            if not password:
                print("Lütfen geçerli bir parola giriniz.")
                time.sleep(2)
                continue
            count = get_pwned_passwords_count(password)

            if count is None:
                continue
            if count > 1000:
                status = "ÇOK TEHLİKELİ ACİL DEĞİŞTİRİN"
            elif count > 100:
                status = "TEHLİKELİ ACİL DEĞİŞTİRİN"
            elif count > 0:
                status = "ORTA TEHLİKE DEĞİŞTİRİN"
            else:
                status = "GÜVENLİ"

            sızıntı = 'SIZDIRILDI' if count > 0 else 'SIZDIRILMADI'

            print(f"Parola: {password} \nSızıntı durumu: {sızıntı} \nSızıntıya uğrama sayısı: {count} \nDeğerlendirme: {status}")
            print("------------------------------")

            if input("Başka bir parola kontrol etmek ister misiniz? (E/H): ").strip().upper() != 'E':
                print("Çıkış yapılıyor...")
                break
        except KeyboardInterrupt:
            print("\nÇıkış yapılıyor...")
            break



if __name__ == "__main__":
    main()
