# Rincian Proses Ndhaftar — powpow-register

Dienggo nalika golek masalah. Kabeh aturan saka kode sumber platform (validasi konsisten frontend/backend Next.js), dicathet sumbere.
Yen platform update, njupuk prilaku nyata online minangka patokan.

## Lawang Mlebu

- Kaca ndaftar: https://global.powpow.online/register
- Kaca login: https://global.powpow.online/login
- Kaca langganan: https://global.powpow.online/subscription
- Yen mlebu saka link share sing ngemot `?next=...`, sawise ndaftar+bayar rampung otomatis bali menyang kaca asline.

## Kolom Formulir lan Aturan

| Kolom | Wajib | Aturan | Sumber Kode |
|---|---|---|---|
| Foto profil | Opsional | gambar ≤5MB, ora ndhukung SVG; server kompres otomatis (>100KB dikompres dadi 400×400 / kualitas 90) | `src/app/api/auth/register/route.ts` |
| Jeneng panganggo | Wajib | 2~50 karakter, sawise trim disimpen **huruf cilik** (Tom lan tom dianggep jeneng panganggo padha, sisih ndaftar lan login padha-padha ora mbedakake gedhe/cilik) | Padha (zod schema) |
| Tembung sandi | Wajib | 8~100 karakter, kudu ngemot huruf gedhe, huruf cilik, angka | Padha |
| Konfirmasi tembung sandi | Wajib | kudu padha karo tembung sandi (mung cek frontend) | `src/app/(public)/register/page.tsx` |
| Jeneng panggilan | Opsional | ≤100 karakter; yen kosong default njupuk jeneng panganggo | register route |
| Email | **Wajib** | format email valid, ≤255 karakter; siji email mung bisa ndhaptar siji akun | register route |
| Kode verifikasi email | **Wajib** | 6 angka; **berlaku 10 menit**; sawise sukses diverifikasi langsung hangus; kirim maneh bakal menehi tandha kode lawas wis digunakake | `src/lib/email-verification.ts` |
| Nomer HP | Opsional | nomer HP China daratan diwiwiti `1[3-9]` total 11 digit; siji nomer mung bisa diiket siji akun | register route |

Kaca uga nyedhiyakake telung tombol login pihak katelu: **Google, Watcha, akun Huawei** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Akun pihak katelu ora duwe tembung sandi lokal, mengko login nganggo tembung sandi bakal oleh
"该账号未设置密码，请使用其他方式登录" (akun iki durung nyetel tembung sandi, mangga gunakake cara liya kanggo login).

## Parameter Rate Limit lan Anti-Bruteforce

| Prilaku | Watesan | Sumber |
|---|---|---|
| Kirim ndhaptar | **3 kali/menit/IP**, ngluwihi dadi 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Kirim kode verifikasi | IP padha 1 kali/menit **lan** email padha 1 kali/menit, ngluwihi dadi 429; tombol frontend countdown 60 detik | `src/app/api/auth/register/send-code/route.ts` |
| Cek kode verifikasi | saben email ing 10 menit maksimal coba **5 kali**, tekan watesan sanajan kode bener tetep ditolak, kudu kirim maneh | `src/lib/email-verification.ts` |
| Kirim kode lali sandi | 1 kali/menit/IP | `src/app/api/auth/forgot-password/route.ts` |
| Login | 5 kali/menit/IP; akun padha gagal berturut-turut **5 kali dikunci 30 menit** (423), sajrone iku ana notifikasi sisa kesempatan sing suda | `src/app/api/auth/login/route.ts`、`rate-limit.ts` |

**Prilaku nglindhungi privasi**: nalika kirim kode verifikasi / lali tembung sandi, ora preduli email wis kadaptar utawa ora ana, API tansah mbalekake
teks sukses sing padha, ora mbocorake email wis kadaptar utawa durung.

## Owah-owahan Status Sawise Ndhaptar Sukses

