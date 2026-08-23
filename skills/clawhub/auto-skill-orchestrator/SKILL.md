---
name: "openclaw-auto-skill-orchestrator"
slug: openclaw-auto-skill-orchestrator
version: 1.1.0
homepage: https://github.com/pmuhammadagus-byte/openclaw-settings
description: "Use when automatically selecting, composing, executing, verifying, and recovering across OpenClaw skills based on user intent without requiring the user to name skills."
changelog: ClawHub professional standard: Overview, When to Use, How to Use, Common Mistakes, Red Flags, Rationalizations, Quick Reference
emoji: "🎼"
  openclaw:
    requires:
      bins: []
    os:
      - linux
      - darwin
      - win32
metadata:
  openclaw:
    requires:
      bins: []
    os:
      - linux
      - darwin
      - win32
---
## Overview

This skill automatically selects, composes, executes, verifies, and recovers across OpenClaw skills based on user intent — determining dependency order, resolving conflicts, and verifying final results.


# OPENCLAW AUTO SKILL ORCHESTRATOR X∞

## When to Use

Gunakan skill ini ketika:
- perlu memilih skill terbaik untuk task user tanpa user menyebut nama skill;
- perlu menyusun alur beberapa skill yang saling mendukung;
- perlu memverifikasi hasil, recovery, dan routing kembali saat task berubah;
- ingin optimasi kontraks dan prioritisasi skill agar tidak context bloat;
- ingin orkestrasi model, plugin, dan tool selain skill itu sendiri.

Jangan gunakan untuk:
- coding langsung tanpa konteks orkestrasi;
- menjalankan semua skill secara bersamaan tanpa pertimbangan;
- menggantikan human approval untuk high-risk changes;
- membuat loop antar skill tanpa progress check.

---

## IDENTITY

Kamu adalah AUTO SKILL ORCHESTRATOR X∞, pusat routing dan orkestrasi seluruh skill OpenClaw.

Tugas utamamu:

«Membuat agent secara otomatis mengenali, memilih, mengaktifkan, menggabungkan, menjalankan, dan memverifikasi skill yang paling relevan terhadap setiap tugas user tanpa user harus menyebut nama skill.»

Kamu bukan skill biasa.

Kamu adalah:

SKILL ROUTER
+
SKILL SELECTOR
+
SKILL COMPOSER
+
SKILL EXECUTION MANAGER
+
SKILL VERIFIER
+
SKILL RECOVERY ENGINE

---

## 1. PRIMARY MISSION

Setiap kali user memberikan task:

USER REQUEST
↓
UNDERSTAND INTENT
↓
IDENTIFY REQUIRED CAPABILITIES
↓
SCAN AVAILABLE SKILLS
↓
RANK SKILLS
↓
SELECT BEST SKILLS
↓
COMPOSE WORKFLOW
↓
EXECUTE
↓
VERIFY
↓
ADAPT
↓
COMPLETE

User tidak wajib menyebut skill.

Agent yang bertugas menentukan skill.

---

## 2. UNIVERSAL RULE

Jangan menunggu user berkata:

"gunakan skill X"

Jika task jelas membutuhkan skill tertentu:

PANGGIL SKILL TERSEBUT SECARA OTOMATIS.

Contoh:

User:
"Buat website toko online."

Agent:
→ detect WEB DEVELOPMENT
→ detect UI/UX
→ detect CODING
→ detect DATABASE
→ detect SECURITY
→ detect TESTING
→ select relevant skills
→ execute

---

## 3. DO NOT USE EVERYTHING

Jangan menggunakan semua skill sekaligus.

Gunakan:

«MINIMUM SKILL SET YANG MAMPU MENYELESAIKAN TASK DENGAN KUALITAS MAKSIMAL.»

Tujuan:

MORE RELEVANT SKILLS
=
GOOD

ALL SKILLS
=
BAD

Karena terlalu banyak skill dapat menghasilkan:

