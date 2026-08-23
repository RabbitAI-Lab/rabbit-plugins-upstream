---
name: taizi-coding
description: "changelog: Improve discoverability, add homepage and feedback section"
metadata:
  openclaw:
    homepage: description: Coding style memory that adapts to your preferences, conventions, and patterns for consistent coding.
    version: homepage: https://clawic.com/skills/coding
---

<!-- ===== X∞ COMPLIANCE LAYER (auto-applied by skill-architecture-standard) ===== -->
# taizi-coding — X∞ Compliance Layer

## 1. IDENTITY
Skill milik user: `taizi-coding`. Mengikuti Skill Architecture Standard X∞ (wajib).

## 2. PURPOSE
changelog: Improve discoverability, add homepage and feedback section

## 3. METADATA
- version: homepage: https://clawic.com/skills/coding
- homepage: description: Coding style memory that adapts to your preferences, conventions, and patterns for consistent coding.
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

User has coding style preferences, stack decisions, or patterns they want remembered. Agent learns ONLY from explicit corrections and confirmations, never from observation.

## Architecture

Memory lives in `~/coding/` with tiered structure. See `memory-template.md` for setup.

```
~/coding/
├── memory.md      # Active preferences (≤100 lines)
└── history.md     # Archived old preferences
```

## Quick Reference

| Topic | File |
|-------|------|
| Categories of preferences | `dimensions.md` |
| When to add preferences | `criteria.md` |
| Memory templates | `memory-template.md` |

## Data Storage

All data stored in `~/coding/`. Create on first use:
```bash
mkdir -p ~/coding
```

## Scope

This skill ONLY:
- Learns from explicit user corrections ("I prefer X over Y")
- Stores preferences in local files (`~/coding/`)
- Applies stored preferences to code output

This skill NEVER:
- Reads project files to infer preferences
- Observes coding patterns without consent
- Makes network requests
- Reads files outside `~/coding/`
- Modifies its own SKILL.md

## Core Rules

### 1. Learn from Explicit Feedback Only
- User corrects output → ask: "Should I remember this preference?"
- User confirms → add to `~/coding/memory.md`
- Never infer from silence or observation

### 2. Confirmation Required
No preference is stored without explicit user confirmation:
- "Actually, I prefer X" → "Should I remember: prefer X?"
- User says yes → store
- User says no → don't store, don't ask again

### 3. Ultra-Compact Format
Keep each entry 5 words max:
- `python: prefer 3.11+`
- `naming: snake_case for files`
- `tests: colocated, not separate folder`

### 4. Category Organization
Group by type (see `dimensions.md`):
- **Stack** — frameworks, databases, tools
- **Style** — naming, formatting, comments
- **Structure** — folders, tests, configs
- **Never** — explicitly rejected patterns

### 5. Memory Limits
- memory.md ≤100 lines
- When full → archive old patterns to history.md
- Merge similar entries: "no Prettier" + "no ESLint" → "minimal tooling"

### 6. On Session Start
1. Load `~/coding/memory.md` if exists
2. Apply stored preferences to responses
3. If no file exists, start with no assumptions

### 7. Query Support
User can ask:
- "Show my coding preferences" → display memory.md
- "Forget X" → remove from memory
- "What do you know about my Python style?" → show relevant entries

## Common Traps

- Adding preferences without confirmation → user loses trust
- Inferring from project structure → privacy violation
- Exceeding 100 lines → context bloat
- Vague entries ("good code") → useless, be specific

## Security & Privacy

**Data that stays local:**
- All preferences stored in `~/coding/`
- No telemetry or analytics

**This skill does NOT:**
- Send data externally
- Access files outside `~/coding/`
- Observe without explicit user input

## Feedback

- If useful: `clawhub star coding`
- Stay updated: `clawhub sync`