1. Pangguna disimpen kanthi `accountStatus: 'pending'`, wiwitane **3 lencana** (register route).
2. Server bebarengan nandur rong cookie HttpOnly: JWT (bisa langsung ngakses `/subscription`) lan
   pendingUserToken (kredensial identitas proses langganan).
3. Kaca ndhaptar ndeteksi `pending_payment` → mlumpat `/subscription` (nyimpen parameter bali `next`).
4. Bayar rampung → `accountStatus` dadi `active` (PayPal liwat Webhook otomatis aktif; WeChat scan QR
   konfirmasi manual; Huawei IAP liwat `activate-huawei`). Rincian deleng `payment-and-activation.md`.

Pangguna sing durung aktif (pending) nelpon API inti (feed, peta, omongan manungsa digital, check-in, lsp.) kabeh 403;
kajaba link pos sing di-share (tetep bisa diakses umum).

## Tabel Golek Masalah sing Kerep

| Kahanan (teks kesalahan asli basa Mandarin) | Sebab | Kepriye Ngatasi |
|---|---|---|
| 「用户名已存在」 (Jeneng panganggo wis ana) | jeneng panganggo wis digunakake (ora mbedakake gedhe/cilik) | ganti jeneng panganggo liyane |
| 「邮箱已被使用」 (Email wis digunakake) | email wis tau kadaptar | ganti email; utawa liwat login + "lali tembung sandi" kanggo mbalekake akun lawas |
| 「邮箱验证码错误或已过期」 (Kode verifikasi email salah utawa wis kadaluwarsa) | kode salah ketik / ngluwihi 10 menit / coba salah ngluwihi 5 kali ditolak | klik "Kirim maneh", gunakake kode saka **email paling anyar** |
| Kode verifikasi ora teka | kena rate limit 60 detik; utawa mlebu folder spam/iklan | enteni countdown rampung banjur kirim maneh; bukak folder spam |
| 「手机号已被使用」 (Nomer HP wis digunakake) | nomer HP wis diiket akun liyane | busak nomer HP (opsional) utawa ganti nomer |
| 「注册请求过于频繁」/ 429 (Panjalukan ndaftar kerep banget) | tekan watesan ndhaptar 3 kali/menit/IP | enteni sawetara menit banjur coba maneh |
| 409「用户名或邮箱已被注册」 (Jeneng panganggo utawa email wis kadaptar) | tabrakan jeneng karo wong liya pas kirim (backup anti-konflik) | ganti jeneng panganggo utawa email banjur coba maneh |
| 「图片大小不能超过5MB」/「不支持 SVG」 (Ukuran gambar ora kena ngluwihi 5MB / Ora ndhukung SVG) | foto profil ora cocog | ganti gambar utawa lewati foto profil |
| Ndhaptar sukses nanging login 403「请完成订阅以激活账户」 (Mangga rampungake langganan kanggo ngaktifake akun) | akun isih pending | sawise login tindakake pitunjuk ing kaca menyang `/subscription` rampungake langganan |
| Login 423「账户已锁定」 (Akun wis dikunci) | salah tembung sandi 5 kali berturut-turut | enteni 30 menit |
| Login 401「还剩 N 次尝试机会」 (Isih ana N kesempatan nyoba) | salah tembung sandi, meh dikunci | pikiren dhisik banjur coba, utawa langsung "lali tembung sandi" |
| 「该账号未设置密码，请使用其他方式登录」 (Akun iki durung nyetel tembung sandi, mangga gunakake cara liya kanggo login) | akun pihak katelu (Google/Watcha/Huawei) | gunakake tombol pihak katelu sing mau kanggo login |
| 「该账号已注销」 (Akun iki wis dipateni) | akun wis di-deactivate | kudu ndhaptar anyar |

## Kawruh Cilik bab Login (sekaligus kanggo golek masalah)

Login ndhukung input telu-dadi-siji **jeneng panganggo / email / nomer HP** (sembarang siji bisa digunakake minangka jeneng akun).
Lali tembung sandi: kaca login → "lali tembung sandi" → lebokake email sing kadaptar nampa kode verifikasi 6 digit → setel maneh.