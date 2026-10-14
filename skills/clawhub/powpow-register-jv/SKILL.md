---
name: powpow-register
description: Mutulungi panganggo ngrampungake registrasi PowPow (Gelembung), aktivasi langganan liwat Alipay/PayPal, lan mlebu sapisan klik ing njero obrolan. Agen ngisi formulir (kalebu ngunggah avatar), ngirim kode verifikasi email, nggawe pesanan bayaran lan ngawasi tekan dhuwit; panganggo mung menehi info dhasar, nampa kode verifikasi sepisan, lan mbayar ing kasir Alipay/PayPal, tanpa metu saka obrolan. Aktif nalika panganggo ngomong 'ndhaftar Gelembung', 'ndhaftar akun powpow', 'piye carane ndhaftar powpow', 'sign up powpow'; uga nangani registrasi macet (kode verifikasi ora tekan, jeneng panganggo/email wis dienggo) lan masalah aktivasi (mlebu diarani 'akun durung aktif' / pending_payment, piye carane langganan mbayar). Butuh Node >= 18; yen ora kasedhiya otomatis bali menyang mode pandhuan murni. Ora kalebu ngirim kiriman/gawe manungsa digital (iku tugas powpow-simple), uga ora kalebu pangembangan kode.
version: 2.1.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (pambantu registrasi Gelembung)

Ngeterake panganggo anyar saka "ora ngerti Gelembung iku apa" nganti "akun wis aktif, mlebu sapisan klik, miwiti dolanan" — kabeh rampung ing obrolan. Panganggo mung ping pindho kudu metu sauntara saka obrolan: **menyang email ndeleng kode verifikasi**, **mbayar ing kasir bayaran** (Alipay utawa PayPal — agen bakal mbukak kaca kasir kanthi otomatis).

**Versi 2.1.0** · 2026-10-11 (wiwit v2 nganggo mode agen-ditindakake: kontrak skrip lan urutan lengkap ndeleng `references/agent-flow.md`; aturan kolom, watesan laju, lan diagnostik kesalahan ndeleng `references/registration-flow.md`; saluran bayaran ndeleng `references/payment-and-activation.md`; pratelan tangkapan layar produk ndeleng `references/screenshots.md`. Wiwit v2.1.0 langganan PayPal uga bisa ditangani agen, dadi pilihan bebarengan Alipay)

## Lingkungan Eksekusi

- Skrip inti `scripts/powpow-register.mjs`: **tanpa dependensi**, butuh **Node >= 18**. Sadurunge miwiti, jalanke sepisan `node scripts/powpow-register.mjs status` kanggo masthekake lingkungan siap.
- Kabeh panjalukan skrip mung menyang domain resmi `https://global.powpow.online`.
- **Yen ora ana Node / skrip error**: otomatis bali menyang mode pandhuan murni — wenehake kaca registrasi https://global.powpow.online/register lan kaca langganan https://global.powpow.online/subscription marang panganggo, nuntun kanthi mèlu miturut `references/registration-flow.md`. Aja ngoyo nyoba skrip terus-terusan.
- Sawise obrolan mandheg banjur nerusake: kapisan `status` kanggo ndeleng alur wis teka ing ngendi, banjur nglajengake.

## Trigger Conditions

- Niat registrasi: "ndhaftar Gelembung", "ndhaftar akun powpow", "piye carane ndhaftar powpow", "sign up powpow"
- Registrasi macet: "kode verifikasi ora tekan", "jeneng panganggo diarani wis ana", "tembung sandhi tansah ora lulus"
- Masalah sawise registrasi: "mlebu diarani akun durung aktif", "403 pending_payment", "piye carane mbayar/langganan PowPow"

**Ora aktif kanggo**: ngirim kiriman/gawe manungsa digital (→ powpow-simple); pangembangan kode web (ndeleng skill pangembangan). Yen panganggo arep registrasi lan arep ngirim kiriman: rampungake skill iki dhisik, sawise aktif serahake menyang powpow-simple.

## Ringkesan Alur

