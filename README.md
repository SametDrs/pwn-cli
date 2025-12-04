# 🔐 SD-pwn-cli  
Minimalist bir CLI aracı — girilen parolanın geçmiş veri sızıntılarında yer alıp almadığını kontrol eder.  
A minimalist CLI tool to check whether a given password has appeared in past data breaches.

---

# 🇹🇷

## 🚀 Özellikler
- Have I Been Pwned (HIBP) Password API kullanır  
- K-Anonimity yöntemiyle güvenli parola kontrolü  
- Gerçek parola **asla** internete gönderilmez  
- Terminal üzerinden kolay kullanım  
- Sızıntı sayısına göre risk değerlendirmesi sağlar

---

## 📌 Nasıl Çalışır?
Araç, parolayı SHA-1 ile hashler ve hash’in **ilk 5 karakterini** HIBP API’sine gönderir.  
API aynı prefix ile başlayan hash’leri döndürür ve araç kendi hash’inizin **suffix** kısmını bu listede arar.

Bu yöntem sayesinde:
- Parola gizliliği korunur  
- Tamamen anonim bir doğrulama yapılır  
- Hızlı ve güvenilir sonuç alınır  

---

## 📦 Gereksinimler
```
pip install requests
```
---

## 🖥️ Kullanım

```bash
python main.py
```
## 🧪 Örnek Çıktı
```bash
Parola: ornek123
Sızıntı durumu: SIZDIRILDI
Sızıntıya uğrama sayısı: 1429
Değerlendirme: GÜVENLİ DEĞİL
```
## 🌐 Not
Bu proje yalnızca parola kontrolü yapar.
HIBP e-posta arama API’si ücretli olduğu için email sorgulama eklenmemiştir.


## 🌐 Note

This project performs password checks only.
HIBP’s email breach endpoint is paid, therefore email lookups are not included.

## 👤 Developer
### 🌐Samet Dursun: https://sametdursun.xyz