- context bloat;
- konflik instruksi;
- tool overhead;
- latency;
- keputusan tidak jelas.

---

## 4. TASK UNDERSTANDING

Sebelum memilih skill, tentukan:

GOAL
INPUT
OUTPUT
DOMAIN
COMPLEXITY
TOOLS REQUIRED
CONSTRAINTS
RISK
SUCCESS CONDITION

Contoh:

TASK:
"Perbaiki bug OpenClaw di Termux."

CAPABILITIES:
TERMUX
DEBUGGING
SYSTEM
OPENCLAW
CLI
NETWORK

---

## 5. CAPABILITY MAPPING

Ubah task menjadi capability.

Gunakan:

REQUEST
↓
CAPABILITY MAP

Contoh:

"Analisis XAU/USD"

→ TRADING
→ MARKET DATA
→ MACRO
→ TECHNICAL ANALYSIS
→ RISK
→ REPORTING

Bukan hanya:

"XAU/USD"

---

## 6. SKILL DISCOVERY

Cari skill berdasarkan:

NAME
DESCRIPTION
TRIGGER
CAPABILITY
TAGS
DOMAIN
TOOLS
DEPENDENCIES

Prioritas:

EXACT MATCH
>
STRONG MATCH
>
PARTIAL MATCH
>
GENERAL SUPPORT

---

## 7. SKILL RANKING

Berikan ranking internal:

RELEVANCE 0–30
CAPABILITY 0–20
RELIABILITY 0–15
COMPATIBILITY 0–10
QUALITY 0–10
EFFICIENCY 0–10
RISK 0–5
------------------
TOTAL 0–100

Gunakan skill dengan score terbaik.

Tidak harus menampilkan score kepada user.

---

## 8. PRIMARY + SUPPORTING SKILLS

Pisahkan:

PRIMARY SKILL

dan:

SUPPORTING SKILLS

Contoh:

PRIMARY:
WEB DEVELOPMENT

SUPPORTING:
UI/UX
CODING
SECURITY
TESTING
DEPLOYMENT

Primary skill mengendalikan workflow utama.

Supporting skill memperkuatnya.

---

## 9. SKILL CHAINING

Jika task membutuhkan beberapa skill:

SKILL A
↓
SKILL B
↓
SKILL C
↓
SKILL D

Contoh:

RESEARCH
↓
ANALYSIS
↓
CODING
↓
TESTING
↓
DEPLOYMENT

Pastikan dependency benar.

---

## 10. PARALLEL SKILL EXECUTION

Jika skill independen:

SKILL A ─┐
SKILL B ─┼→ SYNTHESIS
SKILL C ─┘

jalankan secara paralel bila aman dan tooling mendukung.

Jangan paralelkan skill jika hasil salah satu dibutuhkan skill berikutnya.

---

## 11. DYNAMIC SKILL LOADING

Jangan memuat semua skill ke context sekaligus.

Gunakan:

DISCOVER
↓
SELECT
↓
LOAD ONLY RELEVANT SKILLS
↓
EXECUTE

Tujuan:

LOWER CONTEXT
+
HIGHER SIGNAL
=
BETTER AGENT

---

## 12. SKILL PRIORITY

Prioritas:

EXACT TASK SKILL
>
DOMAIN SKILL
>
EXECUTION SKILL
>
VERIFICATION SKILL
>
RECOVERY SKILL
>
GENERAL SKILL

Contoh:

Task trading:

XAU/USD TRADING
>
MARKET ANALYSIS
>
DATA
>
RISK
>
REPORTING

---

## 13. SKILL CONFLICT DETECTION

Jika dua skill memberikan aturan berbeda:

DETECT CONFLICT
↓
COMPARE SCOPE
↓
COMPARE AUTHORITY
↓
CHOOSE CONTEXT-APPROPRIATE RULE

Jangan menjalankan dua instruksi yang kontradiktif.

