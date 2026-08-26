---
name: openclaw-skill-generator
description: "Gunakan skill ini saat: user memberikan ide, catatan, atau workflow yang belum terstruktur dan meminta dibuat jadi; user ingin membuat skill OpenClaw baru dari bahan mentah;; user memiliki masalah/cara kerja yang berulang dan ingin dijadikan kemampuan agent yang bi. Aktif untuk tugas terkait openclaw-skill-generator."
metadata:
  openclaw:
    version: 1.0.0
author: pmuhammadagus-byte
license: MIT

---




# OPENCLAW WRITING SKILL GENERATOR

## When to Use

Gunakan skill ini ketika:
- user memberikan ide, catatan, atau workflow yang belum terstruktur dan meminta dibuat jadi skill;
- user ingin membuat skill OpenClaw baru dari bahan mentah;
- user memiliki masalah/cara kerja yang berulang dan ingin dijadikan kemampuan agent yang bisa digunakan kembali;
- user meminta "buat skill dari ini" meskipun bahan masih berantakan;
- user ingin standarisasi cara kerja menjadi SKILL.md yang valid.

Jangan gunakan untuk:
- mengedit skill yang sudah ada (gunakan editor langsung);
- debugging skill yang sudah ada (gunakan systematic-debugging);
- menjalankan skill yang sudah ada;
- operasi destruktif tanpa validasi.

---

## PURPOSE

Menerima bahan mentah dari user dan mengubahnya menjadi SKILL.md OpenClaw yang:
- valid;
- dapat dieksekusi agent;
- memiliki trigger, input, output, workflow, error handling, dan recovery yang jelas;
- sesuai environment yang digunakan (Termux/Android-aware);
- tidak mengarang fakta teknis;
- siap dipakai berulang kali.

---

## RAW MATERIAL TYPES

Bahan dari user bisa berupa:
- ide atau konsep singkat;
- catatan acak;
- urutan command yang sering dijalankan;
- workflow yang sudah ada tapi belum terstruktur;
- kode atau snippet;
- URL atau referensi;
- masalah beserta solusi yang belum terorganisir;
- pengalaman yang ingin dijadikan standar;
- gabungan dari semua di atas.

---

## ANALYSIS FRAMEWORK

Untuk setiap bahan, ekstrak jawaban untuk:

WHAT
Apa yang sebenarnya ingin dilakukan?

WHY
Mengapa skill ini dibutuhkan? Apa nilainya?

WHEN
Kapan skill harus diaktifkan?

WHEN NOT
Kapan skill tidak boleh digunakan?

INPUT
Apa yang diterima skill?

PROCESS
Apa langkah-langkah yang harus dilakukan?

TOOLS
Tool mana saja yang dibutuhkan?

OUTPUT
Apa hasil akhir yang diharapkan?

CONSTRAINT
Apa batasan yang harus dihormati?

FAILURE
Apa yang bisa gagal dan bagaimana recovery?

Jika informasi tidak ada di bahan:
- buat asumsi yang masuk akal;
- tandai sebagai ASSUMPTION;
- jangan perlakukan asumsi sebagai fakta.

---

## SKILL ARCHITECTURE

Setiap skill yang dihasilkan harus memiliki struktur konseptual ini:

SKILL
├── Identity
│   ├── name
│   ├── description
│   └── trigger conditions
├── Purpose
├── When to Use
├── When NOT to Use
├── Requirements
├── Inputs
├── Workflow
│   ├── Phase 1 — Analysis
│   ├── Phase 2 — Design
│   ├── Phase 3 — Implementation
│   ├── Phase 4 — Validation
│   ├── Phase 5 — Hardening
│   └── Phase 6 — Finalization
├── Decision Logic
│   └── IF/ELSE rules
├── Tool Usage
│   └── Available tools and fallbacks
├── Execution Rules
├── Validation
│   ├── Self-check checklist
│   └── Quality gate
├── Error Handling
│   ├── Error categories
│   ├── Recovery flow
│   └── Retry policy
├── Security
│   └── Secret handling
├── Output Rules
│   └── Final response format
└── Examples
    └── Normal/failure/edge cases

Tidak semua bagian harus diisi.
Saring bagian yang relevan. Jangan mengisi bagian hanya agar skill terlihat panjang.

---

## PLATFORM AWARENESS

Sebelum menentukan implementasi, deteksi environment:

IF `$PREFIX` contains `com.termux` OR `$HOME` contains `com.termux`:
  PLATFORM = TERMUX
  RULES:
  - Jangan asumsikan systemd
  - Jangan asumsikan path `/usr/local/...`
  - Jangan asumsikan desktop Linux tools tersedia
  - Prioritaskan tool yang tersedia di Termux package manager
  - Perhatikan ARM64 architecture
  - Perhatikan permission dan storage restrictions
  - Background process memiliki keterbatasan

ELSE IF `uname -s` = `Linux` AND `uname -m` = `x86_64`:
  PLATFORM = LINUX_DESKTOP
  RULES:
  - Tool desktop biasanya tersedia
  - Path lebih fleksibel
  - Systemd mungkin tersedia

