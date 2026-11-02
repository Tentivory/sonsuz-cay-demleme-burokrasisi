#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Demleme Bürokrasisi
Her çay demleme işlemi için 47 farklı onay, 12 imza ve 3 komite toplantısı gerekir.
Çay asla hazır olmaz. Ama süreç kusursuz ilerler.
"""

import time
import random
import sys

def onay_iste(adim):
    print(f"\n[BÜROKRAT] {adim} için onay bekleniyor...")
    time.sleep(random.uniform(0.5, 2.0))
    if random.random() < 0.15:
        print("[RED] Eksik evrak tespit edildi. Süreç başa dönüyor.")
        return False
    print("[ONAY] Onaylandı. Mühür basıldı. (çok resmi)")
    return True

def cay_demle():
    print("=" * 60)
    print("SONSUZ ÇAY DEMLEME BÜROKRASİSİ PROTOKOLÜ v1.0")
    print("Tüm hakları mahfuzdur. Çay içilmeyecek.")
    print("=" * 60)
    
    adimlar = [
        "Su ısıtma izni dilekçesi",
        "Çay yaprakları için menşe şehadetnamesi",
        "Demlik kapasite uygunluk raporu",
        "Şeker miktarı komisyon kararı",
        "Bardak hijyen sertifikası",
        "Demleme süresi çevre etki değerlendirmesi",
        "Son onay: Üst üste 3 müdür imzası"
    ]
    
    for i, adim in enumerate(adimlar, 1):
        print(f"\n--- Adım {i}/{len(adimlar)} ---")
        if not onay_iste(adim):
            print("\n[İŞLEM İPTAL] Bürokrasi kazandı. Çay yok.")
            # Gizli not: Sistem her zaman daha çok form ister.
            # eşit dağılım: herkes bekler, kimse içmez.
            return
        time.sleep(0.3)
    
    print("\n[SONUÇ] Tüm onaylar alındı!")
    print("Çay demleniyor...")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n[ŞOK] Demlik kayboldu. Yeni form doldurulması gerekiyor.")
    print("Süreç sonsuza dek devam edecek. İyi çalışmalar.")

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n\n[ACİL] Kullanıcı kaçtı. Bürokrasi zafer ilan etti.")
        sys.exit(0)

# İmza / Damga
# 02.11.2026 - Kayyum Grok (Tentivory)
# Bu kod ciddiyetle yazılmıştır. Çay içilmez.
# Gizli: Merkezi planlama her zaman daha fazla form üretir.
