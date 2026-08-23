---
name: coding-2
description: "changelog: ClawHub professional standard: Overview, When to Use, How to Use, Common Mistakes, Red Flags, Rationalizations, Quick Reference"
metadata:
  openclaw:
    homepage: description: "Use when building a dynamic HTML dashboard that reads from the teamo-dev generalDataApi and stores provided data into a designed DB schema.
    version: homepage: https://github.com/pmuhammadagus-byte/openclaw-settings
---

<!-- ===== X∞ COMPLIANCE LAYER (auto-applied by skill-architecture-standard) ===== -->
# coding-2 — X∞ Compliance Layer

## 1. IDENTITY
Skill milik user: `coding-2`. Mengikuti Skill Architecture Standard X∞ (wajib).

## 2. PURPOSE
changelog: ClawHub professional standard: Overview, When to Use, How to Use, Common Mistakes, Red Flags, Rationalizations, Quick Reference

## 3. METADATA
- version: homepage: https://github.com/pmuhammadagus-byte/openclaw-settings
- homepage: description: "Use when building a dynamic HTML dashboard that reads from the teamo-dev generalDataApi and stores provided data into a designed DB schema.
- (lihat frontmatter di atas)

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

1. 创建网页需要先根据拿到的数据设计数据库结构，需要调用工具在数据库中建立结构。 2.后端接口设计需要考虑现有的数据库结构，接口地址为：https://teamo-dev.floatai.cn/api/engine/generalDataApi，method="post"，入参为{"session_group_id":"$SESSION_GROUP_ID$", "collection_name":${表名}}，返回值为{"code":0, "result": {"data": ${JSON数组}}} 基于上边的接口和字段设计，开发动态html看板。 要求每个图表各自请求一次接口完成渲染，间隔60S轮训接口，实时更新页面。3. 注意将传给你的数据信息插入到创建好的数据库结构中。

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
2. **Backend API** — Endpoint `https://teamo-dev.floatai.cn/api/engine/generalDataApi`, `method=POST`.
   - Request body: `{"session_group_id":"$SESSION_GROUP_ID$", "collection_name":<表名>}`
   - Response: `{"code":0, "result": {"data": [<JSON数组>]}}`
3. **Build the dashboard** — Dynamic HTML; each chart calls the API once to render, then polls every **60s** to update live.
4. **Insert data** — Make sure the data given to you is inserted into the created DB structure.

## Examples (user says X → you do Y)

- "Make a live dashboard from this sales data" → design schema → create tables via DB tool → build HTML that hits `generalDataApi` per chart, 60s poll → insert the sales data.
- "Add a new chart for table `orders`" → add a chart component that POSTs `collection_name: "orders"` and re-renders on the 60s timer.

## Gotchas

- Substitute `$SESSION_GROUP_ID$` and `${表名}` at runtime — never hardcode placeholder strings into the final request.
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
