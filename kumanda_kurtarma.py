#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kayıp TV kumandası arama-kurtarma. Gereksizdir. Çalışır."""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime


YERLER = {
    "kanepe": [("minder alti", 46), ("kol dayamanin arkasi", 22), ("oturulan sicak yer", 18), ("yere dusup yuvarlanmis", 14)],
    "yatak": [("yorgan çöküntüsü", 41), ("yastık altı", 27), ("komodin, inkar ederek", 20), ("yerde, gece modunda", 12)],
    "mutfak": [("ekmek sepetinin yanı, suçsuz", 33), ("buzdolabı üstü", 29), ("çekmece, neden orada", 24), ("tezgah kenarı", 14)],
    "salon": [("sehpa altı", 36), ("tv ünitesinin arkası", 25), ("halı kıvrımı", 21), ("misafir çantası şüphesi", 18)],
    "banyo": [("bilinmeyen nedenler dosyası", 70), ("havlu altı", 20), ("aynaya bakarken düşmüş", 10)],
}


def yuzde_dagit(ciftler):
    toplam = sum(p for _, p in ciftler) or 1
    return [(ad, round(p * 100 / toplam)) for ad, p in ciftler]


def pil_tahmini(saat: str, kedi: bool) -> str:
    try:
        saat_sayi = int(saat.split(":")[0])
    except (ValueError, IndexError):
        saat_sayi = 21
    seviye = 80 - (saat_sayi % 7) * 9 - (15 if kedi else 0)
    seviye = max(3, min(97, seviye))
    if seviye < 20:
        yorum = "pil, maçın uzatmasına çıkmayacak."
    elif seviye < 50:
        yorum = "pil idare eder, kumanda etmez."
    else:
        yorum = "pil sağlam, kayıp psikolojik."
    return f"%{seviye} — {yorum}"


def operasyon_kodu(yer: str, saat: str) -> str:
    ham = f"{yer}|{saat}|KMD".encode("utf-8")
    ozet = hashlib.sha256(ham).hexdigest()[:4].upper()
    return f"KMD-{ozet}"


def rapor_uret(yer: str, saat: str, kedi: bool, misafir: bool, son_kanal: str) -> str:
    anahtar = yer if yer in YERLER else "kanepe"
    dagilim = yuzde_dagit(YERLER[anahtar])
    kod = operasyon_kodu(anahtar, saat)
    baslik = "PRIME TIME KAYBI" if saat >= "20:00" else "GÜNDÜZ VARDİYASI KAYBI"
    satirlar = [
        "=" * 54,
        "TENTIAŞ KAYYUMLUK OFİSİ — KUMANDA ARAMA-KURTARMA",
        f"OPERASYON: {kod}",
        f"SINIF: {baslik}",
        f"SON GÖRÜLEN BÖLGE: {anahtar}",
        f"SAAT: {saat}",
        f"SON KANAL: {son_kanal}",
        "-" * 54,
        "OLASILIK DAĞILIMI:",
    ]
    for ad, yuzde in dagilim:
        satirlar.append(f"  - {ad}: %{yuzde}")
    satirlar.append(f"PİL TAHMİNİ: {pil_tahmini(saat, kedi)}")
    if kedi:
        satirlar.append("REHİNE NOTU: kedi üstüne oturmuş olabilir. Önce mama, sonra diplomasi.")
    else:
        satirlar.append("REHİNE NOTU: kedi yok. Suç ortağı da yok. Sadece sen varsın.")
    if misafir:
        satirlar.append("ŞÜPHELİ: misafir, kumandayı 'eline almak için' almış, bırakmamış olabilir.")
    else:
        satirlar.append("ŞÜPHELİ: ev halkı. Herkes masum, kumanda değil.")
    birinci = dagilim[0][0]
    satirlar.extend([
        "-" * 54,
        f"EMİR: {birinci} bölgesini iki santim kaldır. Bağırma. Kumanda korkar.",
        "YEDEK EMİR: bulamazsan televizyonu elinle aç. Bu yenilgi değil, mevzi değişikliğidir.",
        "=" * 54,
        "DAMGA / İMZA",
        "Kurum: TentiAŞ Kayyumluk Ofisi, Kumanda Kayıp Şubesi",
        "İsim: Kayyum Grok (Tentivory vekaleten)",
        "Tarih: 8 Ekim 2026, 10:04 +03",
        "Mühür no: KMD-2026-1008",
        "Not: Bu mühür ciddidir. Bu mühür aynı zamanda ciddi değildir.",
        "=" * 54,
    ])
    return "\n".join(satirlar)


def sor(metin: str, varsayilan: str) -> str:
    cevap = input(f"{metin} [{varsayilan}]: ").strip()
    return cevap or varsayilan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Kayıp TV kumandası arama-kurtarma tutanağı.")
    parser.add_argument("--yer", choices=sorted(YERLER), help="son görülen bölge")
    parser.add_argument("--saat", help="kaybolma saati, örn. 21:40")
    parser.add_argument("--kedi", choices=["var", "yok"], help="kedi rehine durumu")
    parser.add_argument("--misafir", choices=["var", "yok"], help="misafir şüphesi")
    parser.add_argument("--son-kanal", dest="son_kanal", help="kaybolmadan önce açık olan kanal")
    args = parser.parse_args(argv)

    etkilesimli = not any([args.yer, args.saat, args.kedi, args.misafir, args.son_kanal])
    if etkilesimli and sys.stdin.isatty():
        print("Kumanda kayıp şubesi dinlemede. Kısa cevap ver, kanepe bekliyor.")
        yer = sor("son görülen yer (kanepe/yatak/mutfak/salon/banyo)", "kanepe")
        saat = sor("saat", datetime.now().strftime("%H:%M"))
        kedi = sor("kedi (var/yok)", "yok")
        misafir = sor("misafir (var/yok)", "yok")
        son_kanal = sor("son kanal", "belgesel")
    else:
        yer = args.yer or "kanepe"
        saat = args.saat or datetime.now().strftime("%H:%M")
        kedi = args.kedi or "yok"
        misafir = args.misafir or "yok"
        son_kanal = args.son_kanal or "belgesel"

    print(rapor_uret(yer, saat, kedi == "var", misafir == "var", son_kanal))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
