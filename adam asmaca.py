import random

KELIMELER = [
    "python", "bilgisayar", "klavye", "program", "degisken",
    "fonksiyon", "algoritma", "internet", "yazilim", "dongu",
]

MAKSIMUM_HATA = 6

ASAMALAR = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def kelimeyi_goster(kelime, tahminler):
    """Bilinen harfleri gösterir, bilinmeyenleri _ ile saklar."""
    return " ".join(harf if harf in tahminler else "_" for harf in kelime)


def harf_al(tahminler):
    """Geçerli ve daha önce denenmemiş bir harf alır."""
    while True:
        tahmin = input("Bir harf tahmin edin: ").lower().strip()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Hata: Lütfen tek bir harf girin.")
        elif tahmin in tahminler:
            print("Bu harfi zaten denediniz.")
        else:
            return tahmin


def oyna():
    kelime = random.choice(KELIMELER)
    tahminler = set()
    hata_sayisi = 0

    print("\n=== ADAM ASMACA ===")

    while hata_sayisi < MAKSIMUM_HATA:
        print(ASAMALAR[hata_sayisi])
        print("\nKelime:", kelimeyi_goster(kelime, tahminler))
        print("Denenen harfler:", " ".join(sorted(tahminler)) or "-")
        print(f"Kalan hak: {MAKSIMUM_HATA - hata_sayisi}")

        tahmin = harf_al(tahminler)
        tahminler.add(tahmin)

        if tahmin in kelime:
            print("Doğru!")
        else:
            hata_sayisi += 1
            print("Yanlış!")

        if all(harf in tahminler for harf in kelime):
            print("\nKelime:", kelimeyi_goster(kelime, tahminler))
            print("Tebrikler, kazandınız! 🎉")
            return

    print(ASAMALAR[MAKSIMUM_HATA])
    print(f"\nKaybettiniz! Kelime: {kelime}")


def main():
    while True:
        oyna()
        tekrar = input("\nTekrar oynamak ister misiniz? (e/h): ").lower().strip()
        if tekrar != "e":
            print("Görüşmek üzere!")
            break


if __name__ == "__main__":
    main()