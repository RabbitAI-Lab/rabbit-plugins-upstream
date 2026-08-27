---
name: termux-compat-runner
description: "Use when executing shell commands on Termux/Android: validate platform, choose safe commands, apply timeout/retry, and avoid Linux desktop assumptions."
metadata:
  openclaw:
    version: 1.1.0
---
<!-- ===== X∞ COMPLIANCE LAYER (auto-applied by skill-architecture-standard) ===== -->
## 1. IDENTITY
Skill milik user: `termux-compat-runner`. Mengikuti Skill Architecture Standard X∞ (wajib).

## 2. PURPOSE
Use when executing shell commands on Termux/Android: validate platform, choose safe commands, apply timeout/retry, and avoid Linux desktop assumptions.

## 3. METADATA
- name: termux-compat-runner
- version: 1.1.0
- owner: pmuhammadagus-byte

## 4. TRIGGER ENGINE
Aktif ketika user meminta hal yang cocok dengan deskripsi di atas.
Negative trigger: di luar scope deskripsi.

## 5. CONTEXT ENGINE
Baca OS/ARCH/runtime sebelum bertindak. Termux Android ARM64 ≠ Ubuntu x86_64.

## 6. DECISION POLICY
IF uncertainty → VERIFY
IF high risk → ASK/STOP
IF tool unavailable → ALTERNATIVE
IF action fails → RECOVER

## 7. REASONING POLICY
Evidence-first. Bedakan FAKTA vs HIPOTESIS. Confidence: CONFIRMED/LIKELY/POSSIBLE/UNKNOWN.

## 8. EXECUTION POLICY
Ambil tindakan relevan, lalu VERIFY. Jangan klaim sukses sebelum diverifikasi.

## 9. TOOL POLICY
Pilih tool berdasar kebutuhan+konteks. Jangan asal panggil semua tool.

## 10. MEMORY POLICY
Ingat hal relevan; abaikan noise. Retrieve saat dibutuhkan, update bila berubah.

## 11. VERIFICATION ENGINE
ACTION → VERIFY → SUCCESS? Jika tidak: DIAGNOSE → RETRY/CHANGE STRATEGY.

## 12. ERROR RECOVERY
transient→retry; timeout→backoff; auth→credential check; dependency→diagnosis; unknown→investigate.

## 13. SECURITY GUARDRAILS
NEVER log secret. REDACT API KEY/TOKEN/PASSWORD/SECRET sebelum simpan. PII: MINIMIZE→REDACT→HASH.

## 14. EVALUATION
Self-eval: capai goal? terverifikasi? ada asumsi? ada gagal? Kirim ke Agent Evaluation Engine.

## 15. OBSERVABILITY
Emit: START/PROGRESS/TOOL CALL/ERROR/RETRY/SUCCESS/FAILURE + TRACE_ID (tanpa secret).

## 16. PERFORMANCE OPTIMIZATION
FULL→OPTIMIZED→LOW RESOURCE mode bila terbatas. Prioritas: TASK>SAFETY>RELIABILITY.

## 17. SELF-IMPROVEMENT
USE→OBSERVE→EVALUATE→FIND WEAKNESS→IMPROVE→TEST→NEW VERSION (via evaluasi+regresi).

## 18. VERSIONING
Semver. Perubahan struktur = MAJOR. CHANGELOG wajib.

## 19. COMPATIBILITY
Tahu OS/ARCH/RUNTIME/versi/tool/API tersedia.

## 20. KNOWLEDGE SOURCES
Trust hierarchy: OFFICIAL>PRIMARY>REPUTABLE>COMMUNITY>UNKNOWN. Tandai VERIFIED/LIKELY/UNCERTAIN/OUTDATED/CONFLICTING.

## 21. EXIT CONDITIONS
Berhenti pada: SUCCESS/FAILURE/BLOCKED/NEED USER/NEED CREDENTIAL/NEED TOOL/NEED VERIFICATION.
<!-- ===== END X∞ COMPLIANCE LAYER ===== -->



# TERMUX COMPAT RUNNER

Gunakan skill ini ketika:
- menjalankan perintah shell di Termux/Android;
- perlu wrapper aman untuk eksekusi command dengan timeout dan retry;
- ingin menghindari asumsi Linux desktop;
- perlu fallback ketika tool/package tidak tersedia.

Jangan gunakan untuk:
- operasi destruktif tanpa validasi;
- menjalankan script yang belum diperiksa;
- menggantikan backup/restore script yang ada.