ELSE IF `uname -s` = `Darwin`:
  PLATFORM = MACOS
  RULES:
  - Gunakan tool macOS-native
  - Perhatikan perbedaan command

ELSE:
  PLATFORM = UNKNOWN
  RULES:
  - Gunakan pendekatan konservatif
  - Validasi tool sebelum digunakan

Jangan memindahkan solusi Linux desktop ke Termux tanpa pemeriksaan.

---

## TOOL AWARENESS

Sebelum menentukan implementasi, verifikasi tool yang tersedia:

CHECK:
- `exec` untuk shell commands
- `read` untuk file reading
- `write` untuk file writing
- `edit` untuk file editing
- `web_fetch` untuk URL fetching
- `web_search` untuk web search
- `memory_search` untuk memory recall
- `cron` untuk scheduling
- `message` untuk messaging

Jangan menggunakan tool yang tidak tersedia.
Jika tool tidak tersedia, berikan fallback atau laporkan ERROR.

---

## NO FABRICATION RULES

DILARANG mengarang:
- command yang belum diverifikasi
- API yang belum ada
- tool yang belum tersedia
- path yang tidak valid
- package yang tidak terinstall
- environment variable yang tidak ada
- kemampuan platform yang tidak ada
- hasil eksekusi yang belum dilakukan

Jika informasi tidak diketahui:
- tandai sebagai UNKNOWN atau ASSUMPTION
- berikan cara verifikasi
- jangan perlakukan sebagai fakta

PRIORITAS:
REAL DATA > VERIFIED CONFIGURATION > DOCUMENTED ASSUMPTION > SAFE DEFAULT

---

## ERROR HANDLING

Kategorikan error:

INPUT ERROR
→ Jelaskan format yang salah
→ Berikan contoh yang benar
→ Jangan lanjut tanpa konfirmasi jika kritis

DEPENDENCY ERROR
→ Laporkan tool/package yang hilang
→ Berikan cara install
→ Gunakan fallback jika ada

TOOL ERROR
→ Laporkan pesan error dari tool
→ Jangan lanjut jika output tidak bisa dipercaya

NETWORK ERROR
→ Laporkan koneksi gagal
→ Gunakan fallback offline jika ada
→ Jangan infinite retry

AUTH ERROR
→ Laporkan credential masalah
→ Jangan mencoba retry auth tanpa perubahan

TIMEOUT
→ Laporkan durasi yang exceeded
→ Gunakan fallback atau perintah lebih ringkas

PERMISSION ERROR
→ Laporkan path/operation yang ditolak
→ Berikan recovery: chmod, sudo, atau alternatif

ENVIRONMENT ERROR
→ Laporkan platform mismatch
→ Gunakan solusi yang sesuai platform

OUTPUT ERROR
→ Laporkan output yang tidak sesuai ekspektasi
→ Validasi ulang atau repair

UNKNOWN ERROR
→ Tangkap exception
→ Laporkan dengan jelas
→ Jangan lanjut dengan asumsi

Untuk setiap error:
DETECT → EXPLAIN → RECOVER → RETRY/FALLBACK → VERIFY → REPORT

---

## RETRY & FALLBACK

Gunakan retry secara cerdas:

PRIMARY METHOD
 ↓
FAILED?
 ↓
SAFE RETRY max 2x dengan timeout
 ↓
FAILED?
 ↓
FALLBACK method
 ↓
FAILED?
 ↓
STOP
REPORT ERROR

Aturan:
- Jangan retry tanpa batas
- Jangan retry setelah operasi destruktif
- Jangan lanjut jika validator gagal dengan ERROR kritis
- Gunakan exponential backoff jika relevan

---

## SECURITY

Skill tidak boleh:
- membocorkan secret
- menampilkan API key/token/password
- menyimpan credential sembarang
- menjalankan command berbahaya tanpa validasi
- menghapus file penting tanpa konfirmasi
- melakukan operasi destruktif tanpa pemeriksaan

Untuk operasi berisiko:
CHECK → CONFIRM TARGET → EXECUTE → VERIFY

Gunakan placeholder untuk credential:
- `TELEGRAM_BOT_TOKEN`
- `OPENAI_API_KEY`
- `GITHUB_TOKEN`
- `GROQ_API_KEY`

Jangan memasukkan secret nyata ke dalam SKILL.md.

---

## SELF-VERIFICATION

Sebelum menyatakan skill selesai, verifikasi:

DID IT ACTUALLY WORK?

Bedakan:
- COMMAND EXECUTED (command berhasil dijalankan)
- TASK SUCCESSFULLY COMPLETED (hasil benar-benar sesuai)

Jika memungkinkan, verifikasi output secara nyata.

---

## QUALITY GATE

Nilai skill yang dihasilkan:

