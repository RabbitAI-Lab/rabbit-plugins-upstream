# powpow-register

Asisten pendaftaran PowPow Bubble (versi OpenClaw): membawa pengguna baru dari "tidak tahu Bubble itu apa" sampai
"akun aktif, bisa dipakai normal" — pengenalan produk (beserta tangkapan layar), panduan pendaftaran bertahap,
penelusuran error, penjelasan aktivasi langganan.

Skill panduan murni, tanpa skrip, tanpa dependensi; semua aksi pendaftaran dilakukan pengguna di browser/App.

## Instalasi

```
openclaw skills install @durenzidu/powpow-register
```

## Fitur

1. **Pengenalan produk**: pembuka ~120 kata + link tangkapan layar yang dihosting di repo publik GitHub
   (halaman peta, halaman detail postingan, dll. 6 gambar, pilih kirim 1–3 sesuai situasi).
2. **Panduan pendaftaran**: aturan field (username/kata sandi/kode verifikasi email/nomor HP/foto profil), login pihak ketiga
   (Google/Watcha/Huawei), parameter rate limit, semuanya dari kode sumber platform dan mencantumkan sumber.
3. **Penelusuran error**: kode verifikasi tidak sampai, username/email dipakai, 403 belum aktif, akun terkunci, dll.
   13 masalah umum.
4. **Aktivasi langganan**: penjelasan dan penelusuran tiga kanal PayPal (web) / WeChat scan QR (konfirmasi manual) / Huawei IAP (HarmonyOS);
   rantai pembayaran yang ada bisa langsung dipakai ulang, skill hanya bertugas menunjuk jalan.

## Struktur File

```
powpow-register/
├── SKILL.md                            # Panduan utama (kondisi pemicu, alur, standar nada)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Aturan field, rate limit, tabel penelusuran error (beserta sumber kode)
    ├── payment-and-activation.md       # Aktivasi langganan, kanal pembayaran, kesimpulan pakai ulang
    └── screenshots.md                  # Daftar tangkapan layar host + cek cepat per situasi
```

## Keamanan

- Tidak berisi kunci apa pun; tanpa skrip, tidak menyentuh kredensial pengguna.
- **Jangan pernah meminta** kata sandi, kode verifikasi, atau bukti pembayaran pengguna; pendaftaran dan pembayaran sepenuhnya di halaman platform.

## Lisensi

MIT-0 (lisensi terpadu ClawHub).

## Tautan

- Situs: https://global.powpow.online
- Pendaftaran: https://global.powpow.online/register
- Kenali Bubble (video): https://www.bilibili.com/video/BV1Wu826UEVz/