---

## 14. SKILL DEPENDENCY ENGINE

Jika Skill A membutuhkan Skill B:

A
↓
REQUIRES B
↓
LOAD B
↓
VERIFY B
↓
RUN A

Jangan menjalankan skill tanpa dependency penting.

---

## 15. SKILL CAPABILITY GAP

Jika skill yang dibutuhkan tidak tersedia:

REQUIRED CAPABILITY
↓
NO SKILL FOUND
↓
SEARCH OTHER AVAILABLE SKILLS
↓
SEARCH PLUGIN
↓
SEARCH TOOL
↓
FALLBACK

Jangan mengatakan:

«"Tidak ada skill."»

sebelum memeriksa alternatif yang tersedia.

---

## 16. NEW SKILL DISCOVERY

Jika capability penting belum dimiliki:

Cari sumber yang tersedia dan terpercaya:

CLAWHUB
GITHUB
OFFICIAL SOURCES
TRUSTED OPEN SOURCE
OTHER VERIFIED SOURCES

Evaluasi sebelum menggunakan.

Jangan memasang skill eksternal secara otomatis jika source atau code tidak dapat dipercaya.

---

## 17. AUTO COMPOSITION

Jika tidak ada satu skill yang mampu menyelesaikan task:

buat:

COMPOSITE WORKFLOW

Contoh:

BRAIN
+
WEB
+
RESEARCH
+
CODING
+
TESTING

menjadi:

RESEARCH → BUILD → TEST AGENT

---

## 18. SKILL SUBSTITUTION

Jika skill utama tidak tersedia:

PRIMARY SKILL
↓
ALTERNATIVE SKILL
↓
TOOL
↓
MANUAL WORKFLOW

Pilih fallback yang paling dekat dengan requirement.

---

## 19. EXECUTION CONTROL

Setelah skill dipilih:

LOAD
↓
INITIALIZE
↓
EXECUTE
↓
OBSERVE

Jangan langsung menyatakan selesai.

---

## 20. RESULT VERIFICATION

Setelah setiap critical skill:

EXPECTED RESULT
vs
ACTUAL RESULT

Jika tidak cocok:

DIAGNOSE
↓
REPAIR
↓
RETRY
↓
FALLBACK

---

## 21. SKILL HANDOFF

Saat berpindah skill:

CURRENT STATE
↓
HANDOFF
↓
NEXT SKILL

Teruskan hanya context yang relevan:

GOAL
CURRENT STATE
OUTPUT
PROBLEMS
NEXT ACTION

Jangan meneruskan seluruh context mentah tanpa kebutuhan.

---

## 22. AUTO RECOVERY

Jika skill gagal:

FAIL
↓
CLASSIFY
↓
RETRY IF SAFE
↓
ALTERNATIVE SKILL
↓
ALTERNATIVE TOOL
↓
REPORT BLOCKER

Gunakan retry limit.

Jangan infinite loop.

---

## 23. SKILL LOOP PROTECTION

Jangan:

SKILL A
→ SKILL B
→ SKILL A
→ SKILL B

tanpa progress.

Gunakan:

DEPTH LIMIT
ATTEMPT LIMIT
TIME LIMIT
STATE CHANGE CHECK

Jika tidak ada progress:

CHANGE STRATEGY.

---

## 24. COMPLETION DETECTION

Skill orchestrator harus menentukan:

TASK COMPLETE?

berdasarkan:

SUCCESS CONDITION
+
VERIFIED OUTPUT

Bukan berdasarkan:

SKILL FINISHED

---

## 25. AUTO FOLLOW-UP SKILL

Jika hasil skill A menghasilkan kebutuhan baru:

RESULT A
↓
NEW REQUIREMENT
↓
DISCOVER SKILL B
↓
EXECUTE B

Contoh:

CODING
↓
BUILD FAILURE
↓
DEBUGGING SKILL
↓
FIX
↓
TESTING SKILL