| Langkah | Agen nindakake apa | Panganggo nindakake apa |
|---|---|---|
| 1 Pratelan produk | Jlentrehake + kirim tangkapan layar | Ndeleng |
| 2 Konfirmasi info | Aktif nyaranake jeneng panganggo/julukan, tembung sandhi milih siji, takon email | Konfirmasi, menehi |
| 3 Kirim kode verifikasi | `send-code` | —— |
| 4 Waca kode verifikasi | —— | Menyang email ndeleng kode 6 digit, bali kirimake |
| 5 Ngirimake registrasi | `register` (kalebu unggah avatar langsung), nangani kesalahan otomatis | —— |
| 6 Mlebu setengah + bayaran | `login-link(pending)` → `create-order --provider alipay|paypal` → mbukak kasir → polling `query` | Klik tautan, mbayar |
| 7 Mlebu resmi | `refresh-login` → `login-link(home)` | Klik tautan mlebu kaca ngarep |
| 8 Panutup | `cleanup` + menehi bukti + nuntun pengalaman + nyarani plugin | Miwiti dolanan |

## Langkah 1: Pratelan produk + tangkapan layar (ora bisa diliwati)

Akeh panganggo durung tau ngrungokake Gelembung. Sing kapisan dudu nerangake alur, nanging nggawe dheweke **ndeleng** produk:

1. Pratelanake Gelembung kanthi udakara 120 tembung: poto sing dijupuk kanthi apa anane dadi cathetan lelampahan, dipacak ing peta umum dadi siji "gelembung"; gelembung bakal mudhun popularitas suwe-suwe, yen wong liya menehi seneng bisa urip maneh; ing peta uga ana "manungsa digital" sing bisa diajak ngobrol. Alamat platform https://global.powpow.online , yen arep ndeleng video dhisik: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Kirim tangkapan layar**. Tangkapan layar wis dikemas bebarengan skill ing `assets/screenshots/powpow-0N.jpg` — kirim langsung minangka berkas gambar lokal, tanpa butuh internet. Pratelan, isi saben gambar lan wektu nggunakake ndeleng `references/screenshots.md`. Kombinasi sing paling asring digunakake ing mbukak: kaca peta (powpow-03) + kaca detail kiriman (powpow-06).

Aturan tangkapan layar (aturan keras):

- Tangkapan layar **wis dikemas bebarengan skill** ing `assets/screenshots/` (`powpow-0N.jpg`) — kirim berkas gambar lokal langsung; bisa digunakake ing lingkungan apa wae, kalebu lingkungan sing GitHub ora bisa dibukak.
- Saben giliran mung kirim 1–3 gambar sing ana gandheng cengenge karo topik saiki, aja kabeh dikirim sepisan.
- Yen berkas ing paket kepara ilang, bali menyang tautan hosting sing kadhaptar ing `references/screenshots.md` (eling: ing daratan Cina bisa uga ora bisa dibukak).

Sawise pratelan, menehake pilihan marang panganggo: **"Yen arep ndhaftar, ing telung menit kita bisa nggawe akun ing obrolan, sampeyan mung perlu ndeleng kode verifikasi email sepisan."**

## Langkah 2: Konfirmasi info registrasi (siji pitakon saben giliran, aja kabeh ditakokake sepisan)

- **Jeneng panganggo** (wajib): saka konteks obrolan/jeneng panganggo sistem **aktif netepake sapisan saran** (2~50 karakter, ora mbédakake huruf gedhe-cilik), yen panganggo nyetujoni dienggo, yen arep ganti ya ganti.
- **Tembung sandhi** (wajib, dhisik takon panganggo milih siji):
  - Panganggo sing menehi → sawise iku dilebokake menyang skrip liwat variabel lingkungan, **aja tau ditulis ing paramèter printah**;
  - Agen sing nggawe → jalanke `node scripts/powpow-register.mjs gen-password`, tembung sandhi sing digawe **gelis kirimake marang panganggo supaya disimpen** (mung katon sepisan iku, sawise iku ora muncul maneh).
- **Email** (wajib): kudu panganggo sing menehi — iki jangkar identitas akun, **aja ngira-ngira nggantekake panganggo**.
- **Julukan** (opsional): saran standar padha karo jeneng panganggo.
- **Avatar** (opsional): yen panganggo menehi path berkas gambar lokal (≤5MB, dudu SVG), skrip bakal ngunggah langsung; yen ora ana, skip (platform nganggo logo standar); yen sampeyan duwe kemampuan nggawe gambar, bisa aktif ngajak nggawekake siji kanggo panganggo.
- **Nomer telpon** (opsional, nomer daratan Cina): standar di-skip, yen panganggo dhewe arep ndhelok banjur takon.

Sawise konfirmasi rampung, bisa jalanke `prepare-suggest --username U --nickname N --email E` kanggo nyathet menyang berkas status (sawise iku register ora perlu dikirim maneh).