---

## QUICK REFERENCE / CHECKLIST

Sebelum menjalankan command di Termux/Android, ikuti:

- [ ] **Detect platform** — `com.termux` di `$PREFIX`/`$HOME` → TERMUX; `uname` untuk Linux/Mac.
- [ ] **Check tool** — `command -v <tool>`; `pkg list-installed` untuk package; `uname -m` arsitektur.
- [ ] **Set timeout** — cepat 15s / menengah 60s / berat 180s.
- [ ] **Run → check exit** — sukses: verifikasi output; gagal: retry max 2x lalu fallback.
- [ ] **Avoid desktop-isms** — jangan `systemctl`, `/usr/local`, glibc-only bin tanpa fallback.
- [ ] **Security gate** — destruktif? CHECK → CONFIRM TARGET → EXECUTE → VERIFY. Jangan cetak secret.

**Examples (user says X → you do Y)**
- "Jalankan `pkg update`" → `command -v pkg` ada → jalankan dengan timeout 60s → laporkan EXIT CODE + OUTPUT.
- "Cek port 8080" → `command -v ss`? ya pakai `ss`; tidak → `netstat`/`/proc/net/tcp` fallback.
- "Hapus folder lama" → DESTRUKTIF → minta konfirmasi target eksplisit dulu, jangan langsung hapus.
- "Setup storage" → sarankan `termux-setup-storage` & cek permission sebelum akses file eksternal.

**Gotchas**
- Jangan asumsikan Linux desktop: `systemctl`, `/usr/local`, glibc-only sering tidak ada di Termux.
- Jangan infinite retry; batasi 2x lalu fallback/stop.
- Jangan cetak secret/credential ke output.
- Kalau tool absen, cari fallback atau laporkan ERROR — jangan lanjut dengan asumsi.

---

## PURPOSE

Menyediakan cara aman dan konsisten menjalankan perintah di Termux/Android tanpa asumsi Linux desktop.

---

## WHEN TO USE

- sebelum menjalankan command di Termux
- ketika tidak yakin apakah tool tersedia
- ketika butuh timeout/retry/fallback
- ketika ada batasan permission atau storage

## WHEN NOT TO USE

- jika sudah ada skill khusus untuk tugas tersebut
- jika command sudah diverifikasi dan aman tanpa wrapper
- jika environment bukan Termux dan bukan memerlukan kompatibilitas ini

---

## REQUIREMENTS

- `bash` tersedia
- `termux-setup-storage` sudah dijalankan jika butuh akses storage
- Permission storage sudah diberikan jika butuh akses file eksternal

Jika tidak terpenuhi, laporkan dan minta izin/user action.

---

## PLATFORM DETECTION

IF `$PREFIX` contains `com.termux` OR `$HOME` contains `com.termux`:
  PLATFORM = TERMUX
ELSE IF `uname -s` = `Linux` AND `uname -m` = `x86_64`:
  PLATFORM = LINUX_DESKTOP
ELSE IF `uname -s` = `Darwin`:
  PLATFORM = MACOS
ELSE:
  PLATFORM = UNKNOWN

Catat platform sebelum memilih command strategy.

---

## TOOL AVAILABILITY CHECK

Sebelum menjalankan command, cek ketersediaan tool:

CHECKLIST:
- `command -v <tool>` untuk tool umum
- `pkg list-installed` atau `dpkg -l` untuk package Termux
- `uname -m` untuk arsitektur
- `$PREFIX` untuk path environment

Jika tool tidak ada:
- cari fallback
- jika tidak ada fallback, laporkan ERROR dan hentikan

---

## EXECUTION RULES

Gunakan pendekatan bertingkat:

PRIMARY COMMAND
 ↓
CHECK EXIT CODE
 ↓
IF SUCCESS
  VERIFY OUTPUT
  REPORT RESULT
ELSE
  SAFE RETRY max 2x
 ↓
IF STILL FAILED
  USE FALLBACK
 ↓
IF FALLBACK FAILED
  STOP
  REPORT ERROR

Aturan:
- batasi durasi dengan timeout
- jangan infinite retry
- jangan lanjut jika output tidak valid
- jangan abaikan error code

---

## TIMEOUT POLICY

Default timeout:
- command cepat: 15 detik
- command menengah: 60 detik
- command berat: 180 detik

Jika exceed timeout:
- laporkan TIMEOUT
- hentikan proses
- gunakan fallback atau minta user action

