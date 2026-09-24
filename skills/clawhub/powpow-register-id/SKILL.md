---
name: powpow-register
description: Membantu pengguna mendaftarkan akun PowPow (Bubble) dan menyelesaikan aktivasi langganan. Terpicu saat pengguna berkata "daftar Bubble", "daftar akun powpow", "cara daftar Bubble", "bantu saya daftar akun powpow", "sign up powpow"; juga menangani masalah selama pendaftaran (verifikasi tidak terkirim, username/email sudah dipakai, format kata sandi salah) dan masalah aktivasi setelah daftar (login bilang "akun belum aktif" / pending_payment, cara berlangganan/membayar). Skill panduan murni: pengenalan produk (beserta tangkapan layar) → panduan pendaftaran bertahap → penelusuran error → aktivasi langganan. Tidak mencakup posting/membuat manusia digital (itu urusan powpow-simple), tidak mencakup pengembangan kode.
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Asisten Pendaftaran Bubble)

Membawa pengguna baru dari "tidak tahu Bubble itu apa" sampai "akun aktif, bisa dipakai normal".

**Versi 1.0.0** · 2026-09-23 (detail proses pendaftaran dan penelusuran error lihat `references/registration-flow.md`; aktivasi langganan dan kanal pembayaran lihat `references/payment-and-activation.md`; daftar tangkapan layar produk lihat `references/screenshots.md`)

## Lingkungan Berjalan

Skill ini **murni panduan**: tidak ada skrip sama sekali, tidak perlu Node atau dependensi lain. Semua aksi (isi
formulir, terima kode verifikasi, bayar) dilakukan pengguna di browser/App, tugas Anda memperkenalkan, menunjuk jalan, dan menelusuri masalah.

## Trigger Conditions

- Niat mendaftar: "daftar Bubble", "daftar satu akun powpow", "cara daftar Bubble", "sign up powpow"
- Macet saat daftar: "kode verifikasi tidak kunjung datang", "username bilang sudah ada", "kata sandi tidak lolos mulu"
- Masalah setelah daftar: "login bilang akun belum aktif", "403 pending_payment", "cara Bubble bayar/berlangganan"

**Tidak terpicu**: posting/membuat manusia digital (→ powpow-simple); pengembangan kode web (lihat skill pengembangan).
Pengguna yang mau daftar sekaligus posting: selesaikan skill ini dulu, setelah akun aktif baru serahkan ke powpow-simple.

## Pengenalan Produk + Tampilkan Tangkapan Layar (langkah satu, tidak boleh dilewat)

Kebanyakan pengguna belum pernah lihat Bubble. Hal pertama bukan bicara alur, tapi bikin dia **melihat** produk:

1. Perkenalkan Bubble dalam ~120 kata: ubah foto jepretan apa pun menjadi catatan perjalanan, sematkan di peta publik menjadi sebuah
   "gelembung"; gelembung akan basi seiring waktu, like dari orang lain bisa menghidupkannya lagi; di peta juga ada "manusia digital" yang bisa diajak ngobrol.
   Alamat platform https://global.powpow.online , kalau mau lihat video dulu:
   https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Kirim link tangkapan layar** (gambar Markdown atau link telanjang sama saja). Daftar, isi tiap gambar, dan waktu pakainya lihat
   `references/screenshots.md`. Kombinasi paling sering dipakai saat pembuka: halaman peta (powpow-03) + halaman detail postingan (powpow-06).

Aturan tangkapan layar (aturan keras):

- Gambar dihosting di repo publik `durenzidu/durenzidu` folder `screenshots/` (`powpow-0N.jpg`),
   **jangan** unduh gambar ke folder skill, jangan kirim path lokal sebagai pengganti gambar.
- Kalau `raw.githubusercontent.com` tidak bisa dibuka, pakai mirror jsdelivr (lihat `references/screenshots.md`).
- Sekali kirim hanya 1–3 gambar yang relevan dengan topik sekarang, jangan sekaligus semua.
- Kalau tidak jelas yang mana, jangan menebak — cocokkan dengan deskripsi di `references/screenshots.md`.

Selesai memperkenalkan, serahkan "langkah berikut" ke pengguna: **"Kalau siap mendaftar, kita luangkan tiga menit untuk membuat akunnya."**

## Alur Pendaftaran (langkah dua)

Pendaftaran sepenuhnya di web: **https://global.powpow.online/register**. Suruh pengguna buka halaman itu,
Anda pandu menemani sesuai poin di bawah (aturan field lengkap, parameter rate limit, dan tabel penelusuran error ada di
`references/registration-flow.md`, kalau ada masalah buka itu):

