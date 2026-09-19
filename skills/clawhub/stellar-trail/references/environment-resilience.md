# Environment Resilience — Anti-Rollback Playbook (Container Platforms)

> **Kapan membaca file ini:** lingkungan kerja Anda berjalan di container/sandbox yang bisa di-reset
> (contoh: preview container platform, ephemeral CI runner) DAN Anda melihat gejala: file hasil kerja
> "hilang" setelah restart, versi file terdegradasi ke kondisi lama, atau skill/skrip custom lenyap.
> Bila Anda bekerja di mesin lokal/statis yang tidak pernah di-reset, seksi ini tidak berlaku — abaikan.

## 1. Model Ancaman: Bagaimana Container Me-Rollback State Anda

Banyak platform container memulihkan direktori proyek dari sebuah **arsip restore** (contoh nyata:
`/home/sync/repo.tar` yang diekstrak oleh hook `/start.sh` saat boot — `rm -rf <project>` kecuali
mountpoint, lalu `tar xf repo.tar`). Arsip ini idealnya ditulis ulang oleh **pre-stop packer** saat
container berhenti. Masalahnya: **pre-stop tidak selalu jalan** — container bisa di-crash, di-force-kill,
atau pack-nya gagal (cabang kegagalan ini diakui sendiri oleh hook platform). Akibatnya boot berikutnya
me-restore **kondisi lama**: rollback diam-diam yang menghapus jam-jam kerja.

Empat fakta struktural yang bisa dimanfaatkan (diverifikasi empiris pada satu platform container, 2026):

1. **Sumber restore terbaca**: hook boot dan arsip restore biasanya dapat dibaca dari dalam container
   (`cat` hook-nya, `tar -tf` arsipnya) — Anda bisa membedah formatnya tanpa menebak.
2. **Mount object-storage bertahan**: direktori yang di-mounted dari object storage (mis. ossfs) hidup
   DI LUAR container dan tidak ikut ter-rollback — kanal penyelamatan untuk backup dan marker state.
3. **Boot menoleransi arsip korup** (warning + lanjut) — kegagalan refresh tidak membuat container mati.
4. **Packer bisa mengecualikan direktori penting** (forensik nyata: `skills/` tidak pernah masuk arsip
   packer platform) — instalasi skill adalah target rollback yang paling sering kena.

## 2. Lapisan Pertahanan (sejak v3.3.0 — lapis shadow backup dihapus; catatan arsitektur 2026-09-19 di bawah)

| Lapis | Peran | Kapan bekerja |
|---|---|---|
| **L1 — Refresh sumber** (`scripts/snapshot-repo.sh`) | Menimpa arsip restore platform dengan snapshot kondisi TERKINI — kini termasuk `skills/stellar-trail` (append bedah) — sehingga restore boot native = state segar *selama arsip itu bertahan* | `--apply` setelah milestone signifikan; `--apply-auto` berkala (debounce + cooldown 15 mnt) |
| **L2 — Self-heal instalasi** (`scripts/heal-skill.sh`) | Verifikasi manifest SHA-256 instalasi skill; bila drift (file hilang/rusak/ekstra, versi `_meta.json` mundur) → perbaikan dari sumber sehat berikutnya: kanonik → arsip restore → registry | `--check` (deteksi + heal) / `--force`; cocok untuk boot hook & jalankan berkala |
| **L3 — Backup original** | Undo: arsip restore asli platform disalin sebelum ditimpa — bisa dikembalikan kapan pun | Selalu, sebelum setiap swap L1 |

L1 mencegah rollback **di sumbernya**; L2 **menyembuhkan instalasi** bila rollback/clobber tetap terjadi
(arsip basi, cache platform, taruhan apa pun); L3 menjamin setiap intervensi terhadap infrastruktur
**bisa di-undo**. Ketiganya saling independen — kegagalan satu lapis tidak melumpuhkan dua lainnya.

