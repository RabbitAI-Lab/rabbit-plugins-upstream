---
name: powpow-register
description: Mbiyantu pangguna ndaftar akun PowPow (Gelembung) lan ngrampungake aktivasi langganan. Micu nalika pangguna ngucap "ndaftar Gelembung", "ndaftar akun powpow", "kepriye carane ndaftar Gelembung", "tulung ndaftarake akun powpow", "sign up powpow"; uga nangani masalah sajrone proses ndaftar (kode verifikasi ora teka, jeneng panganggo/email wis digunakake, format tembung sandi salah) lan masalah aktivasi sawise ndaftar (login kandha "akun durung aktif" / pending_payment, kepriye carane langganan/bayar). Skill panduan murni: pambuka produk (kalebu screenshot) → panduan ndaftar tahap demi tahap → golek masalah → aktivasi langganan. Ora kalebu ngirim pos/nggawe manungsa digital (iku urusane powpow-simple), ora kalebu pangembangan kode.
version: 1.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Pitulung Ndhaftar Gelembung)

Nggawa pangguna anyar saka "ora ngerti Gelembung kuwi apa" nganti "akun aktif, bisa digunakake normal".

**Versi 1.0.0** · 2026-09-23 (rincian proses ndaftar lan golek masalah deleng `references/registration-flow.md`; aktivasi langganan lan jalur bayar deleng `references/payment-and-activation.md`; daftar screenshot produk deleng `references/screenshots.md`)

## Lingkungan Mlaku

Skill iki **murni panduan**: ora ana script babar pisan, ora mbutuhake Node utawa dependensi liyane. Kabeh tumindak (ngisi
form, nampa kode verifikasi, bayar) ditindakake pangguna ing browser/App dhewe, tugas sampeyan mung ngenalake, nuduhake dalan, lan golek masalah.

## Trigger Conditions

- Niat ndaftar: "ndaftar Gelembung", "ndaftar siji akun powpow", "kepriye carane ndaftar Gelembung", "sign up powpow"
- Macet nalika ndaftar: "kode verifikasi ora teka-teka", "jeneng panganggo kandha wis ana", "tembung sandi ora tau lolos"
- Masalah sawise ndaftar: "login kandha akun durung aktif", "403 pending_payment", "gelembung kepriye carane bayar/langganan"

**Ora micu**: ngirim pos/nggawe manungsa digital (→ powpow-simple); pangembangan kode web (deleng skill pangembangan).
Pangguna sing pengin ndaftar lan ngirim pos bebarengan: rampungake skill iki dhisik, sawise akun aktif banjur pasrahake menyang powpow-simple.

## Pambuka Produk + Tampilake Screenshot (tahap siji, ora kena diluncati)

Umume pangguna durung nate ndeleng Gelembung. Bab pisanan dudu nerangake proses, nanging gawe dheweke **ndeleng** produk:

1. Ngenalake Gelembung nganggo ~120 tembung: fotone foto dadakan dadi cathetan lelungan, dicethak ing peta umum dadi siji
   "gelembung"; gelembung bakal basi dening wektu, yen ana sing like bisa urip maneh; ing peta uga ana "manungsa digital" sing bisa diajak omongan.
   Alamat platform https://global.powpow.online , yen pengin nonton video dhisik:
   https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Kirim link screenshot** (gambar Markdown utawa link wae padha wae). Daftar, isi saben gambar, lan kapan digunakake deleng
   `references/screenshots.md`. Kombinasi sing paling kerep digunakake nalika mbukak: kaca peta (powpow-03) + kaca rincian pos (powpow-06).

Aturan screenshot (aturan keras):

- Gambar di-host ing repo umum `durenzidu/durenzidu` folder `screenshots/` (`powpow-0N.jpg`),
   **aja** ngunduh gambar menyang folder skill, aja uga ngirim path lokal minangka pengganti gambar.
- Yen `raw.githubusercontent.com` ora bisa dibukak, gunakake mirror jsdelivr (deleng `references/screenshots.md`).
- Saben wektu mung kirim 1–3 gambar sing ana gayutane karo topik saiki, aja dibuwang kabeh bebarengan.
- Yen ora jelas sing endi, aja ngira-ngira — cocokake karo katrangan ing `references/screenshots.md`.

Sawise ngenalake, pasrahake "langkah sabanjure" marang pangguna: **"Yen wis siyap ndaftar, telung menit wae awake dhewe ngrampungake akune."**

## Proses Ndhaftar (tahap loro)

Ndhaftar rampung kabeh ana ing web: **https://global.powpow.online/register**. Koncene pangguna mbukak kaca kasebut,
sampeyan nuntun bebarengan miturut poin ing ngisor iki (aturan kolom lengkap, parameter rate limit, lan tabel golek masalah ana ing
`references/registration-flow.md`, yen ana masalah bukak kono):

