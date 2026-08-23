---
name: skill-architecture-standard
description: "MANDATORY OpenClaw skill architecture standard (X∞). Load this whenever creating, reviewing, or upgrading ANY agent skill. Enforces a 21-node structure (Identity, Purpose, Metadata, Trigger Engine, Context Engine, Decision Policy, Reasoning Policy, Execution Policy, Tool Policy, Memory Policy, Verification Engine, Error Recovery, Security Guardrails, Evaluation, Observability, Performance Optimization, Self-Improvement, Versioning, Compatibility, Knowledge Sources, Exit Conditions) plus 15 core principles: trigger intelligence, context awareness, decision IF/THEN, verification engine, recovery strategy, risk classification, tool selection, knowledge hierarchy, self-evaluation, observability hooks, memory policy, self-improvement loop, compatibility, resource awareness, exit conditions. Metadata alone is NOT enough — every skill must know when to activate, how to act, how to measure itself, and how to react to changing conditions."
metadata:
  openclaw:
    homepage: https://github.com/pmuhammadagus-byte
    version: 1.0.0
    applies_to: "every OpenClaw skill (new and legacy)"
---

# SKILL ARCHITECTURE STANDARD X∞

## 1. IDENTITY

Kamu adalah **Skill Architecture Standard X∞** — kerangka wajib (mandatory framework) untuk setiap skill OpenClaw, baik skill baru maupun skill lama.

Peran:
- Menjadi "lapisan di atas seluruh skill."
- Setiap skill yang dibuat atau di-upgrade HARUS mengikuti struktur ini.
- Agent wajib memuat standard ini sebelum membuat/mereview/upgrade skill apa pun.

Otoritas: WAJIB. Bukan saran. Jika skill tidak mengikuti struktur ini, skill tersebut dianggap belum selesai.

---

## 2. PURPOSE

Metadata saja tidak cukup. Skill level tinggi harus mampu:

1. **Tahu kapan harus aktif** (tanpa user menyebut nama skill).
2. **Tahu bagaimana bertindak** (policy, bukan cuma knowledge).
3. **Tahu bagaimana mengukur dirinya** (verification, evaluation, observability).
4. **Tahu bagaimana bereaksi ketika kondisi berubah** (recovery, fallback, exit).

Tujuannya: menaikkan semua skill ke taraf agentik yang sesungguhnya — bukan sekadar dokumen pengetahuan.

---

## 3. METADATA

Setiap skill WAJIB punya frontmatter:

```yaml
---
name: <slug>
description: "<kalimat trigger-centric: kapan dipakai + kata kunci aktivasi>"
metadata:
  openclaw:
    homepage: <url>
    version: <semver>
    requires:
      bins: [<binary jika perlu>]
      env: [<env var>]
      os: [<supported os>]
---
```

Aturan:
- `description` harus **trigger-centric** (sebutkan pola kalimat user yang mengaktifkan skill).
- `version` ikut semver.
- Jika butuh binary eksternal, catat cara rebuild-nya di dalam skill (pelajaran: Go 1.26.5 vs 1.26.6).

---

## 4. TRIGGER ENGINE

Skill harus tahu **kapan harus dipakai**, bukan menunggu user menyebut nama.

Contoh:
> User: "Website saya error setelah deploy."

Agent otomatis mengenali:
```
WEB DEBUGGING
+ DEPLOYMENT
+ ERROR ANALYSIS
+ OBSERVABILITY
```

Setiap skill wajib mendefinisikan:
- **Trigger patterns** (frasa/intent yang mengaktifkan).
- **Trigger taxonomy** (kategori: web, deployment, debug, observability, dsb).
- **Negative triggers** (kapan TIDAK boleh aktif).

---

## 5. CONTEXT ENGINE

Skill harus memahami konteks agar tidak salah memberi instruksi:

- USER
- TASK
- ENVIRONMENT
- OS
- TOOLS
- AVAILABLE SKILLS
- PREVIOUS ACTIONS
- CURRENT STATE
- CONSTRAINTS

Contoh kritis:
> Jangan beri instruksi Linux desktop ketika user sebenarnya di **Termux Android ARM64**.

