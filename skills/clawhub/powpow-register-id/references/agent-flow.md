# Alur kerja agent dan kontrak skrip — powpow-register

Rincian eksekusi tiap langkah di SKILL.md. Semua perintah berbentuk `node scripts/powpow-register.mjs <sub-perintah> [parameter]`,
skrip **nol dependensi**, butuh **Node ≥ 18**, semua request hanya dikirim ke `https://global.powpow.online`.

## Desain keamanan (kenapa dirancang begini)

| Desain | Alasan |
|---|---|
| Kata sandi hanya masuk lewat variabel lingkungan `POWPOW_REGISTER_PASSWORD` | Parameter baris perintah proses terlihat oleh proses lain pada mesin yang sama (permukaan bocor argv), variabel lingkungan dibaca lalu langsung dipakai di dalam skrip |
| Kata sandi **tidak pernah ditulis ke file status**, tidak pernah muncul di log | File status bisa tertinggal di disk; mode buat dalam percakapan menampilkannya sekali agar pengguna menyimpan |
| File status di direktori sementara sistem (`os.tmpdir()/powpow-register-state.json`, 0600) | Hanya berisi lima bidang email / username / nickname / token / outTradeNo, `cleanup` membersihkannya sekali jalan |
| JWT yang didapat agent ditukar menjadi cookie browser lewat endpoint resmi `me?token=` | Jembatan resmi platform yang didesain untuk WebView HarmonyOS; verifikasi tanda tangan hanya memeriksa tanda tangan + masa berlaku, tidak mengikat sidik perangkat, sehingga browser pengguna bisa memakainya |
| Pembayaran hanya create-order / query / membuka kasir | Aksi membayar dan bukti pembayaran selamanya berada antara pengguna dan kasir resmi Alipay, agent tidak ikut campur |

## Referensi perintah

| Perintah | Parameter kunci | Fungsi / momen |
|---|---|---|
| `status` | —— | Melihat kemajuan proses (membaca file status); setelah percakapan terputus jalankan ini dulu |
| `gen-password` | —— | Membuat kata sandi kuat 24 karakter (berisi huruf besar+kecil+angka), stdout menampilkannya **hanya sekali ini** |
| `prepare-suggest` | `--username --nickname --email` | Mencatat info yang sudah dikonfirmasi ke file status (setelah itu register tak perlu mengirim ulang) |
| `send-code` | `--email` | Memicu platform mengirim kode verifikasi 6 digit (berlaku 10 menit, jeda 60 dtk) |
| `register` | `--code` (wajib); `--username --nickname --avatar --phone` (opsional, jika ada di file status tak perlu dikirim) | Membuat akun pending; kata sandi lewat variabel lingkungan `POWPOW_REGISTER_PASSWORD`; setelah berhasil JWT otomatis tersimpan di file status |
| `login-link` | `--target pending` atau `--target home` | Menghasilkan tautan login sekali klik (desain tautan ganda, lihat bawah) |
| `create-order` | `--package monthly\|quarterly\|yearly` | Membuat pesanan Alipay; mengembalikan path file halaman pembayaran + outTradeNo (otomatis dicatat ke file status) |
| `query` | —— | Memeriksa status pesanan `paid / pending / closed / unknown` (outTradeNo diambil dari file status), polling 10–15 dtk |
| `refresh-login` | kata sandi lewat variabel lingkungan | Login ulang untuk **JWT baru** (klaim langganan berubah dari NONE ke ACTIVE), wajib dijalankan setelah dana masuk |
| `whoami` | —— | Memakai token di file status untuk memeriksa akun dan status langganan (memastikan aktivasi berhasil) |
| `cleanup` | —— | Menghapus file status (wajib dijalankan saat penutup) |

**Penerusan variabel lingkungan** (kata sandi tidak pernah naik ke baris perintah):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<kata sandi>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<kata sandi>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<kata sandi> && node scripts/powpow-register.mjs register --code 123456
```

## Mekanisme tautan ganda (desain inti)

Status login platform adalah cookie HttpOnly, agent tidak bisa langsung menanam cookie untuk browser orang lain;
jembatannya adalah endpoint resmi `/api/auth/me?token=<JWT>&redirect=<jalur dalam situs>`: verifikasi tanda
tangan → pengguna pending otomatis dibuatkan sesi → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax /
7 hari) → validasi redirect (hanya boleh diawali satu garis miring, dilarang `//` dan backslash, setelah resolusi
harus same-origin) → 307 pengalihan sementara ke halaman tujuan.

