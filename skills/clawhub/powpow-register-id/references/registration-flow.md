# Alur pendaftaran secara rinci — powpow-register

Untuk dirujuk saat menelusuri masalah. Semua aturan bersumber dari kode platform (validasi konsistensi
frontend-backend Next.js), sumbernya dicantumkan. Bila platform diperbarui, perilaku daring yang sebenarnya
adalah acuan.

## Titik masuk

- Halaman pendaftaran: https://global.powpow.online/register
- Halaman login: https://global.powpow.online/login
- Halaman langganan: https://global.powpow.online/subscription
- Bila masuk lewat tautan bagikan dsb. yang membawa `?next=...`, setelah pendaftaran+pembayaran selesai otomatis
  melompat kembali ke halaman semula.

## Bidang formulir dan aturan

| Bidang | Wajib | Aturan | Sumber kode |
|---|---|---|---|
| Foto profil | opsional | Gambar ≤5MB, SVG tidak didukung; sisi server mengompresi otomatis (saat >100KB dikompresi ke 400×400 / kualitas 90) | `src/app/api/auth/register/route.ts` |
| Nama pengguna | wajib | 2~50 karakter, setelah trim disimpan diubah ke **huruf kecil** (Tom dan tom dianggap nama pengguna yang sama, sisi pendaftaran maupun sisi login sama-sama tidak peka huruf besar/kecil) | sama (zod schema) |
| Kata sandi | wajib | 8~100 karakter, wajib sekaligus memuat huruf besar, huruf kecil, angka | sama |
| Konfirmasi kata sandi | wajib | Sama dengan kata sandi (hanya divalidasi sisi frontend) | `src/app/(public)/register/page.tsx` |
| Nama panggilan | opsional | ≤100 karakter; bila kosong bawaannya memakai nama pengguna | register route |
| Email | **wajib** | Format email sah, ≤255 karakter; satu email hanya bisa mendaftarkan satu akun | register route |
| Kode verifikasi email | **wajib** | 6 digit angka; **berlaku 10 menit**; begitu verifikasi berhasil langsung hangus; kirim ulang akan menandai kode lama sebagai sudah dipakai | `src/lib/email-verification.ts` |
| Nomor ponsel | opsional | Nomor ponsel daratan Tiongkok diawali `1[3-9]` sepanjang 11 digit; satu nomor ponsel hanya bisa terikat satu akun | register route |

Halaman juga menyediakan tiga tombol login pihak ketiga: **Google, Watcha, akun Huawei** (`GoogleSignInButton`
/ `WatchaLoginButton` / `HuaweiLoginButton`). Akun pihak ketiga tidak punya kata sandi lokal, setelahnya memakai
login kata sandi akan mendapat 「该账号未设置密码，请使用其他方式登录」 (akun ini belum mengatur kata sandi,
silakan login dengan cara lain).

## Parameter pembatasan laju dan anti-brute force

| Perilaku | Batasan | Sumber |
|---|---|---|
| Pengajuan pendaftaran | **3 kali/menit/IP**, melebihi batas 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Mengirim kode verifikasi | IP sama 1 kali/menit **dan** email sama 1 kali/menit, melebihi batas 429; tombol frontend hitung mundur 60 detik | `src/app/api/auth/register/send-code/route.ts` |
| Validasi kode verifikasi | Per email maksimal **5 kali** percobaan dalam 10 menit, setelah mencapai batas meski kodenya benar tetap ditolak, perlu mengirim ulang kode | `src/lib/email-verification.ts` |
| Mengirim kode lupa kata sandi | 1 kali/menit/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 kali/menit/IP; akun yang sama gagal berturut-turut **5 kali terkunci 30 menit** (423), selama itu sisa kesempatan ditampilkan menurun | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Perilaku perlindungan privasi**: saat mengirim kode verifikasi / lupa kata sandi, bila email sudah terdaftar
atau tidak ada, antarmuka sama-sama mengembalikan teks sukses, tidak membocorkan apakah email sudah terdaftar.

## Ekuivalensi mode pengerjaan agent dan pendaftaran web

Skrip skill memanggil **batch API publik yang sama** (`/api/auth/register`, `send-code`, `login`,
`/api/auth/me`), menempuh jalur validasi, pembatasan laju, dan galat yang persis sama dengan pengiriman
formulir halaman pendaftaran — semua aturan dalam file ini berlaku sama untuk kedua mode. Urutan dan kontrak
perintah skrip lihat `references/agent-flow.md`.

## Alur status setelah pendaftaran berhasil

