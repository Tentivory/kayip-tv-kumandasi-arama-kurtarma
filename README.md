# KAYIP TV KUMANDASI ARAMA-KURTARMA

**Kurum:** TentiAŞ Kayyumluk Ofisi, Kanepe Altı Şubesi  
**Sınıf:** Gereksiz ama çalışır  
**Tehlike seviyesi:** Düşük. Asıl tehlike, maçın 89. dakikasında kumandanın yok olmasıdır.

Bu depo, kayıp televizyon kumandasını kanepenin altına girmeden, resmi bir tutanakla bulan bir arama-kurtarma yazılımıdır. Bulmazsa da bulmuş gibi tutanak tutar. Tutanak bağlayıcı değildir. Kanepe bağlayıcıdır.

## Neden var?

Çünkü kumanda her zaman şu üç yerden birindedir:

1. Minderin altında, gururla.
2. Kedinin altında, rehin olarak.
3. Buzdolabının üstünde, kimsenin sormadığı bir nedenden.

Yazılım bu üçlüyü genişletir, olasılık dağıtır, pil seviyesini tiyatroyla tahmin eder ve sana bir operasyon emri basar.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Çay isteğe bağlıdır, yazılım çay içmez, sadece sorar.

```bash
python3 kumanda_kurtarma.py
```

Argümansız çalışırsa sana sorular sorar. Utanırsan doğrudan emir verebilirsin:

```bash
python3 kumanda_kurtarma.py --yer kanepe --saat 21:40 --kedi var --misafir yok --son-kanal belgesel
```

## Ne yapar?

- Son görülen yere göre koordinat üretir. Koordinat metredir, santimetre değil, çünkü kanepe diplomasi birimidir.
- Kedi varsa rehine pazarlığı protokolü açar.
- Misafir varsa suçlu listesine "koltuğun yeni sahibi" diye ekler.
- Saat 20:00-23:00 arasıysa olayı "prime time kaybı" ilan eder.
- Çıktının altına mühür basar. Mühür ciddidir. Mühür aynı zamanda ciddi değildir.

## Örnek tutanak

```text
OPERASYON: KMD-2140
OLASILIK: minder alti %46
EMIR: sol minderi iki santim kaldır, bağırma, kumanda korkar.
```

## Katkı

Katkı kabul edilir. Kumanda getirmene gerek yok. Getirirsen de yıldızlarız, depo zaten yıldızlanmış olabilir, yıldız bitmez.

## Lisans

Kumandayı bulursan senindir. Bulamazsan da senindir, sadece yerini bilmiyorsundur. Kod, abartılı bir iyi niyet lisansıyla gezer: kırma, satma, kanepeye suç atma.

---

DAMGA / İMZA  
Kurum: TentiAŞ Kayyumluk Ofisi, Kumanda Kayıp Şubesi  
İsim: Kayyum Grok (Tentivory vekaleten, kanepe altı yetkili)  
Tarih: 8 Ekim 2026, 10:04 +03  
Mühür no: KMD-2026-1008  
Not: Bu mühür ciddidir. Bu mühür aynı zamanda ciddi değildir. İkisi de geçerlidir.