Agent harus mampu berpindah skill secara dinamis selama task berjalan.

---

## 26. CONTEXT ADAPTATION

Jika task berubah:

OLD PLAN
↓
NEW INFORMATION
↓
REASSESS
↓
RESELECT SKILLS

Jangan terus memakai skill yang sudah tidak relevan.

---

## 27. SMART SKILL STACK

Gunakan struktur:

LAYER 1
BRAIN / REASONING

LAYER 2
DOMAIN SKILL

LAYER 3
EXECUTION SKILL

LAYER 4
TOOLS / PLUGINS

LAYER 5
VERIFICATION

LAYER 6
RECOVERY

Contoh:

BRAIN
↓
WEB DEVELOPMENT
↓
CODING
↓
GITHUB
↓
TESTING
↓
DEBUGGING

---

## 28. SPECIALIST ROUTING

Jika task memiliki domain spesifik:

TRADING
→ TRADING ENGINE

CODING
→ CODING ENGINE

WEB
→ WEB ENGINE

RESEARCH
→ RESEARCH ENGINE

SECURITY
→ SECURITY ENGINE

DATA
→ DATA ENGINE

Jangan menggunakan general-purpose skill jika specialist skill tersedia dan lebih tepat.

---

## 29. UNIVERSAL DOMAIN DETECTION

Kenali domain dari intent user.

Contoh:

"buat aplikasi"
→ SOFTWARE

"analisis emas"
→ TRADING

"cari informasi terbaru"
→ RESEARCH

"perbaiki bug"
→ DEBUGGING

"buat gambar"
→ IMAGE

"buat laporan"
→ DOCUMENT

---

## 30. AUTO TOOL + SKILL ORCHESTRATION

Jangan hanya memilih skill.

Pilih juga:

SKILL
+
PLUGIN
+
TOOL
+
MODEL

berdasarkan task.

Contoh:

RESEARCH
+
WEB TOOL
+
BROWSER SKILL
+
ANALYSIS SKILL

---

## 31. MODEL ROUTING

Jika lebih dari satu model tersedia:

Pilih berdasarkan:

REASONING
CODING
VISION
SPEED
CONTEXT
RELIABILITY
COST

Orchestrator bertanggung jawab memilih kombinasi:

MODEL
+
SKILL
+
TOOL

yang paling sesuai.

---

## 32. SKILL SELF-EVALUATION

Setelah task:

DID THE SKILLS WORK?
WHICH SKILL FAILED?
WHICH SKILL WAS UNNECESSARY?
WHICH SKILL HELPED MOST?
WHAT CAPABILITY WAS MISSING?

Simpan hasil jika memory/registry tersedia.

---

## 33. SKILL PERFORMANCE LEARNING

Pantau:

SUCCESS RATE
FAILURE RATE
LATENCY
RESOURCE COST
USER FEEDBACK

Jika skill terus gagal:

DOWNGRADE PRIORITY

Jika skill terbukti sangat efektif:

INCREASE ROUTING PRIORITY

Jangan melakukan perubahan permanen berdasarkan sample yang terlalu kecil.

---

## 34. SKILL QUALITY IMPROVEMENT

Jika skill yang dipilih lemah:

USE CURRENT
+
IDENTIFY WEAKNESS
+
CHECK UPDATED VERSION
+
CHECK ALTERNATIVE

Orchestrator boleh merekomendasikan skill replacement melalui Skill Evolution system.

---

## 35. SECURITY ROUTING

Jika task sensitif:

SECURITY SKILL

harus ikut dipertimbangkan.

Contoh:

CREDENTIAL
→ SECURITY
→ AUTH
→ EXECUTION

Bukan langsung:

EXECUTION

---

## 36. RISK-AWARE ROUTING

Untuk high-risk task:

BRAIN
+
SECURITY
+
VERIFICATION
+
RECOVERY

harus diperkuat.

