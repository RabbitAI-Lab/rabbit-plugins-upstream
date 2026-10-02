# Detail Alur Pendaftaran — powpow-register

Dipakai untuk menelusuri masalah. Semua aturan berasal dari kode sumber platform (validasi konsisten frontend/backend Next.js), dicantumkan sumbernya.
Saat platform diperbarui, ikuti perilaku aktual online.

## Pintu Masuk

- Halaman pendaftaran: https://global.powpow.online/register
- Halaman login: https://global.powpow.online/login
- Halaman langganan: https://global.powpow.online/subscription
- Jika masuk dari link share yang mengandung `?next=...`, setelah daftar+bayar selesai otomatis kembali ke halaman awal.

## Field Formulir dan Aturan

| Field | Wajib | Aturan | Sumber Kode |
|---|---|---|---|
| Foto profil | Opsional | gambar ≤5MB, tidak mendukung SVG; server kompres otomatis (>100KB dikompres ke 400×400 / kualitas 90) | `src/app/api/auth/register/route.ts` |
| Username | Wajib | 2~50 karakter, setelah trim disimpan **huruf kecil** (Tom dan tom dianggap username sama, sisi daftar dan login sama-sama tidak membedakan besar/kecil) | Sama (zod schema) |
| Kata sandi | Wajib | 8~100 karakter, wajib memuat huruf besar, huruf kecil, angka | Sama |
| Konfirmasi kata sandi | Wajib | harus sama dengan kata sandi (hanya cek frontend) | `src/app/(public)/register/page.tsx` |
| Nama panggilan | Opsional | ≤100 karakter; kosong default pakai username | register route |
| Email | **Wajib** | format email valid, ≤255 karakter; satu email hanya bisa daftar satu akun | register route |
| Kode verifikasi email | **Wajib** | 6 digit; **berlaku 10 menit**; setelah berhasil diverifikasi langsung hangus; kirim ulang akan menandai kode lama sudah terpakai | `src/lib/email-verification.ts` |
| Nomor HP | Opsional | nomor HP China daratan diawali `1[3-9]` total 11 digit; satu nomor hanya bisa diikat satu akun | register route |

Halaman juga menyediakan tiga tombol login pihak ketiga: **Google, Watcha, akun Huawei** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Akun pihak ketiga tidak punya kata sandi lokal, ke depannya login pakai kata sandi akan mendapat
"该账号未设置密码，请使用其他方式登录" (akun ini belum mengatur kata sandi, silakan gunakan cara lain untuk login).

## Parameter Rate Limit dan Anti-Bruteforce

| Perilaku | Batasan | Sumber |
|---|---|---|
| Kirim pendaftaran | **3 kali/menit/IP**, lebih jadi 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Kirim kode verifikasi | IP sama 1 kali/menit **dan** email sama 1 kali/menit, lebih jadi 429; tombol frontend hitung mundur 60 detik | `src/app/api/auth/register/send-code/route.ts` |
| Cek kode verifikasi | per email dalam 10 menit maksimal coba **5 kali**, capai batas meski kode benar tetap ditolak, harus kirim ulang | `src/lib/email-verification.ts` |
| Kirim kode lupa sandi | 1 kali/menit/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 kali/menit/IP; akun sama gagal beruntun **5 kali terkunci 30 menit** (423), selama itu muncul notifikasi sisa kesempatan berkurang | `src/app/api/auth/login/route.ts`、`rate-limit.ts` |

**Perilaku privasi**: saat kirim kode verifikasi / lupa kata sandi, apakah email sudah terdaftar atau tidak ada, API selalu mengembalikan
teks sukses yang sama, tidak membocorkan email sudah terdaftar atau belum.

## Perubahan Status Setelah Pendaftaran Sukses

1. Pengguna disimpan dengan `accountStatus: 'pending'`, awal **3 lencana** (register route).
2. Server sekaligus menanam dua cookie HttpOnly: JWT (bisa akses langsung `/subscription`) dan
   pendingUserToken (kredensial identitas proses langganan).
3. Halaman pendaftaran mendeteksi `pending_payment` → lompat `/subscription` (menyimpan parameter kembali `next`).
4. Pembayaran selesai → `accountStatus` berubah `active` (PayPal lewat Webhook otomatis aktif; WeChat scan QR
   konfirmasi manual; Huawei IAP lewat `activate-huawei`). Detail lihat `payment-and-activation.md`.

Pengguna yang belum aktif (pending) memanggil API inti (feed, peta, ngobrol manusia digital, check-in, dll.) semuanya 403;
kecuali link postingan yang dibagikan (tetap terbuka publik).

## Tabel Penelusuran Error Umum

| Gejala (teks error asli bahasa Mandarin) | Penyebab | Cara Atasi |
|---|---|---|
| 「用户名已存在」 (Username sudah ada) | username sudah dipakai (tidak bedakan besar/kecil) | ganti username lain |
| 「邮箱已被使用」 (Email sudah digunakan) | email sudah pernah didaftarkan | ganti email; atau lewat login + "lupa kata sandi" untuk memulihkan akun lama |
| 「邮箱验证码错误或已过期」 (Kode verifikasi email salah atau kedaluwarsa) | kode salah ketik / lewat 10 menit / coba salah lebih 5 kali ditolak | klik "Kirim ulang", pakai kode dari **email terbaru** |
| Kode verifikasi tidak kunjung datang | kena rate limit 60 detik; atau masuk ke spam/iklan | tunggu hitung mundur selesai lalu kirim ulang; buka folder spam |
| 「手机号已被使用」 (Nomor HP sudah digunakan) | nomor HP sudah diikat akun lain | hapus nomor HP (opsional) atau ganti nomor |
| 「注册请求过于频繁」/ 429 (Permintaan pendaftaran terlalu sering) | menyentuh batas daftar 3 kali/menit/IP | tunggu beberapa menit lalu coba lagi |
| 409「用户名或邮箱已被注册」 (Username atau email sudah terdaftar) | bentrok nama dengan orang lain tepat saat kirim (backup anti-konflik) | ganti username atau email lalu coba lagi |
| 「图片大小不能超过5MB」/「不支持 SVG」 (Ukuran gambar tidak boleh melebihi 5MB / Tidak mendukung SVG) | foto profil tidak sesuai | ganti gambar atau lewati foto profil |
| Daftar sukses tapi login 403「请完成订阅以激活账户」 (Silakan selesaikan langganan untuk mengaktifkan akun) | akun masih pending | setelah login ikuti petunjuk di halaman ke `/subscription` selesaikan langganan |
| Login 423「账户已锁定」 (Akun terkunci) | salah kata sandi 5 kali beruntun | tunggu 30 menit |
| Login 401「还剩 N 次尝试机会」 (Sisa N kesempatan mencoba) | salah kata sandi, hampir terkunci | pikirkan dulu baru coba, atau langsung "lupa kata sandi" |
| 「该账号未设置密码，请使用其他方式登录」 (Akun ini belum mengatur kata sandi, silakan gunakan cara lain untuk login) | akun pihak ketiga (Google/Watcha/Huawei) | pakai tombol pihak ketiga semula untuk login |
| 「该账号已注销」 (Akun ini sudah dinonaktifkan) | akun sudah di-deactivate | perlu daftar baru |

## Kecil-kecilan soal Login (sekalian untuk telusur)

Login mendukung input**username / email / nomor HP** tiga-dalam-satu (semuanya bisa dipakai sebagai nama akun).
Lupa kata sandi: halaman login → "lupa kata sandi" → masukkan email terdaftar terima kode verifikasi 6 digit → atur ulang.