**Temuan arsitektur 2026-09-19 (forensik boot):** pre-stop packer platform ternyata MENIMPA arsip
restore dengan arsipnya sendiri di setiap siklus henti — build L1 kita (termasuk append bedah
`skills/stellar-trail`) **tidak pernah bertahan lintas boot**. Bukti: boot 05:34 menemukan repo.tar
"asing" (0 entri `skills/`) dan direktori `skills/stellar-trail` hilang total, padahal build L1
malam sebelumnya membawa 32 entri skill. Konsekuensinya, peran lapisan bergeser: **rantai lintas-boot
yang benar-benar efektif = kanonik `download/stellar-trail/` (persisten via arsip platform, yang
memang memuat `download/`) + L2 boot-heal** (menyembuhkan instalasi dari kanonik itu, termasuk
membuat ulang `_meta.json`/`origin.json` bila instalasi ter-wipe total — sejak v3.5.2). L1 tetap
bernilai untuk kesegaran intra-boot (repo.tar tidak pernah >15 mnt lebih tua) dan kanal undo L3.

**Dua konvensi lokasi install clawhub (temuan 2026-09-19):** clawhub CLI ≥ 0.23.3 memasang fresh
install **owner-scoped**: `skills/@owner/stellar-trail` dengan lock key `@owner/stellar-trail`;
instalasi era CLI lebih lama bisa flat: `skills/stellar-trail` dengan lock key `stellar-trail`.
Seluruh rantai L2 dan boot-hook (dev.sh / template) sejak v3.5.2 **location-aware**: mencari dan
menyembuhkan KEDUA layout, resolusi sumber walk-up multi-level, dan hint update membaca lock key
aktual dari `.clawhub/lock.json`.

**Mengapa tidak ada lagi lapis shadow backup (pelajaran empiris, dihapus di v3.3.0):** generasi
arsitektur sebelumnya menyertakan shadow backup rolling (snapshot proyek periodik ke mount persistent,
dipulihkan otomatis saat deteksi stale). Empat temuan forensik memvonisnya merugikan: (1) deteksi
stale-nya **false-positive** — aktivitas backupnya sendiri menaikkan heartbeat lalu memicu percobaan
restore yang gagal (insiden 07:38 UTC: dua percobaan restore beruntun gagal ekstrak); (2) **blind spot
yang sama** dengan sumbernya — `skills/` tetap tidak terlindungi justru oleh lapis yang katanya
penyelamat; (3) **failure domain yang sama** — hidup di mount object storage yang sama persis dengan
arsip yang diamankan; (4) biaya tulis 62 MB per 30 menit untuk perlindungan semu. Pelajaran umumnya:
**backup yang jalur restore-nya tidak pernah teruji lebih berbahaya daripada tidak ada backup** — ia
memberi rasa aman sambil menambah mode kegagalan baru. Dua lapis yang tersisa kini keduanya teruji
end-to-end, dan kanal ketiga (registry ClawHub) selalu tersedia sebagai jaring terakhir.

## 3. Memakai Skrip

### 3a. `scripts/snapshot-repo.sh` (L1 — refresh arsip restore)

```
bash scripts/snapshot-repo.sh --status             # diagnosis: usia arsip restore, verdict BASI/SEGAR
bash scripts/snapshot-repo.sh --dry-run            # build + verifikasi penuh TANPA menyentuh arsip
bash scripts/snapshot-repo.sh --apply              # backup asli -> build -> verifikasi -> swap -> verifikasi
bash scripts/snapshot-repo.sh --apply-auto         # --apply dengan gerbang ganda (debounce + cooldown) —
                                                   # aman dipanggil berkala dari boot hook / watcher
bash scripts/snapshot-repo.sh --restore-original   # undo: kembalikan arsip asli terakhir (terverifikasi)
```

Prinsip keamanan yang dipegang skrip (jangan dilanggar saat memodifikasi):

- **Konsen eksplisit untuk aksi manual**: `--apply`/`--restore-original` hanya dijalankan saat diminta;
  `--apply-auto` sengaja berat gerbangnya (debounce + cooldown) agar aman dipicu berkala.
