# Aktivasi Langganan dan Pembayaran — powpow-register

## Kesimpulan (jawaban dulu)

**Metode pembayaran yang ada bisa langsung dipakai ulang, skill asisten pendaftaran nol pengembangan pembayaran.**

Alasannya:

1. Endpoint pendaftaran (`src/app/api/auth/register/route.ts`) saat membuat akun pending sudah menerbitkan
   JWT cookie + pendingUserToken HttpOnly cookie, pengguna mendarat di `/subscription` sudah dalam
   status login — tiga kanal pembayaran semuanya menggantung di halaman langganan ini, yang diaktifkan adalah akun pending yang sama.
2. Endpoint login untuk akun pending mengembalikan 403 + `redirectTo: '/subscription'`, juga menanam
   cookie yang sama — pengguna kapan pun melengkapi pembayaran akan dipandu kembali ke halaman yang sama.
3. Karena itu batas tanggung jawab skill panduan pendaftaran adalah "mengarahkan pengguna ke /subscription"; tidak perlu
   endpoint pembayaran baru, tidak perlu model pesanan baru, tidak perlu perubahan backend apa pun.

Perlu juga dicatat: tahap pembayaran (tombol PayPal JS SDK, WeChat scan QR konfirmasi manual, Huawei IAP asli)
**menentukan bahwa ia tidak bisa dan tidak seharusnya dibayarkan oleh skill command-line/chat**. Jangan coba pakai skrip memanggil endpoint
pembayaran untuk membayar atas nama pengguna, jangan juga meminta bukti pembayaran pengguna.

## Tiga Kanal di Halaman Langganan

Halaman langganan `src/app/(public)/subscription/page.tsx` menampilkan otomatis sesuai lingkungan:

| Kanal | Lingkungan | Mekanisme | Cara Aktivasi |
|---|---|---|---|
| Langganan PayPal | Web (bukan HarmonyOS) | `/api/subscription/create` membuat langganan PayPal → lompat ke otorisasi PayPal; perpanjang otomatis tiap bulan, bisa dibatalkan kapan saja (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) otomatis set `accountStatus` jadi active |
| Langganan scan QR WeChat | Web (bukan HarmonyOS) | blok "Langganan scan QR WeChat" di bawah halaman: scan QR transfer, **dibuka setelah konfirmasi manual** (`WechatQrPaymentSection`) | konfirmasi manual, dana masuk bisa telat; pengguna bayar jangan buru-buru vonis gagal |
| Pembelian dalam aplikasi Huawei (IAP) | Dalam App HarmonyOS | di WebView HarmonyOS PayPal/WeChat tidak bisa dipakai, halaman beralih ke `NativeBridge.purchaseSubscription()` asli | `/api/subscription/activate-huawei` verifikasi pesanan Huawei lalu aktifkan |

Paket dan harga dibaca dinamis dari `/api/subscription/plans` (paket PayPal); teks tetap di halaman:
Auto-renews. Cancel anytime.

## Status dan Perpindahan Halaman

- Pembayaran sukses → `/subscription/success` (callback PayPal membawa `subscriptionId`) → akun
  active → otomatis kembali ke halaman asal yang ditentukan `next` (tidak ada maka beranda).
- Pengguna yang sudah berlangganan mengunjungi lagi halaman langganan → tampil "You're All Set!", 3 detik kemudian otomatis balik beranda.
- Pembayaran gagal/batal → `/subscription/cancel`, bisa mulai lagi.

## Penelusuran

| Gejala | Penanganan |
|---|---|
| Sudah bayar masih 403 | PayPal: Webhook kadang telat, login ulang untuk refresh status (saat login akan mengecek ulang status terbaru dari DB); WeChat: konfirmasi manual belum selesai, tunggu sebentar; Huawei: cek apakah halaman sukses pembayaran dalam App muncul |
| Halaman langganan menampilkan "No subscription plans available" | `/api/subscription/plans` tidak ada paket PayPal yang tersedia, ini masalah konfigurasi sisi platform, suruh pengguna coba lagi nanti |
| Sudah bayar WeChat tapi belum dibuka | konfirmasi manual itu asinkron, beberapa jam belum dibuka baru hubungi dukungan platform (dongtao@outlook.com) |

## Catatan: Alipay

Di kode ada satu set pembayaran web Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`,
model beli putus sekali bayar member biasa ¥9.90 / member premium ¥99, saat sandbox belum dikonfigurasi kunci otomatis
turun menjadi pembayaran simulasi), **tapi belum dihubungkan ke UI halaman langganan**, termasuk kode idle/cadangan. Kalau suatu hari
ingin mengaktifkan Alipay di halaman langganan, tinggal sambungkan set kode yang sudah ada ini — ini tidak terkait dengan skill ini,
hanya untuk referensi keputusan sisi platform.