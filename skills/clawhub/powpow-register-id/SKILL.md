---
name: powpow-register
description: Membantu pengguna menyelesaikan pendaftaran PowPow (Gelembung), mengaktifkan langganan lewat Alipay, dan login sekali klik langsung di dalam percakapan. Agent mengisi formulir atas nama pengguna (termasuk mengunggah foto profil), mengirim kode verifikasi via email, membuat pesanan pembayaran, dan memantau sampai dana masuk; pengguna cukup memberikan informasi dasar, membaca kode satu kali di kotak masuk, dan membayar di halaman kasir Alipay — seluruh proses tanpa keluar dari percakapan. Aktif saat pengguna berkata «daftar Gelembung», «buat akun powpow», «cara daftar Gelembung», «bantu saya buat akun powpow», «sign up powpow»; juga menangani pendaftaran yang macet (kode verifikasi tidak datang, nama pengguna/email sudah dipakai) dan masalah aktivasi (login bilang «akun belum diaktifkan» / pending_payment, cara bayar langganan). Butuh Node ≥ 18; jika tidak ada akan otomatis mundur ke mode panduan murni. Tidak termasuk memposting/membuat manusia digital (itu tugas powpow-simple) dan tidak termasuk pengembangan kode.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (asisten pendaftaran Gelembung)

Mengantarkan pengguna baru dari «tidak tahu apa itu Gelembung» sampai «akun aktif, login sekali klik, mulai bermain» — semuanya di dalam percakapan. Pengguna hanya meninggalkan obrolan dua kali sebentar: **masuk email untuk membaca kode verifikasi** dan **membayar di halaman kasir Alipay** (agent akan membuka halaman pembayarannya sendiri).

**Versi 2.0.1** · 2026-10-08 (sejak v2 adalah mode agent yang bertindak atas nama: kontrak skrip dan urutan lengkap ada di `references/agent-flow.md`; aturan bidang, batas laju, dan penanganan galat ada di `references/registration-flow.md`; kanal pembayaran ada di `references/payment-and-activation.md`; daftar tangkapan layar produk ada di `references/screenshots.md`. Sejak v2.0.1 tangkapan layar produk dibundel bersama skill di `assets/screenshots/`, tidak bergantung pada layanan hosting gambar eksternal)

## Lingkungan eksekusi

- Skrip utama `scripts/powpow-register.mjs`: **nol dependensi**, butuh **Node ≥ 18**. Sebelum mulai, jalankan sekali `node scripts/powpow-register.mjs status` untuk memastikan lingkungan berfungsi.
- Semua request skrip hanya dikirim ke domain resmi `https://global.powpow.online`.
- **Tidak ada Node / skrip melaporkan galat**: otomatis mundur ke mode panduan murni — berikan pengguna halaman pendaftaran https://global.powpow.online/register dan halaman langganan https://global.powpow.online/subscription, dampingi sesuai `references/registration-flow.md`. Jangan terus mencoba-coba skrip tanpa henti.
- Pemulihan setelah percakapan terputus: jalankan `status` dulu untuk melihat proses berhenti di langkah mana, lalu lanjutkan dari sana.

## Trigger Conditions

- Niat mendaftar: «daftar Gelembung», «buat akun powpow», «cara daftar Gelembung», «sign up powpow»
- Pendaftaran macet: «kode verifikasi tidak datang», «katanya nama pengguna sudah ada», «kata sandi terus tidak lolos»
- Masalah pasca-daftar: «login bilang akun belum diaktifkan», «403 pending_payment», «cara bayar/berlangganan di Gelembung»

**Tidak aktif untuk**: memposting/membuat manusia digital (→ powpow-simple); pengembangan kode sisi Web (lihat skill pengembangan). Pengguna yang ingin mendaftar sekaligus memposting: selesaikan skill ini dulu, setelah aktif baru serahkan ke powpow-simple.

## Gambaran proses

