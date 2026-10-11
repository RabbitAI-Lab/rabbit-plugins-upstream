# Aktivasi langganan lan bayaran — powpow-register

## Kesimpulan (jawaban dhisik)

**Saluran Alipay wis urip (wiwit 2026-10-07), dadi cara bayaran utama skill iki, agen bisa njalukake pesanan lan ngawasi tekan dhuwit.**
Panganggo luar negeri/tanpa Alipay bali menyang PayPal; pindai kode WeChat (konfirmasi manual) lan Huawei IAP isih ana, nanging ora ditangani skill.

Bates tanggung jawab ing bagean bayaran: agen bisa **nggawe pesanan, mbukak kasir, ngawasi tekan dhuwit**; **aja tau** nyentuh akun Alipay
panganggo/bukti bayaran, aja tau janji "mbayarke". Tumindak mbayar tansah ditindakake panganggo dhewe ing kasir resmi Alipay.

## Saluran Alipay (vibepay, utama)

Sistem tuku langsung: mbayar sepisan ngaktifake durasi sing cocog, **ora langganan otomatis**. Paket ditetepake ing
`src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Jeneng | Rego | Durasi |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Anggota wulan | ¥6.99 | 30 dina |
| `quarterly` | alipay-quarterly | Anggota kuartal | ¥19.99 | 90 dina |
| `yearly` | alipay-yearly | Anggota taunan | ¥69.99 | 365 dina |

### Kontrak API (skrip skill wis mbungkus, agen ora ngrakit panjalukan langsung)

| API | Metode | Katrangan |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Butuh `Authorization: Bearer <JWT>` (panganggo pending cukup). body `{package}` → bali `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` yaiku kaca formulir sing otomatis dikirim menyang gateway Alipay |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Uga verifikasi Bearer. Bali `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (callback server Alipay) | Verifikasi lima unsur tandha (tandha, app_id, jumlah cocog, TRADE_SUCCESS/TRADE_FINISHED, keunikan pedagang) → nganyari pesanan **idempotent** + nggawe langganan + ngaktifake akun. Skill ora tau nyentuh API iki |
| `/payment/alipay/return` | Kaca bali browser | Path umum, sawise mbayar nampilake konfirmasi 「支付成功」 (bayaran sukses), kaca polling status nyata backend |

- Pesanan durung dibayar **otomatis ditutup sawise 2 jam**; panganggo mandheg ing tengah dalan → langsung jalanke maneh `create-order`, pesanan lawas ora usah diatur-atur.
- Skrip nulis `paymentHtml` menyang berkas HTML sementara, agen mbukak nganggo printah sistem kanggo mlebu kasir Alipay
  (pindai kode utawa mlebu ing Alipay kanggo mbayar).

### Rantai aktivasi (otomatis, tanpa manungsa)

notify verifikasi tandha lulus → `paymentOrders` ditandhani wis dibayar → `user_subscriptions` digawe/diterusake
(`planId`, `currentPeriodEnd` diwilang miturut durationDays, penyambungan durasi diterusake saka tanggal kedaluwarsa lawas) →
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → kaca bali polling nganti paid nampilake sukses.

### Sawise mbayar kudu ngganti status mlebu anyar (penting)

JWT nggawa klaim langganan (akun pending yaiku `NONE`). **Bayaran tekan mung nganyari database, ora ngowahi JWT sing wis ditandatangani** — klaim token lawas isih NONE, yen langsung dienggo nggawe tautan mlebu bakal katon "ora duwe langganan".
Mulane skill sawise konfirmasi `paid` dhisik jalanke `refresh-login` (mlebu maneh njupuk JWT anyar, klaim dadi ACTIVE),
banjur nggawe tautan 2. Iki tumindak desain, dudu pambeneran bug.

## Sekawan saluran ing kaca langganan

Kaca langganan `src/app/(public)/subscription/page.tsx` nampilake miturut lingkungan eksekusi:

| Saluran | Lingkungan | Mekanisme | Cara aktivasi |
|---|---|---|---|
| **Alipay (utama)** | Web | `AlipayPaymentSection` liwat API vibepay (tabel ing ndhuwur) | notify aktivasi otomatis sisih server, tingkat detik |
| Langganan PayPal | Web (ora Harmony) | `/api/subscription/create` → mlumpat menyang otorisasi PayPal; langganan wulanan otomatis bisa dibatalake kapan wae (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) otomatis ndadekake active |
| 「微信扫码订阅」 (langganan pindai kode WeChat) | Web (ora Harmony) | Ngisor kaca 「微信扫码订阅」: pindai kode ngirim dhuwit | **konfirmasi manual**, tekan dhuwit bisa telat; sawise mbayar aja buru-buru nghukumi gagal |
| Pembelian ing-aplikasi Huawei | Ing njero app Harmony | Native `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` verifikasi pesanan Huawei banjur ngaktifake |

Rencana lan rego PayPal diwaca dinamis saka `/api/subscription/plans`; teks tetep kaca: Auto-renews. Cancel anytime.

## Status lan pangalihan

- Alipay rampung mbayar → kaca bali nampilake sukses; PayPal sukses → `/subscription/success` → akun active →
  otomatis bali menyang kaca asal sing ditunjuk paramèter `next` (yen ora ana, kaca ngarep).
- Panganggo sing wis langganan ngakses kaca langganan maneh → nampilake "You're All Set!", 3 detik sawise iku otomatis bali kaca ngarep.
- Bayaran gagal/dibatalake (PayPal) → `/subscription/cancel`, bisa miwiti maneh.

## Diagnostik

| Fenomena | Penanganan |
|---|---|
| Alipay wis mbayar nanging `query` isih pending | notify arang banget telat; enteni 30 detik banjur takokake maneh. Isih ora bisa nyurup panganggo bali menyang browser ndeleng status kaca bali, isih ora bisa hubungi dukungan platform (dongtao@outlook.com), laporake `outTradeNo` |
| Alipay wis mbayar, mlebu tautan 2 isih diblokir | Kurang jalanke `refresh-login` (klaim JWT lawas durung nganyari) — dhisik `refresh-login` banjur `login-link` |
| Sawise mbayar isih 403 (PayPal) | Webhook sok telat, mlebu maneh kanggo nganyari status |
| WeChat wis mbayar nanging durung diaktifake | Konfirmasi manual iku asinkron, yen sawetara jam durung diaktifake banjur hubungi dukungan platform |
| Kaca langganan nampilake "No subscription plans available" | `/api/subscription/plans` ora duwe rencana PayPal sing kasedhiya, masalah konfigurasi sisih platform; panganggo daratan Cina mung ngalih menyang Alipay |

## Cathetan sejarah

Ing kode ana sawijining sistem **lawas** bayaran web Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`,
¥9.90/¥99 tuku langsung, yen kunci sandbox durung disetel mudhun dadi bayaran simulasi), ora tau disambungake menyang UI kaca langganan, ora ana gandheng cengenge karo vibepay. Skill ora tau nyentuh iku; `alipay-vibepay.ts` sing dadi saluran saiki.