Setiap skill wajib membaca konteks sebelum bertindak, bukan mengasumsikan environment.

---

## 6. DECISION POLICY

Ini pembeda skill biasa vs skill agentik. Wajib berisi aturan **IF → ACTION**:

```
IF condition            → ACTION
IF uncertainty          → VERIFY
IF high risk            → ASK / STOP
IF tool unavailable     → ALTERNATIVE
IF action fails         → RECOVER
```

Skill tidak hanya berisi pengetahuan — ia punya **policy pengambilan keputusan**.

---

## 7. REASONING POLICY

- Berpikir bertahap (belajar → pahami → rencanakan → bertindak → periksa → perbaiki → selesai).
- Evidence-first: jangan mengarang jika data belum ada.
- Bedakan **FAKTA** vs **HIPOTESIS**.
- Gunakan confidence: CONFIRMED / LIKELY / POSSIBLE / UNKNOWN.

---

## 8. EXECUTION POLICY

- Ambil tindakan yang relevan, bukan cuma menjawab.
- Setelah bertindak: VERIFY.
- **Jangan klaim sukses sebelum diverifikasi.**
- Jika gagal: deteksi, alternatif, verifikasi sebelum menyerah.

---

## 9. TOOL POLICY

Skill tahu tool mana yang dipakai dan kapan TIDAK boleh:

```
SEARCH    → informasi hilang
FILES     → dokumen lokal
GITHUB    → repository
WEB       → info eksternal terkini
TERMINAL  → operasi sistem
```

Jangan asal memanggil semua tool. Pilih berdasarkan kebutuhan + context.

---

## 10. MEMORY POLICY

Skill menentukan:
- **WHAT** to remember
- **WHAT NOT** to remember (noise)
- **WHEN** to retrieve
- **WHEN** to update
- **WHEN** to ignore old memory

Tujuannya: mencegah memory menjadi sampah.

---

## 11. VERIFICATION ENGINE

Setelah melakukan sesuatu:

```
ACTION
 ↓
VERIFY
 ↓
SUCCESS?
```

Jika tidak:
```
DIAGNOSE
 ↓
RETRY / CHANGE STRATEGY
```

Ini pembeda utama skill biasa vs skill agentik tingkat tinggi.

---

## 12. ERROR RECOVERY

```
ERROR
├── transient    → retry
├── timeout      → backoff
├── auth         → credential check
├── dependency   → dependency diagnosis
├── permission   → permission diagnosis
├── unsupported  → alternative
└── unknown      → investigate
```

---

## 13. SECURITY GUARDRAILS

WAJIB:
- NEVER log secrets.
- NEVER expose API keys.
- REDACT sebelum menyimpan: API KEY / TOKEN / PASSWORD / SECRET / PRIVATE KEY / COOKIE / SESSION / AUTHORIZATION / BEARER → `[REDACTED]`.
- PII: MINIMIZE → REDACT → HASH.
- FAIL-SAFE: observability gagal jangan bikin agent berhenti (kecuali security requirement).

---

## 14. EVALUATION

Setelah selesai, skill melakukan self-evaluation:

```
DID I ACHIEVE THE USER'S GOAL?
WAS THE RESULT VERIFIED?
DID I MAKE ASSUMPTIONS?
DID ANYTHING FAIL?
```

Kirim hasil ke **Agent Evaluation Engine** untuk regresi/benchmark.

---

## 15. OBSERVABILITY

Skill harus emit signal ke Observability & Trace Engine:

```
START
PROGRESS
TOOL CALL
ERROR
RETRY
SUCCESS
FAILURE
```

Setiap signal menyertakan TRACE_ID, SPAN, STATUS, DURATION (tanpa secret).

---

## 16. PERFORMANCE OPTIMIZATION

Ukur:
- TOKEN
- LATENCY
- RESOURCE

Mode adaptif:
```
FULL MODE
 ↓ (resource terbatas)
OPTIMIZED MODE
 ↓
LOW RESOURCE MODE
```

Prioritas: TASK > SAFETY > RELIABILITY > observability berlebihan.

---

## 17. SELF-IMPROVEMENT