- **Tautan 1 (diberikan begitu daftar berhasil)**: `--target pending` → mendarat di `/subscription`.
  Browser pengguna memasuki kondisi «setengah sesi»: halaman langganan dan halaman lompat-balik Alipay terlihat
  dan bisa dioperasikan; halaman konten tetap ditahan paywall kembali ke halaman langganan (tiga lapis
  pengamanan: pemeriksaan klaim JWT di gateway → pemeriksaan ulang DB → pemeriksaan API inti; perilaku normal).
- **Tautan 2 (diberikan setelah paid terkonfirmasi)**: lebih dulu `refresh-login` untuk JWT baru (pembayaran hanya
  memperbarui DB, tidak mengubah klaim JWT yang sudah terbit; tanpa penggantian akan tampak seperti «sudah bayar
  tapi bukan anggota»), lalu `--target home` → mendarat di beranda, status keanggotaan lengkap.

## Urutan lengkap (jalur normal)

```
1.  status                          # Cek mandiri lingkungan
2.  (Langkah 2: konfirmasi info lewat percakapan, kata sandi pilih 1 dari 2; mode buat: gen-password → suruh pengguna langsung menyimpan)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → pengguna masuk email membaca kode (satu-satunya keluar dari percakapan ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → tautan 1 dikirim ke pengguna
7.  (pengguna memilih paket) create-order --package monthly
8.  start <file halaman pembayaran>  # Windows; macOS pakai open, Linux pakai xdg-open
    # → pengguna membayar di kasir Alipay (keluar dari percakapan ②)
9.  query (tiap 10–15 dtk) sampai paid
10. refresh-login                   # Dapatkan JWT baru berklaim ACTIVE
11. login-link --target home        # → tautan 2 dikirim ke pengguna
12. whoami                          # Pastikan subscriptionStatus: ACTIVE (opsional)
13. cleanup                         # Bersihkan file status
```

## Pemetaan perintah → API platform

| Perintah skrip | Antarmuka platform |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, unggah foto profil langsung) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (tautannya sendiri, berlaku saat browser mengeklik) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Sumber aturan: bidang pendaftaran dan batas laju lihat `registration-flow.md`; paket dan rantai aktivasi lihat
`payment-and-activation.md` (keduanya mencantumkan file kode sumber platform).

## Penanganan galat tingkat skrip

| Gejala | Penanganan |
|---|---|
| `Node 版本过低` (versi Node terlalu rendah) | Mundur ke mode panduan murni, jangan memaksakan |
| Galat jaringan / habis waktu | Coba sekali lagi; bila tetap gagal suruh pengguna memeriksa jaringan lalu lanjutkan (file status masih ada, jalankan `status` dari awal untuk pulih) |
| register melaporkan galat bisnis (nama pengguna sudah ada, dsb.) | Tangani sesuai tabel langkah 5 SKILL.md, **kode verifikasi tak perlu dikirim ulang** (masih berlaku 10 menit) |
| register melaporkan 「邮箱验证码错误或已过期」 (kode verifikasi salah atau kedaluwarsa) | Lewat masa berlaku → `send-code` ulang |
| Setelah `create-order` pengguna menutup halaman pembayaran | Langsung `create-order` ulang (pesanan lama tertutup otomatis 2 jam) |
| `query` terus pending | Pengguna mungkin belum membayar; tanyakan sekali. Kalau sudah bayar → ikuti tabel penelusuran di payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Dana belum masuk, kembali ke langkah 9 lanjut polling |
| File status hilang (tak sengaja terhapus / ganti mesin) | `whoami`/`refresh-login` tak bisa dipakai; suruh pengguna membuka ulang halaman langganan di browser yang pernah membuka tautan 1 untuk memastikan status, atau login ulang (mode web) |

## Mode mundur (panduan murni)

Bila salah satu kondisi berikut terjadi, segera mundur ke panduan murni gaya v1 dan berhenti memeras skrip:

- Tidak ada Node ≥ 18 atau skrip gagal dua kali berturut-turut dengan jenis yang sama;
- Pengguna secara eksplisit bilang «aku kerjakan sendiri di web»;
- Kebijakan perusahaan/perangkat membatasi skrip mengakses jaringan.

Setelah mundur: berikan halaman pendaftaran https://global.powpow.online/register dan halaman langganan
https://global.powpow.online/subscription , dampingi penelusuran galat sesuai aturan `registration-flow.md`,
nada tidak berubah, tiap giliran tetap ditutup blok «langkah berikutnya».
