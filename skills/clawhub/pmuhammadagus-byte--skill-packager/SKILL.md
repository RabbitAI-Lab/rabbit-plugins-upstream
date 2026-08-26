---
name: openclaw-skill-packager
slug: openclaw-skill-packager
version: 1.2.0
description: "Gunakan saat memaketkan, memvalidasi, dan menyiapkan skill OpenClaw untuk backup, deploy, atau reuse lintas environment. Menjamin struktur valid, bebas secret, dan kompatibel platform (Termux/Android vs desktop)."
metadata:
  openclaw:
author: pmuhammadagus-byte
license: MIT

---




# OPENCLAW SKILL PACKAGER

Gunakan skill ini ketika:
- ingin memaketkan skill menjadi unit siap backup/deploy;
- ingin memastikan struktur skill valid sebelum dipindah ke environment lain;
- ingin menyiapkan skill untuk dibagikan atau dipakai ulang;
- ingin memeriksa apakah skill siap dipindah antar environment.

Jangan gunakan untuk:
- menjalankan skill yang ada;
- mengedit isi fungsional skill langsung;
- menggantikan backup seluruh workspace;
- operasi destruktif tanpa validasi.

---

## PURPOSE

Mengubah satu atau banyak skill OpenClaw menjadi paket terstruktur yang:
- valid;
- aman (bebas secret);
- mudah dipindah;
- siap backup/deploy/share;
- tidak mengandalkan asumsi platform yang salah.

---

## WHEN TO USE

- sebelum backup skill tertentu
- sebelum deploy skill ke environment lain
- sebelum membagikan skill ke orang lain
- sebelum migrasi workspace
- setelah membuat skill baru

## WHEN NOT TO USE

- jika hanya butuh backup seluruh workspace
- jika skill masih draft dan belum siap dipaketkan
- jika ingin menjalankan skill, bukan memaketkannya

---

## INPUT

Dapat berupa:
- path skill tunggal: `~/.openclaw/workspace/skills/<skill-name>`
- beberapa path skill
- path direktori `skills`
- bahan mentah skill untuk dipaketkan

Default:
- `SOURCE_DEFAULT = ~/.openclaw/workspace/skills`
- `OUTPUT_DEFAULT = ~/.openclaw/workspace/skills-packages`

---

## PACKAGE STRUCTURE

Setiap skill yang dipaketkan harus berbentuk:

```
<skill-name>/
  SKILL.md          # WAJIB
  assets/           # opsional
  scripts/          # opsional
  references/       # opsional
  examples/         # opsional
  templates/        # opsional
```