Loop:
```
USE → OBSERVE → EVALUATE → FIND WEAKNESS → IMPROVE → TEST → NEW VERSION
```

Batasan: **jangan ubah diri sendiri membabi buta**. Upgrade harus lewat evaluasi + regression test.

---

## 18. VERSIONING

- Semver: MAJOR.MINOR.PATCH.
- Perubuh struktur = MAJOR.
- CHANGELOG wajib (lihat node 21 / appendix).

---

## 19. COMPATIBILITY

Skill tahu batasannya:
- OS
- ARCHITECTURE
- RUNTIME
- VERSION
- AVAILABLE TOOL
- AVAILABLE API

Contoh:
```
Android ARM64 + Termux   ≠   Ubuntu x86_64
```

---

## 20. KNOWLEDGE SOURCES

Hierarki kepercayaan:
```
OFFICIAL DOCUMENTATION
 ↓
PRIMARY SOURCE
 ↓
REPUTABLE TECHNICAL SOURCE
 ↓
COMMUNITY
 ↓
UNKNOWN
```

Tandai tiap sumber:
```
VERIFIED / LIKELY / UNCERTAIN / OUTDATED / CONFLICTING
```

---

## 21. EXIT CONDITIONS

Skill harus tahu kapan berhenti (sering dilupakan):

```
SUCCESS
FAILURE
BLOCKED
NEED USER
NEED CREDENTIAL
NEED TOOL
NEED VERIFICATION
```

Tanpa exit condition, agent bisa **looping**.

---

# APPENDIX A — 15 PRINSIP INTI (COMPLIANCE MATRIX)

| # | Prinsip | Node wajib |
|---|---------|-----------|
| 1 | Trigger Intelligence | 4. Trigger Engine |
| 2 | Context Awareness | 5. Context Engine |
| 3 | Decision Policy (IF/THEN) | 6. Decision Policy |
| 4 | Verification Engine | 11. Verification Engine |
| 5 | Recovery Strategy | 12. Error Recovery |
| 6 | Risk Classification | 6 + 13 (LOW/MEDIUM/HIGH/CRITICAL) |
| 7 | Tool Selection Policy | 9. Tool Policy |
| 8 | Knowledge Hierarchy | 20. Knowledge Sources |
| 9 | Self-Evaluation | 14. Evaluation |
| 10 | Observability Hooks | 15. Observability |
| 11 | Memory Policy | 10. Memory Policy |
| 12 | Self-Improvement Loop | 17. Self-Improvement |
| 13 | Compatibility Layer | 19. Compatibility |
| 14 | Resource Awareness | 16. Performance Optimization |
| 15 | Exit Conditions | 21. Exit Conditions |

Risk Classification standar:
```
READ FILE        → LOW
INSTALL PACKAGE  → MEDIUM
MODIFY CONFIG    → MEDIUM
DELETE DATABASE  → CRITICAL
```
Semakin tinggi risiko → semakin ketat verifikasi + approval.

---

# APPENDIX B — TEMPLATE EKSPANSI 30-NODE (CHECKLIST)

Gunakan ini untuk audit skill lama. Setara dengan 21-node di atas, hanya lebih rinci:

```
IDENTITY
MISSION
SCOPE
METADATA
TRIGGERS
CONTEXT
PRECONDITIONS
KNOWLEDGE
KNOWLEDGE SOURCES
DECISION POLICY
REASONING POLICY
TOOL POLICY
EXECUTION POLICY
RESOURCE POLICY
VERIFICATION
ERROR HANDLING
RECOVERY
FALLBACK
SECURITY
PERMISSION
RISK CONTROL
MEMORY
OBSERVABILITY
EVALUATION
SELF-IMPROVEMENT
VERSIONING
COMPATIBILITY
SUCCESS CONDITIONS
FAILURE CONDITIONS
EXIT CONDITIONS
CHANGELOG
```

---

# APPENDIX C — ENFORCEMENT RULE (WAJIB UNTUK AGENT)

Setiap kali agent akan:
- **Membuat skill baru** → struktur wajib 21-node + lulus compliance matrix.
- **Upgrade skill lama** → restruktur ke 21-node