| Langkah | Apa yang agent lakukan | Apa yang pengguna lakukan |
|---|---|---|
| 1 Perkenalan produk | Memperkenalkan + mengirim tangkapan layar | Melihat sebentar |
| 2 Konfirmasi info | Merekomendasikan nama pengguna/nama panggilan, kata sandi pilih 1 dari 2, menanyakan email | Mengonfirmasi, memberi data |
| 3 Kirim kode | `send-code` | —— |
| 4 Baca kode | —— | Masuk email, membaca kode 6 digit, mengirimkannya |
| 5 Kirim pendaftaran | `register` (termasuk unggah foto profil), menangani galat otomatis | —— |
| 6 Setengah sesi + bayar | `login-link(pending)` → `create-order` → membuka kasir → polling `query` | Membuka tautan, membayar |
| 7 Login resmi | `refresh-login` → `login-link(home)` | Membuka tautan masuk ke beranda |
| 8 Penutup | `cleanup` + menyerahkan info akun + panduan pengalaman + saran plugin | Mulai bermain |

## Langkah 1: perkenalan produk + tangkapan layar (tidak boleh dilewati)

Sebagian besar pengguna belum pernah melihat Gelembung. Hal pertama bukan menceritakan proses, melainkan membuat mereka **melihat** produknya:

1. Perkenalkan Gelembung dalam ~120 karakter: mengubah foto-foto spontan menjadi catatan perjalanan, menyematkannya di peta publik sebagai sebuah «gelembung»; gelembung mendingin seiring waktu, «suka» dari orang lain bisa menghidupkannya kembali; di peta juga ada «manusia digital» yang bisa diajak ngobrol. Alamat platform: https://global.powpow.online ; ingin lihat video dulu: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Kirim tangkapan layar**. Tangkapan layar sudah dibundel bersama skill di `assets/screenshots/powpow-0N.jpg` — kirim langsung sebagai file gambar lokal, tanpa perlu internet. Daftar, isi tiap gambar, dan momen penggunaannya ada di `references/screenshots.md`. Pasangan yang paling sering dipakai di pembukaan: halaman peta (powpow-03) + halaman detail postingan (powpow-06).

Aturan tangkapan layar (aturan keras):

- Tangkapan layar **sudah dibundel bersama skill** di `assets/screenshots/` (`powpow-0N.jpg`) — kirim langsung sebagai file gambar lokal; bisa dipakai di semua lingkungan, termasuk yang tidak bisa membuka GitHub.
- Setiap kali kirim hanya 1–3 gambar yang relevan dengan topik saat ini, jangan menumpuk semuanya sekaligus.
- Jika file di dalam bundel hilang tak sengaja, fallback ke tautan hosting yang tercantum di `references/screenshots.md` (catatan: di daratan Tiongkok bisa saja tidak terbuka).

Selesai memperkenalkan, kembalikan pilihan ke pengguna: **«Kalau kamu mau daftar, tiga menit lagi akunmu selesai saya buat di obrolan ini; kamu cukup membaca kode verifikasi di email satu kali.»**

## Langkah 2: konfirmasi info pendaftaran (satu pertanyaan per giliran, jangan menanyakan semuanya sekaligus)

- **Nama pengguna** (wajib): **proaktif menyarankan satu** dari konteks percakapan/nama pengguna sistem (2~50 karakter, tidak peka huruf besar/kecil); pengguna mengangguk ya dipakai, mau ganti ya diganti.
- **Kata sandi** (wajib; lebih dulu suruh memilih 1 dari 2):
  - Pengguna memberikan sendiri → lalu sampaikan ke skrip lewat variabel lingkungan, **jangan sekali-kali memasukkannya ke parameter baris perintah**;
  - agent yang membuat → jalankan `node scripts/powpow-register.mjs gen-password` dan **segera kirim kata sandi yang baru dibuat ke pengguna untuk disimpan** (hanya ditampilkan sekali, setelah itu tidak muncul lagi).
- **Email** (wajib): harus diberikan pengguna sendiri — ini jangkar identitas akun, **jangan menebak-nebak**.
- **Nama panggilan** (opsional): sarankan bawaan sama dengan nama pengguna.
- **Foto profil** (opsional): jika pengguna memberi path gambar lokal (≤5MB, bukan SVG) skrip mengunggahnya langsung; kalau tidak ada ya dilewati (platform memakai logo bawaan); jika kamu punya kemampuan menghasilkan gambar, boleh menawarkan membuatkan satu.
- **Nomor telepon** (opsional, nomor daratan Tiongkok): bawaan dilewati; tanyakan hanya jika pengguna secara eksplisit ingin mengaitkannya.