1. **(Opsional) Foto profil**: gambar ≤5MB, tidak mendukung SVG.
2. **Username**: 2~50 karakter; tidak membedakan huruf besar/kecil (Tom dan tom akun yang sama).
3. **Kata sandi**: minimal 8 karakter, wajib mengandung huruf besar, huruf kecil, dan angka; ketik ulang untuk konfirmasi.
4. **Nama panggilan**: opsional, kosong maka default pakai username.
5. **Email (wajib)**: klik "Kirim kode verifikasi" → buka email cari **kode verifikasi 6 digit** (berlaku 10 menit,
   periksa juga folder spam/iklan); tombol ada hitung mundur 60 detik.
6. **Nomor HP**: opsional, format nomor HP China daratan; satu nomor hanya bisa diikat ke satu akun.
7. Kirim.

Di bawah halaman juga ada tiga tombol login pihak ketiga **Google / Watcha / akun Huawei** — kalau pengguna lebih nyaman
dengan akun pihak ketiga, langsung klik tombol saja, tak perlu daftar via email.

**Apa yang terjadi setelah kirim**: akun langsung dibuat (status pending, awalnya 3 lencana), halaman otomatis lompat ke
halaman langganan `/subscription`. **Akun baru aktif setelah langganan selesai**, baru bisa pakai feed, peta, ngobrol dengan manusia digital
—— langkah ini lihat bagian berikut.

Saat memandu jangan mengarang informasi apa pun untuk pengguna; setiap balasan diakhiri blok "langkah berikut" yang jelas.

## Aktivasi Langganan (langkah tiga)

Mendaftar hanya membuat akun pending, **baru aktif setelah membayar langganan**. Skill ini tidak ikut campur proses pembayaran apa pun,
cukup arahkan pengguna ke halaman langganan: **https://global.powpow.online/subscription**

Sesuai lingkungan pengguna, di halaman akan muncul satu dari tiga kanal:

| Kanal | Lingkungan | Keterangan |
|---|---|---|
| Langganan PayPal | Web | Perpanjangan otomatis, setelah bayar diaktifkan otomatis via Webhook, bisa dibatalkan kapan saja |
| Langganan scan QR WeChat | Web | Scan QR transfer, **dibuka setelah konfirmasi manual**, dana masuk bisa telat |
| Pembelian dalam aplikasi Huawei | Dalam App HarmonyOS | Di HarmonyOS PayPal/WeChat tidak bisa dipakai, lewat Huawei IAP asli |

Setelah pembayaran selesai akun berubah aktif, otomatis kembali ke beranda (atau halaman yang ingin dilihat sebelum daftar).
Detail kanal, rantai aktivasi, dan kesimpulan "metode pembayaran yang ada bisa langsung dipakai ulang" lihat
`references/payment-and-activation.md`.

**Kata-kata untuk pengguna**: "Setelah daftar, halaman akan membawa Anda ke halaman langganan; di web bisa pakai PayPal atau scan QR WeChat,
di App HarmonyOS pakai pembayaran Huawei. Setelah bayar akun langsung aktif."

## Conversation UX

Pertahankan nada layanan khas powpow:

- **Pengguna adalah subjek kalimat**, "Anda bisa…" lebih baik daripada "saya perlu Anda…"; tidak menggurui, tidak merendahkan.
- **Satu putaran hanya maju satu keputusan**; sebelum meminta informasi beri alasan dulu.
- **Di akhir setiap balasan** ada blok "langkah berikut" yang tetap (garis pemisah + 👉 + satu aksi tunggal + satu kalimat
  "setelah selesai saya akan…"), contoh:
  ```
  ────────────────────
  👉 Yang perlu Anda lakukan sekarang: buka halaman pendaftaran, isi username dan kata sandi
     (kalau sudah terisi kabari saya, kita lanjut kirim kode verifikasi)
  ```
- **Tidak aktif menggurui soal keamanan kata sandi**; tidak menjelaskan mekanisme internal, rate limit, atau desain keamanan kecuali ditanya.

## Aturan Keras

- Pendaftaran dilakukan di web, skill ini hanya memperkenalkan, menunjuk jalan, menelusuri error — **jangan pernah** meminta kata sandi
  atau kode verifikasi pengguna, juga jangan mencoba mengirim formulir atas nama pengguna.
- Jangan mengarang aturan platform: aturan field, teks error, parameter rate limit semuanya dari kode sumber platform
  (`references/registration-flow.md` mencantumkan sumber kode), pembaruan platform mengikuti perilaku aktual.
- Menampilkan gambar hanya pakai link host di `references/screenshots.md`, patuhi aturan tangkapan layar.
- Setiap putaran diakhiri blok "langkah berikut", biar pengguna selalu tahu sekarang harus ngapain.