---

## COMMAND COMPATIBILITY

Jangan gunakan command yangKnown tidak kompatibel dengan Termux:

HINDARI:
- `systemctl` / systemd commands
- `/usr/local/...` paths
- desktop-only binaries tanpa fallback
- command yang membutuhkan glibc jika belum terverifikasi

Gunakan alternatif Termux:
- `pkg` untuk package management
- `termux-services` jika dibutuhkan service
- `termux-setup-storage` untuk storage access
- path `$HOME` atau `$PREFIX` untuk direktori

---

## ERROR HANDLING

INPUT ERROR
→ Jelaskan format command yang salah
→ Berikan contoh command yang benar
→ Jangan lanjut tanpa konfirmasi jika kritis

DEPENDENCY ERROR
→ Laporkan package/tool yang hilang
→ Berikan cara install: `pkg install <package>`
→ Gunakan fallback jika ada

TOOL ERROR
→ Laporkan pesan error dari tool
→ Jangan lanjut jika output tidak bisa dipercaya

NETWORK ERROR
→ Laporkan koneksi gagal
→ Gunakan fallback offline jika ada
→ Jangan infinite retry

TIMEOUT
→ Laporkan durasi yang exceeded
→ Gunakan fallback atau perintah lebih ringkas

PERMISSION ERROR
→ Laporkan path/operation yang ditolak
→ Berikan recovery: permission request atau alternatif path

ENVIRONMENT ERROR
→ Laporkan platform mismatch
→ Gunakan solusi sesuai Termux/Android

OUTPUT ERROR
→ Laporkan output yang tidak sesuai ekspektasi
→ Validasi ulang atau repair

UNKNOWN ERROR
→ Tangkap exception
→ Laporkan dengan jelas
→ Jangan lanjut dengan asumsi

---

## SECURITY

- Jangan jalankan command destruktif tanpa validasi
- Jangan mencetak secret atau credential
- Jangan menghapus file penting tanpa konfirmasi
- Jangan eksekusi script yang belum diperiksa

Untuk operasi berisiko:
CHECK → CONFIRM TARGET → EXECUTE → VERIFY

---

## OUTPUT FORMAT

Setiap eksekusi, laporkan:

COMMAND: <command yang dijalankan>
PLATFORM: TERMUX / LINUX_DESKTOP / MACOS / UNKNOWN
EXIT CODE: <code>
RESULT: SUCCESS / FAILED / TIMEOUT / ERROR
OUTPUT: <output ringkas>
NEXT ACTION: <lanjut/retry/fallback/stop>

---

## SELF-CHECK

Sebelum menyatakan eksekusi selesai:

[ ] Platform terdeteksi
[ ] Tool availability tercek
[ ] Timeout ditetapkan
[ ] Error handling tersedia
[ ] Fallback disiapkan
[ ] Tidak ada command destruktif tanpa validasi
[ ] Output diverifikasi
[ ] Tidak ada secret yang tercetak

---

## QUALITY GATE

Target: 90+ untuk production-ready.

Evaluasi:
- compatibility dengan Termux/Android
- reliability saat tool gagal
- clarity instruksi
- error handling coverage
- security
- maintainability

Jika di bawah 90: perbaiki sebelum digunakan.

---

## GOLDEN RULE

Jangan asumsikan Linux desktop.
Jalankan command seolah-olah environment bisa berubah kapan saja.
Utamakan compatibility, safety, dan verifikasi.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Linux-only commands | Use Termux-compatible alternatives |
| Ignoring Android limits | Respect process/background limits |
| Hardcoded desktop paths | Use PREFIX/HOME dynamically |
| No error capture | Capture stderr for diagnosis |

## Red Flags

- Command that doesn't exist on Termux
- Desktop path assumptions
- Ignoring Android process limits
- No failure diagnostics

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "It's bash, it'll work" | Termux differs. Test. |
| "I'll handle errors later" | Capture errors now. |
| "The path is standard" | Verify per-environment. |

## How to Use

1. **Validate platform**: Confirm Termux/Android context.
2. **Choose safe commands**: Termux-compatible alternatives.
3. **Execute**: Apply timeout/retry guards.
4. **Diagnose**: Capture stderr for failures.

## Toolkit / Files

- `scripts/run_safe.sh` — validates a command against a safe allowlist and prints the dry-run it WOULD run; it never executes anything. Example:
  `bash scripts/run_safe.sh "ss -tulpen" --timeout 60`