Setelah dikonfirmasi bisa menjalankan `prepare-suggest --username U --nickname N --email E` untuk mencatatnya ke file status (setelah itu register tak perlu mengirim ulang).

## Langkah 3–4: kode verifikasi via email (satu-satunya bagian yang harus keluar dari percakapan)

```
node scripts/powpow-register.mjs send-code --email <email>
```

Lalu jelaskan ke pengguna: **masuk email dan cari kode verifikasi 6 digit, berlaku 10 menit; jangan lupa periksa folder spam/promosi**; kalau sudah ketemu kembalilah dan kirimkan kodenya. Pengiriman punya jeda 60 detik, jangan menekan-nekan terus.

## Langkah 5: mengirim pendaftaran (agent yang bertindak)

```
POWPOW_REGISTER_PASSWORD=<kata sandi> node scripts/powpow-register.mjs register --code <kode> [--username U] [--nickname N] [--avatar <path gambar lokal>] [--phone P]
```

Berhasil berarti akun sudah dibuat (status pending, dengan 3 lencana pembuka). Galat yang sering terjadi ditangani otomatis, tanpa mengganggu pengguna:

| Galat | Penanganan |
|---|---|
| 「用户名已存在」 (nama pengguna sudah ada) | Otomatis menyarankan variasi (nama pengguna + angka), begitu pengguna mengonfirmasi langsung coba lagi (kode masih berlaku, tidak perlu dikirim ulang) |
| 「邮箱已被使用」 (email sudah dipakai) | Tanyakan ke pengguna: ganti email, atau sebenarnya sudah punya akun? (beralih ke login/lupa kata sandi) |
| 「邮箱验证码错误或已过期」 (kode verifikasi salah atau kedaluwarsa) | Lebih dari 10 menit → jalankan `send-code` lagi |
| Kirim/daftar terlalu sering (429) | Tunggu 1 menit lalu coba lagi; cukup kabari pengguna satu kalimat |

## Langkah 6: login sekali klik (tautan 1) + pembayaran

1. Begitu pendaftaran berhasil:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Kirim tautan ke pengguna: **dibuka di browser dan jatuh langsung ke halaman langganan, sudah dalam kondisi login** — supaya setelah membayar, halaman lompat-balik menampilkan «pembayaran berhasil» dengan benar. (Dalam kondisi ini halaman konten tetap diarahkan balik ke halaman langganan: itu perilaku normal paywall platform, bukan bug, dan tidak perlu menjelaskan mekanisme internal ke pengguna.)
2. Tiga paket untuk dipilih, saat memperkenalkan sertakan harganya:
   - Bulanan **¥6.99** (disarankan saat baru mencoba) / Triwulan **¥19.99** / Tahunan **¥69.99** — dengan Alipay sekali beli putus untuk periode terkait, **tanpa perpanjangan otomatis**
3. Setelah pengguna memilih:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   Skrip mengembalikan path file halaman pembayaran; **buka langsung dengan perintah sistem** (Windows: `start <file>`; macOS: `open <file>`; Linux: `xdg-open <file>`). Browser melompat sendiri ke halaman kasir resmi Alipay; pengguna memindai QR atau masuk ke Alipay untuk membayar.
4. Jalankan `query` setiap 10–15 detik sampai mengembalikan `paid` (dana masuk biasanya beberapa detik sampai satu menit). Pengguna menutup halaman pembayaran di tengah jalan → langsung jalankan `create-order` lagi (pesanan lama tertutup otomatis dalam 2 jam, tak perlu dipikirkan).
5. Pengguna luar negeri/tanpa Alipay: arahkan memakai kanal PayPal di halaman langganan (skill tidak bertindak atas nama, hanya menunjukkan jalan); kanal pindai QR WeChat perlu konfirmasi manual, dana masuknya lambat. Setelah pembayaran selesai tetap kembali ke langkah 7 seperti biasa.

## Langkah 7: login resmi (tautan 2)

Setelah dana masuk terkonfirmasi, lebih dulu ganti ke status login dengan klaim langganan terbaru, baru buat tautan langsung ke beranda:

