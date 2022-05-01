PERTANYAAN_ELLEN = {
    "1. Ranking 10 besar (B/S):": "b",
    "2. Suka makan (B/S):": "b",
    "3. Tidak mengenakan kacamata (B/S):": "s",
    "4. Suka bercanda dengan teman (B/S):": "b",
    "5. Berbeda angkatan (B/S):": "s",
    "6. Suka musik (B/S):": "b",
    "7. Jarang tertawa (B/S):": "s",
    "8. Hobi jajan (B/S):": "b",
    "9. Lebih tinggi (B/S):": "b",
    "10. Tidak suka jalan - jalan (B/S):": "s",
    "11. Tidak suka manis (B/S):": "s",
    "12. Asik (B/S):": "b",
    "13. Jarang beribadah (B/S):": "b",
    "14. Sering bercanda dengan guru (B/S):": "b",
    "15. Jarang bermain hape (B/S):": "s"
}
PERTANYAAN_NICHO = {
    "1. Suka nico (B/S):": "b",
    "2. Ga suka apel (B/S):": "s",
    "3. Suka qamu (B/S):": "b",
    "4. Suka yu (B/S):": "b",
    "5. Suka suka (B/S):": "b",
    "6. Suka spotify (B/S):": "b",
    "7. Suka keshi (B/S):": "b",
    "8. Suka napas (B/S):": "b",
    "9. Suka rang hari minggu (B/S):": "b",
    "10. Suka berbi (B/S):": "b",
    "11. Ga suka dens (B/S):": "s",
    "12. Ga suka krebipeti (B/S):": "s",
    "13. Suka salto (B/S):": "b",
    "14. Ga suka biru (B/S):": "s",
    "15. Suka kiwi (B/S):": "b"
}
PERTANYAAN_RIFANI = {
    "1. Bukan pinter tp cerdas (B/S):": "b",
    "2. Humoris (B/S):": "b",
    "3. pekaaa (B/S):": "b",
    "4. Easy going (B/S):": "b",
    "5. Tinggi atau sepantaran (B/S):": "b",
    "6. Toxic (B/S):": "s",
    "7. Sayang keluarga (B/S):": "s",
    "8. Soft boy (B/S):": "b",
    "9. Pengertian (B/S):": "b",
    "10. Perhatian (B/S):": "b",
    "11. Lucu (B/S):": "b",
    "12. Ga religius (B/S):": "s",
    "13. Kanak - kanak (B/S):": "s",
    "14. Ga suka makan dan jajan (B/S):": "s",
    "15. Body 8 pack (B/S):": "s"
}
jalan = True

while jalan:
    skor = 0

    print("\nHALOOO, SELAMAT DATANG DI TEBAK DOI")
    print("Pilih B untuk Benar dan S untuk Salah")
    print("Mau Tebak Doi Siapa?\n1. Ellen\n2. Nicho\n3. Rifani")
    pertanyaan_doi = [PERTANYAAN_ELLEN, PERTANYAAN_RIFANI, PERTANYAAN_NICHO]
    no_doi = int(input("Pilih (1/2/3): ")) - 1
    for pertanyaan, jawaban in pertanyaan_doi[no_doi].items():
        user_jawab = input(f"{pertanyaan} ")
        if user_jawab.lower() == jawaban:
            skor += 1

    if skor > 7:
        print("Asikk! kamu sudah menebak benar lebih dari setengah pertanyaan, ayo tebak siapa orang itu?")
    else:
        print("Haduuu, kamu belum berhasil menebak benar setengah dari pertanyaan tadi. Ayo coba lagi!")

    lagi = input("\nLagi? (Y/N): ")
    if lagi.lower() == "y":
        skor = 0
        continue
    if lagi.lower() == "n":
        jalan = False
    else:
        print("Pilih yang benar dong bambank, yok lanjut aja :b")

print("TERIMA KASIH SUDAH BERMAIN!")
