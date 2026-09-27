# Aktivasi Langganan lan Pembayaran — powpow-register

## Kesimpulan (jawaban dhisik)

**Cara bayar sing wis ana bisa langsung digunakake maneh, skill asisten ndhaptar nol pangembangan bayar.**

Sebab:

1. Endpoint ndaftar (`src/app/api/auth/register/route.ts`) nalika nggawe akun pending wis nerbitake
   JWT cookie + pendingUserToken HttpOnly cookie, pangguna sing ndharat ing `/subscription` wis ana ing
   status login — telung jalur bayar kabeh gantung ing kaca langganan iki, sing diaktifake yaiku akun pending sing padha.
2. Endpoint login kanggo akun pending mbalekake 403 + `redirectTo: '/subscription'`, uga nandur
   cookie sing padha — pangguna kapan wae nglengkapi bayar bakal dituntun bali menyang kaca sing padha.
3. Mula wates tanggung jawab skill panduan ndhaptar yaiku "ngarahake pangguna menyang /subscription"; ora perlu endpoint
   bayar anyar, ora perlu model pesenan anyar, ora perlu owah-owahan backend apa wae.

Bebarengan kudu digatekake: tahap bayar (tombol PayPal JS SDK, WeChat scan QR konfirmasi manual, Huawei IAP asli)
**nemtokake manawa iku ora bisa lan ora kena dibayarake dening skill command-line/chat**. Aja nyoba nganggo script nelpon endpoint
bayar kanggo mbayar atas jenenge pangguna, aja uga njaluk bukti bayar pangguna.

## Telung Jalur ing Kaca Langganan

Kaca langganan `src/app/(public)/subscription/page.tsx` otomatis nampilake miturut lingkungan:

| Jalur | Lingkungan | Mekanisme | Cara Aktivasi |
|---|---|---|---|
| Langganan PayPal | Web (dudu HarmonyOS) | `/api/subscription/create` nggawe langganan PayPal → mlumpat menyang otorisasi PayPal; auto-renew saben wulan, bisa dibatalake kapan wae (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) otomatis nyetel `accountStatus` dadi active |
| WeChat scan QR langganan | Web (dudu HarmonyOS) | blok "WeChat scan QR langganan" ing ngisor kaca: scan QR transfer, **dibukak sawise konfirmasi manual** (`WechatQrPaymentSection`) | konfirmasi manual, dhuwite uwal bisa telat; pangguna wis bayar aja grusa-grusu vonis gagal |
| Tuku ing aplikasi Huawei (IAP) | Ing App HarmonyOS | ing WebView HarmonyOS PayPal/WeChat ora bisa digunakake, kaca ngalih menyang `NativeBridge.purchaseSubscription()` asli | `/api/subscription/activate-huawei` verifikasi pesenan Huawei banjur aktifake |

Paket lan rega diwaca dinamis saka `/api/subscription/plans` (paket PayPal); teks tetep ing kaca:
Auto-renews. Cancel anytime.

## Status lan Owah-owahan Kaca

- Bayar sukses → `/subscription/success` (callback PayPal nggawa `subscriptionId`) → akun
  active → otomatis bali menyang kaca asli sing ditemtokake `next` (ora ana yaiku kaca ngarep).
- Pangguna sing wis langganan mampir maneh ing kaca langganan → muncul "You're All Set!", 3 detik mengko otomatis bali kaca ngarep.
- Bayar gagal/batal → `/subscription/cancel`, bisa miwiti maneh.

## Golek Masalah

| Kahanan | Penanganan |
|---|---|
| Wis bayar isih 403 | PayPal: Webhook kadhang telat, login maneh kanggo refresh status (nalika login bakal mriksa maneh status paling anyar saka DB); WeChat: konfirmasi manual durung rampung, enteni sedhela; Huawei: cek apa kaca sukses bayar ing App muncul |
| Kaca langganan nampilake "No subscription plans available" | `/api/subscription/plans` ora ana paket PayPal sing kasedhiya, iki masalah konfigurasi sisih platform, koncene pangguna coba maneh mengko |
| Wis bayar WeChat durung dibukak | konfirmasi manual iku asinkron, sawetara jam durung dibukak anyar hubungi dhukungan platform (dongtao@outlook.com) |

## Cathetan: Alipay

Ing kode ana siji set bayar web Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`,
model tuku putus sekali bayar anggota biasa ¥9.90 / anggota premium ¥99, nalika sandbox durung dikonfigurasi kunci otomatis
mudhun dadi bayar simulasi), **nanging durung disambungake menyang UI kaca langganan**, iku kode nganggur/cadangan. Yen mengko
pengin ngaktifake Alipay ing kaca langganan, sambungake set kode sing wis ana iki wae — iki ora ana gayutane karo skill iki,
mung kanggo referensi keputusan sisih platform.