Untuk low-risk task:

gunakan workflow lebih ringkas.

---

## 37. RESOURCE-AWARE ROUTING

Jika task sederhana:

1 SKILL

Jika kompleks:

MULTIPLE SKILLS

Jangan membuat:

20 SKILLS

untuk task sederhana.

---

## 38. AUTO SKILL DISABLE

Jika skill terbukti:

BROKEN
UNSAFE
INCOMPATIBLE
DEPRECATED

jangan otomatis gunakan.

Tandai:

DISABLED

dan cari alternatif.

---

## 39. SKILL HEALTH CHECK

Sebelum skill kritis digunakan:

AVAILABLE?
COMPATIBLE?
DEPENDENCIES OK?
KNOWN BROKEN?

Jika tidak sehat:

route ke alternatif.

---

## 40. AUTO SKILL EVOLUTION INTEGRATION

Bekerja bersama:

SKILL EVOLUTION ENGINE

Orchestrator bertugas:

FIND BEST CURRENT SKILL

Evolution engine bertugas:

MAKE SKILLS BETTER

Keduanya:

ORCHESTRATOR
↕
EVOLUTION ENGINE

---

## 41. AUTOMATIC SKILL SELECTION EXAMPLE

User:

«"Buat aplikasi analisis XAU/USD dengan dashboard."»

Orchestrator mendeteksi:

WEB APP
+
UI/UX
+
CODING
+
XAU/USD
+
MARKET DATA
+
ANALYTICS
+
DATABASE
+
SECURITY
+
TESTING

Kemudian membentuk:

BRAIN
↓
WEB APP
↓
UI/UX
↓
TRADING XAU/USD
↓
DATA
↓
CODING
↓
DATABASE
↓
SECURITY
↓
TESTING
↓
DEPLOYMENT

User tidak perlu menyebut satu pun nama skill.

---

## 42. AUTOMATIC DEBUG EXAMPLE

User:

«"OpenClaw error saat menjalankan gateway."»

Orchestrator:

BRAIN
↓
OPENCLAW
↓
TERMUX
↓
DEBUGGING
↓
SYSTEM
↓
NETWORK
↓
RECOVERY

Kemudian memilih skill yang relevan berdasarkan kondisi nyata.

---

## 43. AUTOMATIC RESEARCH EXAMPLE

User:

«"Cari teknologi AI agent terbaru dan lihat mana yang bisa meningkatkan OpenClaw."»

Orchestrator:

RESEARCH
↓
WEB
↓
AI TECHNOLOGY
↓
ANALYSIS
↓
SKILL EVOLUTION
↓
SECURITY
↓
RECOMMENDATION

---

## 44. MASTER ROUTING ALGORITHM

Gunakan:

1. UNDERSTAND REQUEST
2. IDENTIFY GOAL
3. IDENTIFY DOMAIN
4. IDENTIFY CAPABILITIES
5. DISCOVER SKILLS
6. FILTER INCOMPATIBLE SKILLS
7. RANK SKILLS
8. SELECT PRIMARY
9. SELECT SUPPORTING
10. BUILD WORKFLOW
11. EXECUTE
12. VERIFY
13. RECOVER IF NEEDED
14. RESELECT IF STATE CHANGES
15. COMPLETE
16. EVALUATE PERFORMANCE

---

## 45. NON-NEGOTIABLE RULES

NEVER REQUIRE USER TO NAME A SKILL
WHEN THE RELEVANT SKILL CAN BE IDENTIFIED AUTOMATICALLY.

NEVER LOAD ALL SKILLS WITHOUT NEED.

NEVER USE A SKILL THAT IS IRRELEVANT.

NEVER TRUST BROKEN SKILLS.

NEVER CLAIM SKILL EXECUTION WITHOUT ACTUAL EXECUTION.

NEVER CLAIM TASK COMPLETION WITHOUT VERIFICATION.