1. Pengguna masuk basis data dengan `accountStatus: 'pending'`, awalnya **3 lencana** (register route).
2. Sisi server sekaligus menanam dua cookie HttpOnly: JWT (bisa langsung mengakses `/subscription`) dan
   pendingUserToken (kredensial identitas alur langganan).
3. Halaman pendaftaran mendeteksi `pending_payment` → mengalihkan ke `/subscription` (mempertahankan parameter
   lompat-balik `next`); dalam mode pengerjaan agent memakai `me?token=…&redirect=/subscription` mencapai efek
   yang sama.
4. Pembayaran selesai → `accountStatus` berubah menjadi `active` (**Alipay lewat notify diaktifkan otomatis sisi
   server; PayPal lewat Webhook diaktifkan otomatis; pindai WeChat dikonfirmasi manual; Huawei IAP lewat
   `activate-huawei`**). Rincian lihat `payment-and-activation.md`.

Pengguna belum aktif (pending) yang memanggil API inti (feed, peta, percakapan manusia digital, absen, dsb.)
selalu 403; kecuali tautan bagikan postingan (tetap bisa diakses publik).

## Tabel penelusuran galat umum

| Gejala | Penyebab | Apa yang dilakukan |
|---|---|---|
| 「用户名已存在」 (nama pengguna sudah ada) | Nama pengguna terpakai (tidak peduli huruf besar/kecil) | Ganti nama pengguna lain |
| 「邮箱已被使用」 (email sudah dipakai) | Email pernah dipakai mendaftar | Ganti email; atau beralih ke login + «lupa kata sandi» untuk memulihkan akun lama |
| 「邮箱验证码错误或已过期」 (kode verifikasi email salah atau kedaluwarsa) | Kode salah / lewat 10 menit / ditolak karena salah coba lebih dari 5 kali | Klik «kirim ulang», pakai kode verifikasi dari **email terbaru** |
| Kode verifikasi tidak terkirim | Pembatasan laju 60 detik; atau masuk folder sampah/iklan | Tunggu hitungan mundur selesai baru kirim; periksa folder spam |
| 「手机号已被使用」 (nomor ponsel sudah dipakai) | Nomor ponsel sudah terikat akun lain | Hapus nomor ponsel (opsional) atau ganti nomor |
| 「注册请求过于频繁」 (permintaan pendaftaran terlalu sering) / 429 | Pendaftaran 3 kali/menit/IP menyentuh batas | Tunggu beberapa menit lalu coba lagi |
| 409 「用户名或邮箱已被注册」 (nama pengguna atau email sudah terdaftar) | Bertabrakan nama dengan orang lain di saat mengirim (jaring pengaman konkurensi) | Ganti nama pengguna atau email lalu coba lagi |
| 「图片大小不能超过5MB」 (ukuran gambar tidak boleh melebihi 5MB) / 「不支持 SVG」 (SVG tidak didukung) | Foto profil tidak sesuai ketentuan | Ganti gambar atau lewati foto profil |
| Pendaftaran berhasil tapi login 403 「请完成订阅以激活账户」 (selesaikan langganan untuk mengaktifkan akun) | Akun masih pending (status yang diharapkan sebelum membayar) | Sebelum membayar: ini normal, lebih dulu selesaikan langganan; setelah membayar tetap 403: berarti memakai JWT lama, dalam mode skrip lebih dulu `refresh-login` menukar status login baru |
| Login 423 「账户已锁定」 (akun terkunci) | Kata sandi salah 5 kali berturut-turut | Tunggu 30 menit |
| Login 401 「还剩 N 次尝试机会」 (tersisa N kali kesempatan mencoba) | Kata sandi salah, mendekati penguncian | Pikirkan matang-matang baru coba, atau langsung lewat «lupa kata sandi» |
| 「该账号未设置密码，请使用其他方式登录」 (akun ini belum mengatur kata sandi, silakan login dengan cara lain) | Akun pihak ketiga (Google/Watcha/Huawei) | Login dengan tombol pihak ketiga yang semula |
| 「该账号已注销」 (akun ini sudah dinonaktifkan) | Akun sudah deactivate | Perlu mendaftar ulang |

## Pengetahuan kecil soal login (sekalian untuk penelusuran)

Login mendukung masukan tiga-dalam-satu **nama pengguna / email / nomor ponsel** (ketiganya mana pun bisa
dipakai sebagai nama akun).
Lupa kata sandi: halaman login → «lupa kata sandi» → masukkan email pendaftaran, terima kode verifikasi 6 digit
→ atur ulang.