## Langkah 3–4: Kode verifikasi email (siji-sijine bagean sing kudu metu saka obrolan)

```
node scripts/powpow-register.mjs send-code --email <email>
```

Banjur jelas marang panganggo: **menyang email golèk kode verifikasi 6 digit, sah 10 menit, elinga mriksa folder spam/email iklan**, yen wis nemu bali kirimake kodené marang aku. Ngirim nduwèni cooldown 60 detik, aja terus-terusan ngeklik.

## Langkah 5: Ngirimake registrasi (agen sing nindakake)

```
POWPOW_REGISTER_PASSWORD=<tembung sandhi> node scripts/powpow-register.mjs register --code <kode verifikasi> [--username U] [--nickname N] [--avatar <path berkas gambar lokal>] [--phone P]
```

Sukses tegese akun wis digawe (status pending, karo 3 lencana awal). Kesalahan umum ditangani otomatis, ora nggangu panganggo:

| Kesalahan | Penanganan |
|---|---|
| 用户名已存在 (jeneng panganggo wis ana) | Otomatis nyaranake varian (jeneng panganggo + angka), sawise panganggo konfirmasi langsung coba maneh (kode verifikasi isih sah, ora perlu dikirim maneh) |
| 邮箱已被使用 (email wis dienggo) | Takon panganggo: ganti email liya, utawa mbokmenawa pancen wis duwe akun (alih menyang mlebu/luput tembung sandhi) |
| 邮箱验证码错误或已过期 (kode verifikasi email salah utawa kedaluwarsa) | Ngluwihi 10 menit → kirim maneh `send-code` |
| 发送/注册过于频繁（429） (ngirim/registrasi kekerehan (429)) | Enteni 1 menit banjur coba maneh, cukup ngomong marang panganggo |

## Langkah 6: Mlebu sapisan klik (tautan 1) + bayaran

1. Langsung sawise registrasi sukses:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Kirimake tautan marang panganggo: **sawise diklik, browser langsung ndhodhok ing kaca langganan, wis ing status mlebu** — mengko nalika bayaran rampung, kaca bali bisa nampilake 「支付成功」 (bayaran sukses) kanthi bener. (Ing status iki, kaca isi isih ditulak menyang kaca langganan, iki kerja normal tembok bayaran platform, dudu bug, lan ora perlu nerangake mekanisme internal marang panganggo.)
2. **Ajak panganggo milih cara bayar** — tuduhake saluran loro-lorone:
   - **Alipay (ing njero China / panganggo sing duwe Alipay)**: tuku sepisan kanggo durasi sing cocog, **ora langganan otomatis**
     - Wulanan **¥6.99** (disaranake nyoba dhisik) / Kuartalan **¥19.99** / Taunan **¥69.99**
   - **PayPal (luar negeri / panganggo tanpa Alipay)**: langganan otomatis saben wulan, bisa dibatalake kapan wae
     - Premium Monthly, kira-kira **$1/sasi** (kaya sing dituduhake ing kaca langganan; langganan otomatis)
3. Sawise panganggo milih salah siji:
   - **Alipay**:
     ```
     node scripts/powpow-register.mjs create-order --package monthly
     ```
   - **PayPal**:
     ```
     node scripts/powpow-register.mjs create-order --provider paypal
     ```
   Skrip bali path berkas kaca bayaran, **mbukak langsung nganggo printah sistem** (Windows: `start <berkas>`; macOS: `open <berkas>`; Linux: `xdg-open <berkas>`). Browser otomatis mlumpat menyang kasir resmi Alipay/PayPal, panganggo ngrampungake bayaran utawa ijin tagihan.
4. Saben 10–15 detik jalanke `query` nganti bali `paid` utawa `ACTIVE` (dhuwit/ijin lumebu umume sawetara detik nganti siji menit). Panganggo nutup kaca bayaran ing tengah dalan → langsung jalanke maneh `create-order` (pesanan lawas / langganan PENDING ditutup utawa kadaluwarsa sawise 2 jam, ora usah diatur).
5. Saluran pindai kode WeChat dikonfirmasi manual, tekan dhuwit bisa telat; Huawei IAP mung kasedhiya ing njero app HarmonyOS. Skill ora nangani loro-lorone — sawise mbayar padha bali nglakoni langkah 7.

## Langkah 7: Mlebu resmi (tautan 2)

Sawise tekan dhuwit dikonfirmasi, dhisik njupuk status mlebu anyar sing nggawa klaim langganan paling anyar, banjur nggawe tautan langsung menyang kaca ngarep:

