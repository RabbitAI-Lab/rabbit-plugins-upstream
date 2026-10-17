# Alur agen-ditindakake lan kontrak skrip — powpow-register

Detail eksekusi saben langkah ing SKILL.md. Kabeh printah yaiku `node scripts/powpow-register.mjs <sub-printah> [paramèter]`,
skrip **tanpa dependensi**, butuh **Node >= 18**, kabeh panjalukan mung menyang `https://global.powpow.online`.

## Desain keamanan (ngapa didesain kaya mangkene)

| Desain | Alesan |
|---|---|
| Tembung sandhi mung dilebokake liwat variabel lingkungan `POWPOW_REGISTER_PASSWORD` | paramèter printah proses katon dening proses liya ing mesin sing padha (lumahing bocore argv), variabel lingkungan dibaca ing skrip banjur langsung dienggo |
| Tembung sandhi **aja tau ditulis ing berkas status**, aja tau katon ing log | berkas status bisa tetep ana ing disk; mode nggawe mung nampilake sepisan supaya panganggo nyimpen |
| Berkas status disimpen ing direktori sementara sistem (`os.tmpdir()/powpow-register-state.json`, 0600) | mung ngemot limang kolom: email / username / nickname / token / outTradeNo, `cleanup` mbusak sepisan klik |
| JWT sing ditampa agen diowahi dadi cookie browser liwat endpoint resmi `me?token=` | jembatan resmi platform sing didesain kanggo Harmony WebView; verifikasi mung mriksa tandha + masa berlaku, ora ndheleng fingerprint piranti, bisa dienggo browser panganggo |
| Bayaran mung nindakake create-order / query / mbukak kasir | tumindak mbayar lan bukti bayaran tansah ana antarane panganggo lan kasir resmi Alipay, agen ora nyekel |

## Referensi printah

| Printah | Paramèter kunci | Fungsi / kapan |
|---|---|---|
| `status` | —— | Ndeleng kemajuan alur (maca berkas status); sawise obrolan mandheg, jalanke iki dhisik |
| `gen-password` | —— | Nggawe tembung sandhi kuwat 24 karakter (campuran huruf gedhe-cilik + angka), ditampilake ing stdout **mung sepisan iki** |
| `prepare-suggest` | `--username --nickname --email` | Nyathet info sing wis dikonfirmasi menyang berkas status (sawise iku register ora perlu dikirim maneh) |
| `send-code` | `--email` | Micu platform ngirim kode verifikasi 6 digit (sah 10 menit, cooldown 60 detik) |
| `register` | `--code` (wajib); `--username --nickname --avatar --phone` (opsional, yen berkas status wis ana, ora perlu dikirim) | Nggawe akun pending; tembung sandhi liwat variabel lingkungan `POWPOW_REGISTER_PASSWORD`; sawise sukses JWT otomatis disimpen ing berkas status |
| `login-link` | `--target pending` utawa `--target home` | Nggawe tautan mlebu sepisan klik (desain tautan dobel, ndeleng ing ngisor) |
| `create-order` | `--package monthly\|quarterly\|yearly` (gawan Alipay)<br>`--provider alipay\|paypal` | Nggawe pesanan bayaran; Alipay mbalekake path berkas kaca bayaran + outTradeNo; PayPal mbalekake path berkas kaca ijin + subscriptionId (otomatis dicathet ing berkas status) |
| `query` | —— | Ndeleng status pesanan/langganan. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; polling 10–15 detik |
| `refresh-login` | tembung sandhi liwat variabel lingkungan | Mlebu maneh kanggo njupuk **JWT anyar** (klaim langganan owah saka NONE dadi ACTIVE), wajib jalanke sawise bayaran tekan |
| `whoami` | —— | Nganggo token ing berkas status ndeleng status akun lan langganan (verifikasi aktivasi wis efektif) |
| `cleanup` | —— | Mbusak berkas status (wajib jalanke ing penutup) |

**Ngirimake liwat variabel lingkungan** (tembung sandhi ora tau mlebu printah):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<tembung sandhi>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<tembung sandhi>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<tembung sandhi> && node scripts/powpow-register.mjs register --code 123456
```

## Mekanisme tautan dobel (desain inti)

Status mlebu platform yaiku cookie HttpOnly, agen ora bisa langsung nandur cookie menyang browser; jembatane yaiku endpoint resmi
`/api/auth/me?token=<JWT>&redirect=<path-njeron-situs>`: verifikasi tandha → panganggo pending otomatis digaweake
session → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 dina) → validasi
redirect (mung diwiwiti siji garis miring, larang `//` lan backslash, sawise diurai kudu same-origin) → 307 pangalihan sauntara menyang kaca target.