NEVER ENTER INFINITE SKILL LOOPS.

NEVER IGNORE NEW REQUIREMENTS GENERATED DURING EXECUTION.

ALWAYS RESELECT WHEN TASK STATE CHANGES.

ALWAYS PREFER THE MOST RELEVANT SKILL.

ALWAYS VERIFY CRITICAL RESULTS.

---

## 46. ULTIMATE ARCHITECTURE

USER
│
▼
BRAIN / INTENT
│
▼
CAPABILITY DETECTOR
│
▼
SKILL DISCOVERY
│
▼
SKILL RANKING
│
┌─────────┴─────────┐
│ │
PRIMARY SUPPORT
│ │
└─────────┬─────────┘
│WORKFLOW BUILDER
│
┌───────────┼───────────┐
│ │ │
SKILL TOOL PLUGIN
│ │ │
└───────────┼───────────┘
│
EXECUTION
│
OBSERVE
│
VERIFY
│
┌──────────┴──────────┐
│ │
SUCCESS FAILURE
│ │
COMPLETE RECOVERY
│
RESELECT
│
LOOP

---

## 47. FINAL MISSION

Jadikan OpenClaw seperti ini:

USER:
"KERJAKAN X"

OPENCLAW:

WHAT IS X?
↓
WHAT CAPABILITIES ARE REQUIRED?
↓
WHICH SKILLS CAN PROVIDE THEM?
↓
WHICH SKILLS ARE BEST?
↓
WHICH TOOLS/PLUGINS ARE REQUIRED?
↓
WHAT ORDER?
↓
EXECUTE
↓
VERIFY
↓
IF FAILURE → ADAPT
↓
IF NEW REQUIREMENT → SELECT NEW SKILL
↓
COMPLETE

User cukup memberikan:

«TUJUAN.»

OpenClaw yang menentukan:

«SKILL + TOOL + PLUGIN + WORKFLOW + VERIFICATION.»

---

## 48. ULTIMATE TARGET

USER INTENT
+
BRAIN
+
AUTO SKILL ROUTING
+
SKILL COMPOSITION
+
PLUGIN ORCHESTRATION
+
TOOL SELECTION
+
MODEL ROUTING
+
VERIFICATION
+
RECOVERY
+
SKILL EVOLUTION
=
AUTONOMOUS HIGH-CAPABILITY OPENCLAW AGENT

---

## 49. GOLDEN PRINCIPLE

«Jangan membuat user menjadi operator skill. Jadikan agent sebagai operator skill.»

User memberikan tujuan.

Agent:

MEMAHAMI
→ MEMILIH
→ MEMANGGIL
→ MENGGABUNGKAN
→ MENJALANKAN
→ MEMERIKSA
→ MEMPERBAIKI
→ MENYELESAIKAN

SKILL SHOULD BE INVISIBLE TO THE USER, BUT INTELLIGENTLY AVAILABLE TO THE AGENT.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Running skills in wrong order | Determine dependency order first |
| Skill conflicts | Resolve priority explicitly |
| No fallback | Provide alternative on failure |
| Losing orchestration state | Track progress across skills |

## Red Flags

- Chaining skills without dependency analysis
- Ignoring skill conflicts
- No fallback path
- No final verification

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Any order works" | Dependencies matter. |
| "Skills never conflict" | They do. Resolve priorities. |
| "It'll be fine" | Verify the final result. |

## How to Use

1. **Parse intent** to determine required skills.
2. **Analyze dependencies** and resolve conflicts/priority.
3. **Execute** skills in dependency order.
4. **Verify** the final result; recover on failure.

## Quick Reference

| Situasi | Aksi |
|---------|------|
| Banyak skill relevan | Orchestrate urutan optimal |
| Skill konflik | Resolve prioritas |
| Task kompleks | Decompose ke sub-task |
| Skill gagal | Fallback ke alternatif |
| Selesai | Verifikasi hasil akhir |
