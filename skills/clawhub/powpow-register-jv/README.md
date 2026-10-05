# powpow-register

Pitulung ndhaptar PowPow Gelembung (versi OpenClaw): nggawa pangguna anyar saka "ora ngerti Gelembung kuwi apa" nganti
"akun aktif, bisa digunakake normal" — pambuka produk (kalebu screenshot), panduan ndhaptar tahap demi tahap,
golek masalah, katrangan aktivasi langganan.

Skill panduan murni, tanpa script, tanpa dependensi; kabeh tumindak ndhaptar ditindakake pangguna ing browser/App.

## Instalasi

```
openclaw skills install @durenzidu/powpow-register
```

## Fungsi

1. **Pambuka produk**: mbukak ~120 tembung + link screenshot interface sing di-host ing repo umum GitHub
   (kaca peta, kaca rincian pos, lsp. 6 gambar, pilih kirim 1–3 miturut kahanan).
2. **Panduan ndhaptar**: aturan kolom (jeneng panganggo/tembung sandi/kode verifikasi email/nomer HP/foto profil), login pihak katelu
   (Google/Watcha/Huawei), parameter rate limit, kabeh saka kode sumber platform lan dicathet sumbere.
3. **Golek masalah**: kode verifikasi ora teka, jeneng panganggo/email wis digunakake, 403 durung aktif, akun dikunci, lsp.
   13 masalah sing kerep kedadeyan.
4. **Aktivasi langganan**: katrangan lan golek masalah telung jalur PayPal (web) / WeChat scan QR (konfirmasi manual) / Huawei IAP (HarmonyOS);
   renten bayar sing ana bisa langsung digunakake maneh, skill mung dadi penunjuk dalan.

## Struktur File

```
powpow-register/
├── SKILL.md                            # Panduan utama (kondisi micu, proses, standar gaya)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Aturan kolom, rate limit, tabel golek masalah (kalebu sumber kode)
    ├── payment-and-activation.md       # Aktivasi langganan, jalur bayar, kesimpulan digunakake maneh
    └── screenshots.md                  # Daftar screenshot sing di-host + cek cepet miturut kahanan
```

## Keamanan

- Ora ngemot kunci apa wae; tanpa script, ora ndemek kredensial pangguna.
- **Aja nate njaluk** tembung sandi, kode verifikasi, utawa bukti bayar pangguna; ndhaptar lan bayar rampung kabeh ana ing kaca platform.

## Lisensi

MIT-0 (lisensi seragam ClawHub).

## Link

- Situs resmi: https://global.powpow.online
- Ndhaftar: https://global.powpow.online/register
- Kenal Gelembung (video): https://www.bilibili.com/video/BV1Wu826UEVz/