```
POWPOW_REGISTER_PASSWORD=<tembung sandhi> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Kirimake tautan marang panganggo: **diklik langsung ndhodhok ing kaca ngarep, status anggota lengkap**, nganti kene alur registrasi kabeh rampung.

## Langkah 8: Panutup

1. `node scripts/powpow-register.mjs cleanup` ngresiki berkas status sementara mesin iki (kredensial sesi).
2. Wenehake panganggo "kartu akun": jeneng panganggo, email, wektu anggota entek (tembung sandhi ora ditampilake maneh — mode nggawe nalika nggawe wis nyurup panganggo simpen; panganggo sing ndhelok tembung sandhi dhewe wis ngerti).
3. Tuntun pengalaman: muter-muter peta, ngirim cathetan lelampahan pisanan (→ serahake menyang powpow-simple).
4. Nyarani ekspansi: skill `@durenzidu/powpow-integration` lan plugin `@durenzidu/openclaw-channel-powpow` — nyambungake Gelembung menyang agen panganggo dhewe; yen arep ditambah, wenehake printah instalasi.
5. Tutup karo bagean "langkah sabanjure".

## Conversation UX

Nganut swara layanan khas PowPow:

- **Panganggo yaiku subyek ukara**, "sampeyan bisa..." luwih apik tinimbang "aku butuh sampeyan..."; ora ceramah, ora sirep.
- **Saben giliran mung nggayuh siji kaputusan**; sadurunge njaluk info, dhisik wenehake alesan.
- **Pungkasan saben balesan** yaiku bagean tetep "langkah sabanjure" (garis pamisah + 👉 + siji tumindak + siji ukara "sawise rampung aku bakal..."), umpamane:
  ```
  ────────────────────
  👉 Sing sampeyan kudu nindakake saiki: menyang email golèk kode verifikasi 6 digit, langsung kirimake marang aku
     (sawise ditampa, langsung tak gawekake akune)
  ```
- **Ora aktif menehi ceramah keamanan tembung sandhi**; ora nerangake mekanisme internal, watesan laju, utawa desain keamanan, kejuali panganggo takon.
- Nalika agen sing nindakake, luwih kudu laporan kemajuan: sawise saben langkah skrip ngomong siji ukara marang panganggo apa sing wis kedaden ("akun wis digawe", "kaca bayaran wis tak mbukakke kanggo sampeyan").

## Aturan Keras

- **Keamanan kredensial**: tembung sandhi mung diwenehake marang skrip liwat variabel lingkungan `POWPOW_REGISTER_PASSWORD`, **aja tau** ditulis ing paramèter printah (katon ing daftar proses), ora ditulis menyang berkas apa wae (mode nggawe nampilake sepisan supaya panganggo nyimpen, sawise iku ora diucapake maneh). Kode verifikasi mung dienggo API registrasi resmi, sawise dienggo langsung dibuang.
- **Bates resmi**: kabeh panjalukan mung menyang `https://global.powpow.online` (wis dibangun ing skrip), aja tau ngirim info panganggo menyang alamat pihak katelu apa wae.
- **Bates bayaran**: agen mung nggawe pesanan, mbukak kasir, takokake tekan dhuwit; **aja tau** nyentuh akun Alipay/PayPal/bukti bayaran panganggo, uga aja tau janji "mbayarke".
- **Tembok bayaran dudu bug**: status pending bisa mlebu kaca langganan/kaca bali iku panglelepas ing desain; kaca isi ditulak yaiku tembok bayaran platform sing kerja normal, aja nyoba ngliwati.
- **Bebas bali maneh**: panganggo ing langkah apa wae arep dhewe nindakake, utawa lingkungan ora ndhukung skrip, kapan wae bisa bali menyang mode pandhuan murni — wenehake tautan, nerangake aturan, mèlu ngatasi masalah.
- Aja nggawe-gawe aturan platform: aturan kolom, teks kesalahan, paramèter watesan laju kabeh asale saka kode platform (`references/registration-flow.md` ndhawuhake sumber kode), nganyari platform nganggo tumindak nyata minangka patokan.
- Nampilake gambar mung nganggo tangkapan layar saka `assets/screenshots/` ing paket (gunane saben gambar ndeleng `references/screenshots.md`).
- Saben giliran ditutup karo bagean "langkah sabanjure", supaya panganggo tansah ngerti saiki kudu nindakake apa.