- **Backup-first**: arsip asli disalin ke mount persistent SEBELUM swap; bila backup gagal, swap batal.
- **Verify-before-swap**: tar divalidasi (struktur + jumlah entri + entri kunci) dua kali — build dan
  staging — sebelum rename-overwrite; final diverifikasi lagi setelah swap.
- **Audit member anti traversal**: arsip restore diekstrak platform via `tar xf` tanpa validasi
  member, maka skrip sendiri yang menjaga: member absolut atau berkomponen `..` DITOLAK keras,
  symlink ber-target absolut diperingatkan; `--restore-original` pun diaudit sebelum swap
  (undo tetap byte-identical — verifikasi hanya membaca, arsip korup/hostile ditolak agar tidak
  merusak boot berikutnya).
- **Build anti argument-injection**: daftar entri NUL-terpisah via `tar --null -T` — nama file
  tidak pernah di-parse sebagai opsi tar (file `--use-compress-program=...` di project root
  tidak bisa membuat tar mengeksekusi perintah); nama diawali `-` atau ber-newline di-skip.
  Disiplin penyerta: fungsi yang memproduksi data di stdout tidak boleh mencetak diagnostik
  ke stdout (`slog_q` log-only) — diagnostik bocor akan terbaca sebagai entri daftar.
- **Marker fingerprint**: arsip buatan sendiri ditandai (mtime|size) agar tidak dibackup berulang dan
  backup original sejati tidak tertimpa (pelajaran bug kolisi nama resolusi-detik).
- **Format mengikuti packer platform**: entri relatif tanpa prefix `./`, exclude `node_modules/`,
  `db/`, `upload/`, `.venv/`, `.next/` — beda format = restore aneh. Pengecualian `skills/`
  milik packer ditutup dengan append bedah `skills/stellar-trail` (path literal, bukan ekspansi
  nama file — vektor injection tidak berlaku).
- **Atomic sebisanya mount**: build di disk lokal -> salin ke nama staging di mount yang sama ->
  rename-overwrite in-mount (rename didukung umum oleh FUSE object-storage).

### 3b. `scripts/heal-skill.sh` (L2 — self-heal instalasi, sejak v3.3.0)

```
bash scripts/heal-skill.sh --status     # laporan versi + drift, TANPA aksi
bash scripts/heal-skill.sh --check      # deteksi drift; heal bila ada (default)
bash scripts/heal-skill.sh --force      # heal tanpa deteksi
bash scripts/heal-skill.sh --manifest   # regenerasi manifest (SAAT RILIS, di salinan kanonik)
bash scripts/heal-skill.sh --dir <path> <mode>   # target instalasi stellar-trail lain
```

- **Verifikasi tanpa sumber eksternal**: manifest `assets/integrity.sha256` (hash seluruh file
  konten) + `assets/integrity.version` (versi rilis) — file hilang, rusak, ekstra, dan versi
  `_meta.json` yang mundur (signature persis insiden degrade nyata) semuanya terdeteksi.
- **Perbaikan multi-sumber berurut** (location-aware sejak v3.5.2): `STELLAR_CANONICAL` (env) →
  `<proyek>/download/stellar-trail` (deteksi walk-up **2/3/4 level** dari lokasi skill — flat
  `skills/<slug>` maupun owner-scoped `skills/@owner/<slug>`) → arsip restore
  (`STELLAR_RESTORE_TAR`, default `/home/sync/repo.tar`, subtree sesuai **layout aktual**
  instalasi) → hint manual `clawhub update <lock-key> --force` (butuh login; lock key dibaca
  dari `.clawhub/lock.json` instalasi, bukan hardcoded). Bila semua sumber lokal gagal, skrip
  **gagal keras**: tanpa manifest DAN tanpa sumber, `--check` exit 1 dengan pesan eksplisit
  (sejak v3.5.2 — sebelumnya WARN senyap exit 0) — verifikasi yang mustahil tidak pernah
  menyamar jadi sukses.
