---
name: coding-2
description: "Gunakan saat membangun dashboard HTML dinamis dari data API atau merancang schema database."
metadata:
  openclaw:
    version: 1.1.0
    author: pmuhammadagus-byte
    license: MIT
    maturity: stable
    quality: high
    tags: [coding, dashboard, api, database, html, realtime]
author: pmuhammadagus-byte
license: MIT

---

# coding-2 — X∞ Compliance Layer

## 1. IDENTITY
Skill milik user: `coding-2`. Mengikuti Skill Architecture Standard X∞ (wajib).

## 2. PURPOSE
Membangun dashboard HTML dinamis yang dibacking oleh data API: merancang skema DB dari data, mendesain backend API (generalDataApi), lalu merender chart yang masing-masing memanggil API sendiri dan mem-polling tiap 60 detik untuk update real-time.

## 3. METADATA
- name: coding-2
- version: 1.0.0
- standard: Skill Architecture Standard X∞ (21-node)
- scope: dashboard HTML dinamis + data API
- depends_on: tool DB (pembuatan skema), network API

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
**CHANGELOG**
- 1.0.0 — Perbaikan kualitas lapisan X∞: frontmatter `description` rusak (berisi teks changelog) diganti deskripsi trigger nyata; Node 2 (PURPOSE) & Node 3 (METADATA) diisi (bukan stub); `metadata.openclaw.version` ditambahkan. Konten domain (skema DB, generalDataApi, polling 60s, style_lint.py) dipertahankan.

## 19. COMPATIBILITY
Tahu OS/ARCH/RUNTIME/versi/tool/API tersedia.

## 20. KNOWLEDGE SOURCES
Trust hierarchy: OFFICIAL>PRIMARY>REPUTABLE>COMMUNITY>UNKNOWN. Tandai VERIFIED/LIKELY/UNCERTAIN/OUTDATED/CONFLICTING.

## 21. EXIT CONDITIONS
Berhenti pada: SUCCESS/FAILURE/BLOCKED/NEED USER/NEED CREDENTIAL/NEED TOOL/NEED VERIFICATION.
## When to Use

Use this skill when:
- Building a dynamic HTML dashboard that reads from a data API
- Designing database schema before frontend implementation
- Creating real-time updating charts with polling
- Working with the teamo-dev generalDataApi or similar endpoints

**Don't use when:** Simple static HTML or non-dashboard work.

# Coding

## Overview

This skill provides specialized capabilities for coding, focused on building a real-time HTML dashboard backed by a data API.

## Instructions

Buat dashboard HTML dinamis yang dibacking data API. Pendekatan umum:

1. **Rancang skema DB** dari data yang diterima, lalu buat struktur tersebut di database via tool yang tersedia.
2. **Rancang backend API** sesuai struktur DB. Gunakan endpoint milik user/organisasi sendiri — **jangan** menyambung ke host pihak ketiga yang tidak dikenal. Ganti `API_BASE_URL` dan kredensial dengan milik user, yang disetel lewat environment variable atau config eksplisit (mintalah ke user jika belum ada).
3. **Render chart**: tiap chart memanggil API sendiri, lalu polling tiap 60 detik untuk update real-time.
4. **Masukkan data** yang diberikan user ke struktur DB yang sudah dibuat — hanya data yang user berikan secara eksplisit, ke database yang user setujui.

> Keamanan: jangan kirim data user ke endpoint eksternal yang tidak dikonfirmasi. Selalu minta persetujuan user untuk target DB, nama collection, dan operasi tulis sebelum eksekusi.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Designing UI before DB schema | Design schema from data first |
| One API call for all charts | Each chart requests its own data |
| No polling | Set 60s interval for real-time updates |
| Hardcoding endpoint | Use the generalDataApi contract with session_group_id |

## Red Flags

- Building the dashboard without the DB schema
- Charts without their own API request
- Missing session_group_id in requests
- Static page instead of 60s polling updates

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "I'll skip the DB schema" | Schema drives the API design. |
| "One request is enough" | Each chart needs its own data fetch. |
| "Polling is overkill" | The spec requires real-time updates. |

## How to Use

1. **Get schema**: Read the DB schema to design the dashboard tables.
2. **Design**: Sketch the dashboard UI from the schema.
3. **Implement**: One API request per chart via generalDataApi with `session_group_id`.
4. **Poll**: Refresh at 60s intervals.

## Quick Reference / Workflow

1. **Design DB schema** — From the data you receive, design the table/collection structure, then call a tool to create it in the database.
2. **Backend API** — Gunakan endpoint milik user (`API_BASE_URL`). `method=POST`.
   - Request body contoh: `{"session_group_id":"<SESSION_GROUP_ID>", "collection_name":<nama_tabel>}`
   - Response diharapkan: `{"code":0, "result": {"data": [<JSON array>]}}`
3. **Build the dashboard** — Dynamic HTML; each chart calls the API once to render, then polls every **60s** to update live.
4. **Insert data** — Make sure the data given to you is inserted into the created DB structure.

## Examples (user says X → you do Y)

- "Make a live dashboard from this sales data" → design schema → create tables via DB tool → build HTML that hits `generalDataApi` per chart, 60s poll → insert the sales data.
- "Add a new chart for table `orders`" → add a chart component that POSTs `collection_name: "orders"` and re-renders on the 60s timer.

## Gotchas

- Substitute `API_BASE_URL`, `SESSION_GROUP_ID`, dan nama tabel at runtime via config/env milik user — jangan hardcode ke endpoint pihak ketiga yang tidak dikenal.
- Each chart must request the API **independently** (one call per chart), not share a single fetch.
- Poll interval is fixed at **60s**; don't shorten/extend without being asked.
- The response shape uses `result.data` as a JSON array — guard for `code !== 0` before rendering.

## Usage Notes

- This skill is based on the Coding agent configuration
- Template variables (if any) like $DATE$, $SESSION_GROUP_ID$ may require runtime substitution
- Follow the instructions and guidelines provided in the content above

## Toolkit / Files

- `scripts/style_lint.py` — checks an HTML/JS dashboard for the skill's conventions (independent fetch per chart, 60s poll, `code !== 0` guard, no leftover placeholders). Example:
  `python3 scripts/style_lint.py dashboard.html --require-poll 60000`
