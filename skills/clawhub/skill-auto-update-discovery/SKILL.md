---
name: openclaw-skill-auto-update-discovery
description: "Engine auto-update & discovery skill OpenClaw: scan, evaluate, update, test, install, verify, rollback — dengan validation gate dan safety agar update tidak merusak workspace."
metadata:
  openclaw:
author: pmuhammadagus-byte
license: MIT

---



## Edge Cases
- **ClawHub CLI tidak tersedia** → fallback `git` + `web_fetch`; laporkan tool hilang, jangan gagal diam.
- **Workspace di Termux vs desktop** → path & binary beda; jangan copy skill bawaan (`npm-global`).
- **Skill punya dependency tool yang tak ada** → BLOCK, jangan install parsial.
- **Dua skill dengan capability identik** → ranking by Quality Score + Relevance, pilih 1, disable duplikat (bukan hapus).
- **Update mayor dgn migration** → PENDING REVIEW, jangan auto-apply.
- **Rollback tapi backup rusak** → ESCALATE ke user, jangan asumsi versi aman.

## Concrete Examples
- **Input:** "Cek update buat trading-analyst." → **Output:** scan `_meta.json` (v1.0.0), `clawhub` latest (v1.1.0), baca changelog (fix RSI), security scan PASS, compat PASS → lapor "update v1.0.0→v1.1.0 tersedia, low risk" → tunggu approval / auto-update bila gate lolos → backup → apply → post-install test (trigger "analisa gold" respon) → VERIFY PASS → report.
- **Input:** "Cari skill buat screenshot web di Android." → **Output:** discover by capability "screenshot/web/android" → temukan 2 kandidat → Quality Score (A=82, B=54) → eval B (obfuscated install script) → BLOCK B → rekomendasikan A, minta approval install.
- **Input:** "Skill brain-core-ultra error load." → **Output:** detect broken → diagnose (JSON corrupt di `_meta.json`) → cek latest source → patch/copy bersih → post-install test → jika gagal → ROLLBACK ke backup → report.

## Failure Modes
- **Auto-update buta** → break agent. FIX: validasi gate wajib sebelum apply.
- **Version conflict tak diresolve** → skill saling timpa. FIX: prioritas + PENDING REVIEW.
- **Tanpa rollback** → rusak permanen. FIX: backup old version tiap update penting.
- **Update saat agent aktif pakai skill** → race condition. FIX: jangan update skill sedang dipakai, atau queue.
- **Hallucinate "installed"** → laporan bohong. FIX: anti-hallucination, verify dulu.
- **Bloat** (10 skill sama) → resource habis. FIX: anti-bloat, pilih 1 terkuat.

## Common Mistakes
| Mistake | Fix |
|---------|-----|
| Auto-updating without validation | Validate before applying |
| Version conflicts | Resolve priorities |
| No rollback | Keep previous versions |
| Updating broken skills | Detect and skip broken updates |

## Red Flags
- Applying untested updates
- Ignoring version conflicts
- No rollback capability
- Updating during active use

## Rationalization Prevention
| Excuse | Reality |
|--------|---------|
| "Updates are safe" | Validate each. |
| "Latest wins" | Resolve conflicts. |
| "I'll rollback if needed" | Have rollback ready. |

## How to Use
1. **Scan**: Discover skills and available updates.
2. **Evaluate**: Assess version conflicts and compatibility.
3. **Update**: Apply with validation gates.
4. **Verify**: Test post-update; rollback if broken.

## Quick Reference
| Situasi | Aksi |
|---------|------|
| Cek update skill | Jalankan discovery |
| Update tersedia | Validasi sebelum apply |
| Versi bentrok | Resolve prioritas |
| Auto-update gagal | Rollback aman |
| Selesai update | Verifikasi berfungsi |