```
POWPOW_REGISTER_PASSWORD=<kata sandi> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Kirim tautan ke pengguna: **dibuka dan jatuh langsung ke beranda, status keanggotaan lengkap**; sampai di sini seluruh proses pendaftaran tuntas.

## Langkah 8: penutup

1. `node scripts/powpow-register.mjs cleanup` membersihkan file status sementara di mesin (informasi sesi login).
2. Serahkan ke pengguna sebuah «kartu akun»: nama pengguna, email, dan tanggal berakhirnya keanggotaan (kata sandi tidak ditampilkan lagi — mode buat kata sandi sudah membuat pengguna menyimpannya saat dibuat; kalau dia yang menetapkan, dia memang sudah tahu).
3. Panduan pengalaman pertama: berkeliling peta, posting catatan perjalanan pertama (→ serahkan ke powpow-simple).
4. Sarankan ekstensi: skill `@durenzidu/powpow-integration` dan plugin `@durenzidu/openclaw-channel-powpow` — menghubungkan Gelembung ke agent milik pengguna sendiri; jika tertarik berikan perintah pemasangannya.
5. Tutup dengan blok «langkah berikutnya».

## Conversation UX

Pertahankan nada layanan khas powpow:

- **Pengguna adalah subjek kalimat**; «kamu bisa…» lebih baik daripada «aku butuh kamu untuk…»; jangan menggurui, jangan merendahkan.
- **Satu kemajuan keputusan per giliran**; sebelum meminta informasi, sampaikan alasannya dulu.
- **Di ujung setiap jawaban** ada blok «langkah berikutnya» yang tetap (pemisah + 👉 + satu tindakan + satu kalimat «setelah kamu selesai, aku akan…»), contoh:
  ```
  ────────────────────
  👉 Giliranmu: masuk email, cari kode 6 digit, dan kirim langsung ke aku
     (begitu kodenya kuterima, akunmu langsung kubuat)
  ```
- **Jangan proaktif kuliah keamanan soal kata sandi**; jangan menjelaskan mekanisme internal, batas laju, atau desain keamanan, kecuali pengguna bertanya.
- Semakin agent bertindak atas nama, semakin harus melaporkan kemajuan: setelah tiap langkah skrip, beri tahu pengguna satu kalimat tentang apa yang barusan terjadi («akunmu sudah jadi», «halaman pembayarannya sudah kubuka»).

## Aturan keras

- **Keamanan kredensial**: kata sandi hanya disampaikan ke skrip lewat variabel lingkungan `POWPOW_REGISTER_PASSWORD`, **jangan sekali-kali** lewat parameter baris perintah (terlihat di daftar proses), jangan ditulis ke file mana pun (mode buat kata sandi ditampilkan sekali agar pengguna menyimpan, setelah itu tidak disebut lagi). Kode verifikasi hanya untuk antarmuka pendaftaran resmi dan dibuang setelah dipakai.
- **Batas resmi**: semua request hanya dikirim ke `https://global.powpow.online` (sudah tertanam di skrip); jangan pernah mengirim informasi pengguna ke alamat pihak ketiga mana pun.
- **Batas pembayaran**: agent hanya membuat pesanan, membuka kasir, memeriksa dana masuk; **jangan sekali-kali** menyentuh akun Alipay/bukti pembayaran pengguna, dan jangan sekali-kali menjanjikan «kubayarin».
- **Paywall bukan bug**: status pending bisa masuk halaman langganan/halaman lompat-balik adalah izin lewat yang memang didesain; halaman konten yang diblokir adalah paywall yang bekerja normal; jangan cari cara memutarnya.
- **Kebebasan mundur**: jika di langkah mana pun pengguna ingin mengerjakan sendiri, atau lingkungan tidak bisa menjalankan skrip, mundurlah kapan saja ke mode panduan murni — berikan tautan, jelaskan aturannya, atasi galat bersama-sama.
- Jangan mengarang aturan platform: aturan bidang, teks galat, parameter batas laju semuanya berasal dari kode platform (`references/registration-flow.md` mencantumkan sumbernya); bila platform diperbarui, perilaku nyata yang jadi patokan.
- Saat menampilkan gambar gunakan hanya tangkapan layar dalam bundel `assets/screenshots/` (kegunaan tiap gambar lihat di `references/screenshots.md`).
- Tutup setiap giliran dengan blok «langkah berikutnya», supaya pengguna selalu tahu apa yang harus dilakukannya sekarang.