- **Aman by design**: identitas install clawhub (`_meta.json` ownerId/publishedAt, `.clawhub/`)
  tidak pernah ditimpa — hanya field versi yang dipatch konsisten; bila keduanya absen akibat
  instalasi ter-wipe total saat boot, file minimal dibuat ulang (v3.5.2); hasil heal 0644 tanpa
  exec bit, identik dengan perilaku registry (semua invokasi memang via `bash`/`python3`).
- **Di lingkungan reset-prone**: panggil `--check` dari boot hook (setelah L1) dan/atau berkala
  dari watcher — biayanya lokal dan murah; manifest membuat hasilnya bisa diaudit.

## 4. Prosedur Pasca-Reset (Decision Tree Saat Boot Segar)

1. **Deteksi apakah rollback/degrade terjadi**: gejala cepat — file termutakhir hilang, atau
   `bash scripts/heal-skill.sh --status` melaporkan DRIFT / versi `_meta` mundur.
2. **Drift terdeteksi** ⇒ `bash scripts/heal-skill.sh --check` — heal otomatis dari kanonik atau
   arsip restore; lalu jalankan L1 `--apply` agar sumber ikut segar; `git status` untuk file ekstra
   sisa restore (rsync-heal menghapus ekstra di dalam skill dir, bukan seluruh proyek).
3. **Kanonik ikut hilang** ⇒ heal dari arsip restore (repo.tar membawa `skills/stellar-trail`);
   bila arsip pun basi ⇒ `clawhub update <lock-key> --force` setelah re-login — lock key dilihat
   dari `.clawhub/lock.json` (instalasi flat: `stellar-trail`; owner-scoped:
   `@hoshiyomix/stellar-trail`; hint akurat juga tercetak otomatis oleh heal-skill). Ingat:
   `~/.config` tidak persisten lintas restart — token login harus di-set ulang.
4. **Tidak terjadi** ⇒ cukup pastikan L1 segar bila hendak berhenti/istirahat.
5. **memory/ ikut hilang** (reset total) ⇒ pulihkan dari handoff terbaru di mount persistent;
   bila tidak ada, jalankan cold-start protocol (Part II seksi 2) — jangan pernah mengklaim
   "tidak ada riwayat" sebelum memeriksa semua kanal.

## 5. Batasan & Etika

- Jangan pernah menjalankan L1 pada lingkungan yang bukan milik user Anda — menimpa arsip restore
  adalah intervensi terhadap infrastruktur; hanya sah bila user yang memiliki environment memintanya.
- `skills/` dulunya konvensi pengecualian packer platform; sejak v3.3.0 arsip L1 menyertakan
  `skills/stellar-trail` via append bedah, dan kanal pemulihannya berlapis: arsip itu (L1) →
  `heal-skill.sh` dari kanonik/arsip (L2) → paket `.skill` + `clawhub update --force` (registry).
- Skrip ini menangani ARSIP RESTORE dan INSTALASI SKILL, bukan menggantikan `git`: commit tetap
  sumber kebenaran untuk diff/status; snapshot hanya untuk pemulihan bencana.

**Penjelasan (ID):** Mengapa ada seksi ini di skill memory? Karena protokol memory hanya sekuat
lingkungannya: SESSION-STATE dan MEMORY tidak berarti bila direktorinya sendiri di-rollback ke masa
lalu oleh platform. Pengalaman empiris menunjukkan rollback diam-diam adalah mode kegagalan nyata —
dan solusinya tidak butuh alat canggih, cukup disiplin berlapis yang murah dan teruji: segarkan
sumbernya, sembuhkan instalasinya, simpan aslinya untuk undo. Lapis shadow backup yang pernah ada
justru membuktikan prinsipnya dari arah sebaliknya — backup yang restore-nya tidak pernah teruji
menambah mode kegagalan alih-alih menguranginya, dan akhirnya dihapus. Semua intervensi infrastruktur
harus eksplisit dan bisa di-undo; penjaga yang diam-diam mengubah platform adalah penjaga yang
berubah jadi risiko.