Aturan:
- `SKILL.md` wajib ada.
- direktori lain opsional.
- jangan memasukkan file sampah: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.log`, `node_modules/`, `.git/`.
- jangan memasukkan secret atau credential.

---

## WORKFLOW

### 1. Requirement Analysis
Tujuan: tahu skill mana yang akan dipaketkan dan untuk apa (backup / deploy / share). Konfirmasi tujuan & target platform jika belum jelas.

### 2. Input Validation
Cek secara fisik:
- path sumber ada (`test -d` / `test -f`)
- `SKILL.md` ada di root skill
- frontmatter valid: minimal ada `name` dan `description` (parse YAML frontmatter)
- tidak ada file sensitif: secret, token, key, credential

Jika ada masalah → laporkan ERROR, perbaiki bila aman, atau SKIP skill tersebut.

### 3. Structure Normalization
Bersihkan:
- file temporary / junk
- direktori kosong
- duplikasi struktur
- path tidak relevan

Jangan ubah isi `SKILL.md` kecuali:
- memperbaiki frontmatter yang rusak
- menghapus secret yang terdeteksi

### 4. Compatibility Check
Cek:
- tidak ada command fiktif
- tidak ada tool yang belum terverifikasi (`command -v`)
- tidak ada asumsi Linux desktop jika target Termux/Android (path `$PREFIX`, bukan `/usr`)

Jika ketidakcocokan ditemukan → laporkan WARNING + beri catatan platform-specific.

### 5. Packaging
Buat paket:
- salin struktur skill ke output directory
- nama konsisten: `<skill-name>-v<version>` jika ada versi, else nama skill
- gunakan `cp -r` (atau `rsync -a --exclude` bila tersedia)

Jangan:
- menambah metadata eksternal berlebihan
- menyertakan file tak dibutuhkan

### 6. Validation
Setelah paket dibuat, jalankan checklist VERIFICATION ENGINE (node 11):
- `SKILL.md` masih valid
- struktur direktori konsisten
- tidak ada secret baru muncul selama copy (`grep` ulang)
- ukuran paket wajar (`du -sh`)

### 7. Output Report
Lihat format di CONTOH NYATA (Output Report).

---

## EDGE CASES

- **Skill tanpa versi di frontmatter** → pakai nama skill saja, catat "NO VERSION".
- **Path mengandung spasi** → selalu quote: `cp -r "$SRC" "$DST"`.
- **Skill berisi symlink ke luar direktori** → jangan ikuti; salin hanya isi riil dalam batas skill (cegah kebocoran).
- **Banyak skill sekaligus** → proses per skill; satu gagal tidak menghentikan batch; tandai tiap status.
- **Target Termux tapi SKILL.md pakai path `/usr`** → WARNING, sarankan ganti ke `$PREFIX` / relatif.
- **File raksasa tak terduga (>5 MB)** → investigasi; mungkin asset sah atau secret terselip; jangan lanjut tanpa cek.

---

## COMMON MISTAKES / ANTI-PATTERNS

| Mistake | Fix |
|---------|-----|
| Memaketkan secret (`.env`, token di SKILL.md) | Jalankan `grep -rEi` sebelum copy; hapus jika ketemu |
| Menyertakan junk file | Exclude `.DS_Store`, `*.tmp`, `*.log`, `node_modules/`, `.git/` |
| `SKILL.md` invalid / frontmatter rusak | Validasi frontmatter dulu, perbaiki bila aman |
| Asumsi platform desktop di Termux | Cek `uname -s -m`; gunakan `$PREFIX` & path relatif |
| Mengubah isi fungsional SKILL.md saat packaging | Hanya ubah untuk perbaiki frontmatter/secret |
| Klaim sukses tanpa verify | Jalankan checklist node 11; jangan andalkan exit code saja |
| Memaketkan seluruh workspace | Skill ini untuk skill tertentu, bukan backup workspace |

---

## CONCRETE EXAMPLES (INPUT → OUTPUT)

**Contoh 1 — Paketkan satu skill bersih**
- Input: `"Paketkan skill openclaw-skill-packager"`
- Proses: validate → scan secret (0) → normalize → copy ke `skills-packages/openclaw-skill-packager-v1.2.0` → verify hijau.
- Output report:
```
PACKAGED SKILLS
- openclaw-skill-packager: OK
TOTAL: 1 packaged, 0 failed
OUTPUT: ~/.openclaw/workspace/skills-packages/openclaw-skill-packager-v1.2.0
SIZE: 24K
SECRET LEAK: OK
PLATFORM COMPATIBILITY: OK
```

**Contoh 2 — Skill mengandung secret**
- Input: `"Validasi skill X sebelum share"`
- Proses: scan secret ketemu `API_KEY=...` di `scripts/config.sh`.
- Tindakan: hapus file dari salinan + WARNING "SECRET REMOVED".
- Output report:
```
PACKAGED SKILLS
- X: OK (WARNING: secret removed from scripts/config.sh)
TOTAL: 1 packaged, 0 failed
SECRET LEAK: OK (remediated)
PLATFORM COMPATIBILITY: WARNING (assumes /usr)
```

**Contoh 3 — User salah minta jalankan skill**
- Input: `"Jalankan skill Y untuk saya"`
- Tindakan: TOLAK (negative trigger). "Skill packager hanya memaketkan, bukan menjalankan. Gunakan skill Y secara langsung."

---

## FAILURE MODES

| Mode Gagal | Penyebab | Deteksi | Pemulihan |
|------------|----------|---------|-----------|
| Copy gagal (I/O) | disk penuh / path salah | exit code ≠ 0 | retry; periksa `df`, quote path |
| Secret lolos ke paket | lupa scan / pola tak cocok | `grep` pasca-copy ≠ 0 | hapus file, rescan, WARNING |
| `SKILL.md` rusak | YAML frontmatter invalid | parse gagal | SKIP + laporkan; jangan tebak |
| Tool `rsync` absen | environment minimal | `command -v rsync` kosong | fallback `cp -r` |
| Path spasi putus | tidak di-quote | argumen terpisah | quote `"$SRC"` `"$DST"` |
| Platform mismatch | asumsi desktop di Termux | ada path `/usr` / systemd | WARNING + catatan `$PREFIX` |

---

## ERROR HANDLING

INPUT ERROR
→ Jelaskan path/format yang salah → Berikan contoh benar → Jangan lanjut jika kritis

DEPENDENCY ERROR
→ Laporkan tool/package hilang → Berikan fallback (`cp` jika `rsync` tiada)

TOOL ERROR
→ Laporkan pesan error → Jangan lanjut jika output tidak bisa dipercaya

OUTPUT ERROR
→ Laporkan path output tak bisa ditulis → Recovery: ganti path atau perbaiki permission

PERMISSION ERROR
→ Laporkan file/directory ditolak → Recovery: `chmod` atau jalankan dengan izin sesuai

ENVIRONMENT ERROR
→ Laporkan platform mismatch → Gunakan pendekatan konservatif (Termux-safe)

UNKNOWN ERROR
→ Laporkan ERROR → Jangan lanjut dengan asumsi → Minta klarifikasi user

---

## SECURITY

- Jangan masukkan secret ke dalam paket.
- Jangan cetak isi file sensitif.
- Jangan packaging file di luar direktori skill.
- Jangan jalankan command selama packaging kecuali validator statis yang aman.

---

## SELF-CHECK

Sebelum menyatakan packaging selesai:

- [ ] Input path divalidasi
- [ ] SKILL.md terverifikasi
- [ ] Struktur skill normal (tanpa junk)
- [ ] Tidak ada secret yang terdeteksi (grep = 0)
- [ ] Compatibility diperiksa
- [ ] Output dibuat dengan benar & bisa dibaca kembali
- [ ] Laporan diberikan

---

## QUALITY GATE

Target: skor ≥ 90 untuk production-ready.

Evaluasi:
- struktur paket benar
- tidak ada secret (grep = 0)
- tidak ada file tidak perlu
- compatibility jelas
- output bisa digunakan langsung

Jika di bawah 90 → perbaiki sebelum deploy/share.

---

## GOLDEN RULE

Paket harus bisa dipindah dan langsung dipakai.
Jangan packaging skill yang belum siap.
Utamakan validasi, keamanan, dan kebersihan struktur.

---

## RED FLAGS

- Secret dalam paket
- `SKILL.md` rusak
- Platform mismatch (desktop vs Termux)
- Paket tak divalidasi

---

## RATIONALIZATION PREVENTION

| Excuse | Reality |
|--------|---------|
| "Ini cuma backup" | Paket sering dibagikan. Jangan ada secret. |
| "Strukturnya sudah oke" | Validasi dulu, jangan asumsi. |
| "Nanti saya bersihkan" | Paket harus bersih sekarang. |

---

## QUICK REFERENCE

| Situasi | Aksi |
|---------|------|
| Publish / share | Package + scan secret + laporan |
| Validasi | Cek struktur + frontmatter |
| Install di env lain | Verifikasi paket dulu |