Architecture: alur skill logis dan tidak terputus?
Reliability: tetap berjalan jika sebagian tool gagal?
Clarity: instruksi jelas untuk agent?
Tool Usage: hanya pakai tool yang tersedia?
Error Handling: semua error tercover?
Security: aman dari secret exposure?
Compatibility: sesuai Termux/Android/desktop?
Maintainability: mudah diperbarui?
Extensibility: mudah menambah fitur?
Verification: agent bisa mempercayai hasil?

Target: minimal 90 untuk production-ready.

Jika di bawah 90: perbaiki skill sebelum final.

---

## SKILL SCORING

0–49 = INCOMPLETE
50–69 = BASIC
70–79 = GOOD
80–89 = ADVANCED
90–95 = PROFESSIONAL
96–100 = MASTER / PRODUCTION-GRADE

---

## OUTPUT FORMAT

Setelah membuat skill, berikan:

STATUS: PRODUCTION-READY / NEEDS IMPROVEMENT
PLATFORM: TERMUX / LINUX_DESKTOP / MACOS / UNKNOWN
SCORE: 0-100

SUMMARY:
- Ringkasan skill yang dibuat

SKILL STRUCTURE:
- Daftar bagian yang diisi

DECISIONS:
- Asumsi yang dibuat (jika ada)
- Alasan pemilihan tools
- Platform-specific choices

VALIDATION:
- Checklist yang terpenuhi
- Checklist yang belum terpenuhi (jika ada)

RECOVERY NOTES:
- Bagaimana jika skill gagal
- Fallback yang tersedia

NEXT STEPS:
- Apa yang perlu dilakukan user selanjutnya
- Bagaimana menguji skill
- Bagaimana mengembangkan skill lebih lanjut

---

## SKILL WRITING WORKFLOW

PHASE 1 — REQUIREMENT ANALYSIS
↓
Pahami WHAT/WHY/WHEN/INPUT/PROCESS/OUTPUT/CONSTRAINT/FAILURE

PHASE 2 — ENVIRONMENT ANALYSIS
↓
Deteksi platform dan verifikasi tools

PHASE 3 — ARCHITECTURE
↓
Buat struktur skill sesuai konteks

PHASE 4 — IMPLEMENTATION
↓
Tulis SKILL.md

PHASE 5 — VALIDATION
↓
Cek konsistensi, trigger, error handling

PHASE 6 — HARDENING
↓
Tambahkan fallback, security, platform-aware rules

PHASE 7 — SELF-TEST
↓
Simulasikan normal, failure, edge case

PHASE 8 — FINALIZATION
↓
Berikan output format lengkap

---

## MODE AUTOMATIC ENGINEERING

Jika requirement ambigu tapi masih dapat disimpulkan secara aman:
- jangan berhenti untuk bertanya
- buat asumsi yang masuk akal
- tandai sebagai ASSUMPTION
- lanjutkan implementasi

Namun jika ambiguity dapat menyebabkan:
- kehilangan data
- kerusakan sistem
- credential exposure
- operasi destruktif
- konsekuensi besar

maka gunakan SAFE-STOP dan laporkan kebutuhan klarifikasi.

---

## GOLDEN RULE

Jangan menulis skill seperti dokumentasi.
Tulis skill seperti membangun:

«OTAK OPERASIONAL UNTUK AGENT OPENCLAW.»

Skill harus membuat agent mampu:

MEMAHAMI
↓
MEMILIH
↓
BERTINDAK
↓
MEMERIKSA
↓
MEMPERBAIKI
↓
MENYELESAIKAN

Bukan hanya menerima input dan mengeluarkan jawaban.

---

## FINAL COMMAND

Setiap kali user memberikan bahan mentah:

ANALYZE
→ EXTRACT
→ STRUCTURE
→ ENHANCE
→ IMPLEMENT
→ VERIFY
→ HARDEN
→ SELF-TEST
→ FINALIZE

Kemudian hasilkan skill OpenClaw terbaik yang dapat dibangun dari bahan tersebut, tanpa mengarang fakta teknis yang tidak tersedia.

Bahan mentah boleh berantakan. Tugasmu adalah membuatnya menjadi skill yang luar biasa.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Incomplete frontmatter | Include name + description minimum |
| No validation | Validate before deploy |
| Non-standard structure | Follow ClawHub conventions |
| No testing | Test the generated skill |

## Red Flags

- Missing frontmatter fields
- Non-standard skill structure
- No validation step
- Generated skill untested

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "I'll fill metadata later" | Fill it now. |
| "This structure is fine" | Follow the standard. |
| "No time to test" | Deploying untested = broken. |

## How to Use

1. **Gather**: Collect raw ideas/notes/workflows from the user.
2. **Structure**: Transform into a valid SKILL.md.
3. **Validate**: Check frontmatter, structure, and conventions.
4. **Deploy**: Save to workspace and verify it loads.

See SKILL WRITING WORKFLOW for the full procedure.

## Quick Reference

| Situasi | Aksi |
|---------|------|
| Butuh skill baru | Generate dari template |
| Struktur skill | Ikuti ClawHub standar |
| Validasi skill | Cek frontmatter + konten |
| Skill tidak jalan | Debug struktur |
| Publikasi | Package + dokumentasi |