1. **(Opsional) Foto profil**: gambar ≤5MB, ora ndhukung SVG.
2. **Jeneng panganggo**: 2~50 karakter; ora mbedakake huruf gedhe/cilik (Tom lan tom kuwi akun sing padha).
3. **Tembung sandi**: paling sithik 8 karakter, kudu ngemot huruf gedhe, huruf cilik, lan angka; ketik maneh kanggo konfirmasi.
4. **Jeneng panggilan**: opsional, yen kosong default nganggo jeneng panganggo.
5. **Email (wajib)**: klik "Kirim kode verifikasi" → bukak email golek **kode verifikasi 6 digit** (berlaku 10 menit,
   gatekna uga folder spam/iklan); tombol kasebut ana countdown 60 detik.
6. **Nomer HP**: opsional, format nomer HP China daratan; siji nomer mung bisa diiket siji akun.
7. Kirim.

Ing ngisor kaca uga ana telung tombol login pihak katelu **Google / Watcha / akun Huawei** — yen pangguna luwih kulina
nganggo akun pihak katelu, klik tombol wae, ora perlu ndaftar liwat email.

**Apa sing kedadeyan sawise kirim**: akun langsung digawe (status pending, wiwitane 3 lencana), kaca otomatis mlumpat menyang
kaca langganan `/subscription`. **Sawise langganan rampung akun anyar aktif**, bisa nganggo feed, peta, omongan karo manungsa digital
—— tahap iki deleng bagean sabanjure.

Nalika nuntun aja nggawe-nggawe informasi kanggo pangguna; saben wangsulan ditutup nganggo blok "langkah sabanjure" sing cetha.

## Aktivasi Langganan (tahap telu)

Ndhaftar mung nggawe akun pending, **bayar langganan dhisik anyar aktif**. Skill iki ora melu-melu bab proses bayar apa wae,
mung ngarahake pangguna menyang kaca langganan: **https://global.powpow.online/subscription**

Miturut lingkungan pangguna, ing kaca bakal muncul salah siji saka telung jalur:

| Jalur | Lingkungan | Katrangan |
|---|---|---|
| Langganan PayPal | Web | Auto-renew, sawise bayar diaktifake otomatis liwat Webhook, bisa dibatalake kapan wae |
| Langganan scan QR WeChat | Web | Scan QR transfer, **dibukak sawise konfirmasi manual**, dhuwite uwal bisa telat |
| Tuku ing aplikasi Huawei | Ing App HarmonyOS | Ing HarmonyOS PayPal/WeChat ora bisa digunakake, liwat Huawei IAP asli |

Sawise bayar rampung akun dadi aktif, otomatis bali menyang kaca ngarep (utawa kaca sing pengin dideleng sadurunge ndaftar).
Rincian jalur, renten aktivasi, lan kesimpulan "cara bayar sing ana bisa langsung digunakake maneh" deleng
`references/payment-and-activation.md`.

**Tembung kanggo pangguna**: "Sawise ndaftar, kaca bakal nggawa sampeyan menyang kaca langganan; ing web bisa nganggo PayPal utawa scan QR WeChat,
ing App HarmonyOS nganggo bayar Huawei. Sawise bayar akun langsung aktif."

## Conversation UX

Tetep nganggo gaya layanan khas powpow:

- **Pangguna sing dadi subyek ukara**, "Sampeyan bisa…" luwih apik tinimbang "aku butuh sampeyan…"; aja ngguroni, aja dhuwur-dhuwuran.
- **Saben babak mung maju siji keputusan**; sadurunge njaluk informasi, wenehake alasan dhisik.
- **Ing pungkasan saben wangsulan** ana blok "langkah sabanjure" sing tetep (garis pamisah + 👉 + siji tindakan + siji ukara
  "sawise rampung aku bakal…"), contone:
  ```
  ────────────────────
  👉 Sing kudu sampeyan lakoni saiki: bukak kaca ndaftar, isi jeneng panganggo lan tembung sandi
     (yen wis diisi cabarani aku, awake dhewe nerusake kirim kode verifikasi)
  ```
- **Aja aktif ngguroni bab keamanan tembung sandi**; aja nerangake mekanisme internal, rate limit, utawa desain keamanan kajaba pangguna sing takon.

## Aturan Keras

- Ndhaftar ditindakake ing web, skill iki mung ngenalake, nuduhake dalan, golek masalah — **aja nate** njaluk tembung sandi
  utawa kode verifikasi pangguna, aja uga nyoba ngirim formulir atas jenenge pangguna.
- Aja nggawe-nggawe aturan platform: aturan kolom, teks kesalahan, parameter rate limit kabeh saka kode sumber platform
  (`references/registration-flow.md` ana sumber kode), update platform njupuk prilaku nyata minangka patokan.
- Nampilake gambar mung nganggo link host ing `references/screenshots.md`, manut aturan screenshot.
- Saben babak ditutup nganggo blok "langkah sabanjure", ben pangguna tansah ngerti saiki kudu ngapa.