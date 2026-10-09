# powpow-register

Asisten pendaftaran PowPow Gelembung (versi OpenClaw): mengantarkan pengguna baru dari «tidak tahu apa itu
Gelembung» sampai «akun aktif, login sekali klik, mulai bermain» — perkenalan produk (dengan tangkapan layar
antarmuka), pendaftaran yang dikerjakan agent (termasuk unggah foto profil), pesanan dan pemantauan langganan
Alipay, login sekali klik dengan tautan ganda, penelusuran galat.

**Sejak v2.0.0 adalah mode agent yang bertindak atas nama**: skrip utama `scripts/powpow-register.mjs` nol
dependensi (Node ≥ 18), pengguna sepanjang proses tidak keluar dari percakapan, hanya dua kali meninggalkan
sebentar: masuk email membaca kode verifikasi, dan membayar di kasir Alipay. Tanpa Node, atau bila pengguna ingin
mengerjakan sendiri, otomatis mundur ke mode panduan murni.

## Pemasangan

```
openclaw skills install @durenzidu/powpow-register
```

## Fitur

1. **Perkenalan produk**: pembukaan ~120 karakter + tangkapan layar antarmuka yang dibundel (`assets/screenshots/`
   berisi 6 gambar: halaman peta, halaman detail postingan, dsb.; pilih kirim 1–3 sesuai skenario; tanpa hosting
   eksternal, bisa dipakai luring).
2. **Pendaftaran atas nama**: agent proaktif menyarankan nama pengguna/nama panggilan, kata sandi pilih 1 dari 2
   (diberikan pengguna atau dibuat agent), pengiriman dan pengisian kode verifikasi, unggah foto profil langsung
   (≤5MB non SVG), penanganan otomatis galat umum (dipakai/kedaluwarsa/limit laju).
3. **Login sekali klik (tautan ganda)**: begitu daftar berhasil diberikan tautan «setengah sesi» yang mendarat
   langsung di halaman langganan; setelah dana masuk, ganti status login baru lalu berikan tautan keanggotaan
   penuh yang mendarat langsung di beranda (lewat jembatan resmi `me?token=` platform, otomatis menanam cookie
   HttpOnly).
4. **Pembayaran langganan**: kanal Alipay dengan pesanan yang dikerjakan agent (bulanan ¥6.99 / triwulan ¥19.99 /
   tahunan ¥69.99, beli putus sekali tanpa perpanjangan otomatis) + polling dana masuk; pengguna luar negeri
   mundur ke PayPal; pindai WeChat/Huawei IAP hanya ditunjukkan jalannya.
5. **Penelusuran galat**: kode verifikasi tidak datang, nama pengguna/email dipakai, 403 belum aktif, akun
   terkunci, dan masalah umum lainnya — semuanya bersumber dari kode platform dengan sumber dicantumkan.

## Struktur file

```
powpow-register/
├── SKILL.md                            # Panduan utama (syarat pemicu, proses 8 langkah, standar nada, aturan keras)
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # Tangkapan layar produk dalam bundel (powpow-01~06.jpg)
├── scripts/
│   └── powpow-register.mjs             # Skrip utama (nol dependensi, Node≥18, 11 sub-perintah)
└── references/
    ├── agent-flow.md                   # Kontrak skrip, urutan lengkap, mekanisme tautan ganda, desain keamanan
    ├── registration-flow.md            # Aturan bidang, batas laju, tabel penelusuran galat (dengan sumber kode)
    ├── payment-and-activation.md       # Kontrak Alipay vibepay, rantai aktivasi, penelusuran per kanal
    └── screenshots.md                  # Daftar tangkapan layar dalam bundel + kilas skenario
```

## Keamanan

- **Kata sandi** hanya masuk ke proses skrip lewat variabel lingkungan, tidak pernah sebagai parameter baris
  perintah, tidak tersimpan ke disk, tidak masuk file status; kata sandi buatan agent hanya ditampilkan sekali
  agar pengguna menyimpannya.
- **Kode verifikasi** hanya untuk antarmuka pendaftaran resmi, dibuang setelah dipakai; file status
  (email/nama pengguna/token/nomor pesanan) tersimpan di direktori sementara sistem, setelah proses selesai
  `cleanup` membersihkannya sekali jalan.
- **Pembayaran**: agent hanya membuat pesanan, membuka kasir, memeriksa dana masuk; tidak pernah menyentuh akun
  Alipay atau bukti pembayaran pengguna, tidak pernah membayarkan. Pembayaran selalu terjadi antara pengguna dan
  kasir resmi Alipay.
- Semua request hanya ke domain resmi `https://global.powpow.online`; tidak berisi kunci apa pun.

## Lisensi

MIT-0 (lisensi terpadu ClawHub).

## Tautan

- Situs resmi: https://global.powpow.online
- Pendaftaran: https://global.powpow.online/register
- Mengenal Gelembung (video): https://www.bilibili.com/video/BV1Wu826UEVz/