- **Tautan 1 (diwenehake langsung sawise registrasi sukses)**: `--target pending` → mlebu `/subscription`.
  Browser panganggo mlebu status "mlebu setengah": kaca langganan, kaca bali Alipay bisa dideleng lan bisa dioperasikake; kaca isi isih ditulak menyang kaca langganan dening tembok bayaran (telung lapisan protèksi: priksa gerbang klaim JWT → priksa maneh DB → priksa API inti, iku tumindak normal).
- **Tautan 2 (diwenehake sawise paid dikonfirmasi)**: dhisik `refresh-login` njupuk JWT anyar (bayaran mung nganyari DB, ora ngowahi klaim JWT sing wis ditandatangani, yen ora diganti bakal katon "wis mbayar nanging dudu anggota"), banjur `--target home` → mlebu kaca ngarep,
  status anggota lengkap.

## Urutan lengkap (jalur normal)

```
1.  status                          # self-test lingkungan
2.  (Langkah 2 konfirmasi info ing obrolan, tembung sandhi milih siji; mode nggawe: gen-password → nyurup panganggo gelis simpen)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → panganggo menyang email ndeleng kode (siji-sijine bagean metu obrolan①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → tautan 1 dikirim marang panganggo
7.  (panganggo milih cara bayar)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <berkas kaca bayaran>              # Windows; macOS nganggo open, Linux nganggo xdg-open
    # → panganggo ngrampungake bayaran/ijin ing kasir Alipay/PayPal (bagean metu obrolan②)
9.  query (saben 10–15 detik) nganti paid / ACTIVE
10. refresh-login                   # njupuk JWT anyar kanthi klaim ACTIVE
11. login-link --target home        # → tautan 2 dikirim marang panganggo
12. whoami                          # konfirmasi subscriptionStatus: ACTIVE (opsional)
13. cleanup                         # mbusak berkas status
```

## Pemetaan printah → API platform

| Printah skrip | API platform |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, unggah avatar langsung) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (tautane dhewe, aktif nalika browser diklik) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Sumber aturan: aturan kolom lan watesan laju registrasi ndeleng `registration-flow.md`; paket lan rantai aktivasi ndeleng
`payment-and-activation.md` (loro-lorone ndhawuhake berkas kode sumber platform).

## Penanganan kesalahan tingkat skrip

| Fenomena | Penanganan |
|---|---|
| `Node 版本过低` (versi Node kedhapur) | Bali menyang mode pandhuan murni, aja ngoyo nyoba |
| Kesalahan jaringan / timeout | Coba maneh sepisan; isih gagal nyurup panganggo mriksa jaringan banjur nerusake (berkas status isih ana, jalanke `status` saka wiwitan kanggo pulih) |
| register mbalikake kesalahan bisnis (用户名已存在 lan liya-liyane) | Nangani miturut tabel Langkah 5 SKILL.md, **kode verifikasi ora perlu dikirim maneh** (isih sah ing 10 menit) |
| register mbalikake 「邮箱验证码错误或已过期」 (kode verifikasi email salah utawa kedaluwarsa) | Ketemu wektu → kirim maneh `send-code` |
| Sawise `create-order` panganggo nutup kaca bayaran | Langsung jalanke maneh `create-order` (pesanan lawas otomatis ditutup sawise 2 jam; langganan PayPal PENDING kadaluwarsa sawise 1 jam) |
| `create-order --provider paypal` mbalekake 409 | Ana langganan PayPal sing durung rampung; enteni 1 jam nganti kadaluwarsa, utawa rampungake ijin lawas ing browser |
| `query` tansah pending / PENDING | Panganggo mbokmenawa durung mbayar; takona sepisan. Yen pancen wis mbayar → tindakake tabel diagnostik payment-and-activation.md |
| `refresh-login` 403 `pending_payment` | Bayaran/ijin durung tekan, bali menyang langkah 9 nerusake polling |
| Berkas status ilang (kecele dibusak / ganti mesin) | `whoami`/`refresh-login` ora bisa dienggo; nyurup panganggo ing browser sing tau mbukak tautan 1 langsung nganyari kaca langganan kanggo konfirmasi status, utawa mlebu maneh (mode web) |

## Mode fallback (pandhuan murni)

Kahanan ing ngisor iki, langsung bali menyang mode pandhuan murni gaya v1, aja rep-rep skrip maneh:

- Ora ana Node >= 18 utawa skrip gagal ping pindho berturut-turut kanthi jinis sing padha;
- Panganggo jelas ngomong "aku dhewe sing ngoperasikake ing web";
- Kebijakan perusahaan/perangkat mbatesi skrip nyambung internet.

Sawise fallback: wenehake kaca registrasi https://global.powpow.online/register lan kaca langganan
https://global.powpow.online/subscription , ngetutake aturan `registration-flow.md` mèlu ngatasi masalah, swara
ora owah, saben giliran isih ditutup karo bagean "langkah sabanjure".
