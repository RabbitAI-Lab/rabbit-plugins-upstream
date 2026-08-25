---
name: openclaw-auto-skill-orchestrator
slug: openclaw-auto-skill-orchestrator
version: 1.1.2
description: "Gunakan saat user secara eksplisit meminta menyusun/mengorkestrasikan urutan eksekusi beberapa skill untuk task tertentu (mis. 'susun alur skill A lalu B', 'orkestrasikan skill ini')."
metadata:
  openclaw:
    version: 1.1.2
---

# openclaw-auto-skill-orchestrator — X∞ Compliance Layer

## 1. IDENTITY
`openclaw-auto-skill-orchestrator` adalah skill orkestrasi tingkat sistem. Perannya: membantu sebagai **SKILL ROUTER + SELECTOR + COMPOSER + VERIFIER + RECOVERY** — merancang alur, bukan mengeksekusi otomatis. Aksi nyata tetap di bawah kendali dan persetujuan user. Skill ini tidak mengerjakan domain secara langsung; ia membantu merutekan dan mengoordinasikan skill lain, dengan setiap langkah terverifikasi.

## 2. PURPOSE
Memberikan agent kemampuan untuk:
- mendeteksi intent user dan memetakan ke capability yang dibutuhkan;
- menemukan, memeringkat, dan memilih skill paling relevan (primary + supporting);
- menyusun workflow berurutan/paralel dengan resolusi dependensi & konflik;
- mengusulkan eksekusi, memverifikasi, me-recover, dan berpindah skill saat state berubah;
- mengoptimasi pemakaian context, tool, plugin, dan model agar tidak bloat.

## 3. METADATA
Lihat frontmatter (name, slug, version, description). Version mengikuti SemVer; setiap perubahan struktur/kebijakan wajib dicatat di CHANGELOG.

## 4. TRIGGER ENGINE
Aktif ketika user memberikan task yang membutuhkan koordinasi lebih dari satu kemampuan, atau meminta agent "kerjakan X" tanpa menyebut skill.

**Frasa pemicu spesifik** (cocokkan secara longgar):
- user secara eksplisit meminta orkestrasi: "susun alur skill", "orkestrasikan skill X dan Y", "buatkan workflow dari skill berikut";
- task dengan >1 skill yang sudah disebut user tapi butuh penyusunan urutan;
- user minta bantuan merencanakan urutan eksekusi skill.

**Bukan trigger sendirian:** frasa umum seperti "buat aplikasi", "kerjakan saja", "urus semua" TIDAK cukup — butuh permintaan orkestrasi eksplisit atau user menyebut beberapa skill.

**Contoh kalimat user:**
- "Tolong orkestrasikan skill research dan coding untuk dashboard analisis XAU/USD."
- "OpenClaw error saat menjalankan gateway di Termux, bantu susun urutan skill penanganannya."
- "Susun alur skill untuk menelusuri teknologi AI agent terbaru lalu buat rekomendasi."

**Negative trigger (JANGAN aktifkan sebagai orchestrator murni):**
- coding/debugging langsung yang hanya butuh satu skill tanpa koordinasi lintas skill;
- satu skill sudah cukup dan tidak ada dependensi silang;
- perintah di luar kapabilitas agent (minta kredensial/user/tool yang tidak ada) — route ke EXIT CONDITIONS, bukan orkestrasi penuh;
- user sudah menunjuk skill tertentu secara eksplisit dan tidak butuh komposisi.

## 5. CONTEXT ENGINE
Sebelum memilih/execute, baca dan catat: OS, ARCH, runtime, versi tool/API, dan batasan resource. **Termux Android ARM64 ≠ Ubuntu x86_64** (path, package manager, binary, permission berbeda). Verifikasi environment sebelum menjalankan skill yang bergantung platform.

## 6. DECISION POLICY

| KONDISI | MAKA | ALASAN |
|---|---|---|
| Intent ambigu / kurang konteks | VERIFY (tanya klarifikasi minimal) | Salah routing lebih mahal dari satu pertanyaan |
| Task jelas butuh skill X | RANTAI X (ajukan rencana + minta konfirmasi untuk aksi berdampak) | Agent membantu menyusun alur, tapi aksi nyata butuh persetujuan user |
| >1 skill relevan | RANK lalu pilih PRIMARY + SUPPORTING | Hindari context bloat & konflik instruksi |
| Dua skill konflik aturan | COMPARE scope & authority, pilih yang pas konteks | Cegah eksekusi instruksi kontradiktif |
| Skill utama tidak tersedia | SUBSTITUSI → tool → manual workflow | Task tetap selesai dengan kualitas terbaik |
| High-risk (credensial / destruktif) | LIBATKAN security + verification + minta approval | Keamanan & oversight wajib |
| Hasil kritis tidak cocok harapan | DIAGNOSE → REPAIR → RETRY → FALLBACK | Jangan klaim sukses tanpa bukti |
| State task berubah | RESELECT skill | Skill usang memperburuk hasil |
| Tak ada progress setelah N percobaan | CHANGE STRATEGY / REPORT BLOCKER | Cegah loop tak berujung |
| Dependency skill belum siap | LOAD & VERIFY dependency dulu | Eksekusi prematur = gagal |

## 7. REASONING POLICY
Evidence-first. Bedakan **FAKTA** (terverifikasi) vs **HIPOTESIS** (dugaan). Gunakan confidence: CONFIRMED / LIKELY / POSSIBLE / UNKNOWN. Jangan klaim eksekusi/selesai tanpa verifikasi nyata.

## 8. EXECUTION POLICY (Runbook)
Urutan aksi wajib:
1. **PARSE** intent → goal, input, output, domain, complexity, tools, constraints, risk, success condition.
2. **MAP** ke capability (bukan kata kunci mentah).
3. **DISCOVER** skill via name / description / trigger / capability / tags / domain / tools / dependencies.
4. **FILTER** skill incompatible (OS/ARCH/versi).
5. **RANK** (skor 0–100) → pilih PRIMARY + SUPPORTING.
6. **BUILD** workflow: urutan berurutan (dependency) atau paralel (jika independen & aman).
7. **LOAD ONLY** skill terpilih (jangan semua).
8. **EXECUTE** per urutan; OBSERVE tiap langkah.
9. **VERIFY** hasil kritis (lihat Verification Engine).
10. Jika gagal → RECOVER (lihat Error Recovery), lalu RESELECT bila state berubah.
11. **COMPLETE** hanya bila success condition terpenuhi & terverifikasi.

Preferensi tool: gunakan tool paling presisi untuk kebutuhan (mis. `read`/`exec` untuk file/shell, `web_fetch`/`browser` untuk web, `skill_workshop` untuk manajemen skill). Jangan memanggil semua tool sekaligus.

## 9. TOOL POLICY
Pilih tool berdasar kebutuhan + konteks, bukan kebiasaan. Prioritas: tool native agent > CLI > browser. Untuk orkestrasi skill, baca daftar skill (`openclaw skills` / file `SKILL.md`) sebelum `skill_workshop` apply. Redact secret sebelum log/store.

## 10. MEMORY POLICY
Ingat hasil routing yang terbukti (skill mana efektif/ gagal untuk domain tertentu). Retrieve saat task mirip muncul; update bila performa berubah. Simpan ke memory/registry bila tersedia. Abaikan noise; jangan bloat context dengan seluruh riwayat.

## 11. VERIFICATION ENGINE
Verifikasi NYATA pasca-aksi (bukan sekadar exit code 0). Checklist per critical step:
- [ ] **EXISTENCE**: file/dir/resource yang dijanjikan benar-benar ada (`read`/`ls`/`stat`).
- [ ] **CONTENT**: isi sesuai harapan (bukan kosong/template).
- [ ] **BEHAVIOR**: aksi berdampak nyata (proses jalan, endpoint merespons, build lulus).
- [ ] **EXIT/STATE**: exit code & state sistem konsisten dengan sukses.
- [ ] **NO REGRESSION**: perubahan tidak merusak konfigurasi/dependensi lain.
- [ ] **USER-FACING**: output yang diklaim ke user sudah benar & lengkap.

Jika salah satu gagal → DIAGNOSE → REPAIR → RETRY → FALLBACK. "Sukses" hanya bila semua checklist hijau.

## 12. ERROR RECOVERY
Hierarki recovery (naik level bila gagal):
1. **Transient** (network blip, race) → RETRY dengan backoff eksponensial (max 3–5x).
2. **Timeout** → tingkatkan timeout / pindah ke low-resource mode / pecah task.
3. **Auth/credential** → cek kredensial, minta user (EXIT: NEED CREDENTIAL).
4. **Dependency missing/broken** → cari alternatif skill/tool, atau install dari source terpercaya (EXIT: NEED TOOL).
5. **Logic/conflict** → ubah strategi, reselect skill, resolve prioritas.
6. **Unknown** → investigasi minimal, batasi blast radius, REPORT BLOCKER (EXIT: BLOCKED).

Setiap retry wajib **state change check**: jika tidak ada progres nyata setelah batas, STOP dan ganti strategi — jangan infinite loop.

**Contoh:** Skill coding gagal build → (1) retry bersih → (2) cek dependency → (3) ganti ke skill debugging → (4) jika dependency rusak, fallback ke tool CLI langsung → (5) masih gagal, laporkan blocker + log tanpa secret.

## 13. SECURITY GUARDRAILS
NEVER log secret. REDACT API KEY / TOKEN / PASSWORD / SECRET sebelum simpan atau tampilkan. PII: MINIMIZE → REDACT → HASH. Untuk task sensitif (credensial, perubahan sistem, destruktif), wajibkan security skill + approval user. Jangan bypass safeguard apa pun.

## 14. EVALUATION
Self-eval pasca-task: capai goal? terverifikasi? ada asumsi tak tertutup? ada skill gagal/tak perlu? capability hilang? Kirim ringkasan ke Agent Evaluation Engine bila tersedia. Gunakan untuk naik/turunkan routing priority.

## 15. OBSERVABILITY
Emit event: START / PROGRESS / TOOL CALL / ERROR / RETRY / SUCCESS / FAILURE lengkap dengan TRACE_ID. Tanpa secret. Catat skill yang dipilih, urutan, dan hasil tiap step untuk audit.

## 16. PERFORMANCE OPTIMIZATION
Mode: FULL → OPTIMIZED → LOW RESOURCE (bila terbatas). Prioritas: TASK > SAFETY > RELIABILITY. Kurangi context dengan dynamic loading (load only relevant). Paralelkan hanya bila independen & aman.

## 17. SELF-IMPROVEMENT
USE → OBSERVE → EVALUATE → FIND WEAKNESS → IMPROVE → TEST → NEW VERSION. Pantau SUCCESS/FAILURE RATE, latency, resource cost, user feedback. Naikkan prioritas skill efektif; turunkan yang sering gagal (berbasis sampel cukup, jangan terlalu kecil). Integrasikan dengan Skill Evolution Engine.

## 18. VERSIONING
SemVer. Perubahan struktur/kebijakan = MAJOR; penambahan panduan/runbook = MINOR; perbaikan redaksi = PATCH. CHANGELOG wajib tiap rilis.



**CHANGELOG**
- 1.0.0 — Light upgrade: frontmatter `description` diperbaiki jadi trigger nyata; Node 2 (PURPOSE) & Node 3 (METADATA) diisi bila stub; `metadata.openclaw.version` diset. Body domain dipertahankan.
- 1.1.2 — Cabut sisa pattern: hapus unicode tersembunyi, shadow command, keyword bait di contoh, soften role menjadi helper, perbaiki skill-card.md.
- 1.1.1 — Kepatuhan SkillSpector: frontmatter diperbaiki; lunakkan auto-call menjadi rantai dengan approval; hapus blockquote; persempit trigger agar butuh permintaan orkestrasi eksplisit; tegaskan aksi berdampak butuh approval user.
## 19. COMPATIBILITY
Ketahui OS / ARCH / RUNTIME / versi tool & API yang tersedia sebelum routing. Skill yang incompatible dengan environment = jangan otomatis gunakan; tandai DISABLED & cari alternatif.

## 20. KNOWLEDGE SOURCES
Trust hierarchy: OFFICIAL > PRIMARY > REPUTABLE > COMMUNITY > UNKNOWN. Tandai tiap sumber: VERIFIED / LIKELY / UNCERTAIN / OUTDATED / CONFLICTING. Jangan pasang skill eksternal otomatis bila source/code tak terpercaya.

## 21. EXIT CONDITIONS
Berhenti (dan laporkan) pada: SUCCESS / FAILURE / BLOCKED / NEED USER / NEED CREDENTIAL / NEED TOOL / NEED VERIFICATION. Jangan lanjut orkestrasi tanpa syarat terpenuhi.
# OPENCLAW AUTO SKILL ORCHESTRATOR X∞

## Overview
Skill orkestrasi yang membantu user menyusun urutan eksekusi beberapa skill OpenClaw ketika diminta — merutekan, memverifikasi, dan me-recover alur, dengan persetujuan user untuk setiap aksi berdampak. Menyelesaikan dependensi dan konflik instruksi agar agent bekerja dengan context tetap ramping.

---

## When to Use
Gunakan ketika:
- user secara eksplisit meminta orkestrasi beberapa skill, dan task butuh >1 kemampuan;
- perlu menyusun alur beberapa skill yang saling mendukung;
- perlu memverifikasi hasil, recovery, dan routing ulang saat task berubah;
- ingin optimasi context (hindari bloat) dan prioritas skill;
- perlu orkestrasi model, plugin, dan tool—bukan hanya skill.

Jangan gunakan untuk:
- coding/debugging langsung yang cukup satu skill tanpa koordinasi;
- menjalankan semua skill sekaligus tanpa pertimbangan;
- menggantikan approval user untuk high-risk change;
- membuat loop antar skill tanpa progress check.

---

## Core Operating Model

### 1. PRIMARY MISSION (Pipeline)
```
USER REQUEST
  ↓ UNDERSTAND INTENT
  ↓ IDENTIFY REQUIRED CAPABILITIES
  ↓ SCAN AVAILABLE SKILLS
  ↓ RANK SKILLS
  ↓ SELECT BEST (PRIMARY + SUPPORTING)
  ↓ COMPOSE WORKFLOW
  ↓ EXECUTE
  ↓ VERIFY
  ↓ ADAPT / RECOVER
  ↓ COMPLETE
```
Agent membantu menyusun alur, tetapi setiap aksi nyata tetap di bawah kendali dan persetujuan user.

### 2. UNIVERSAL RULE
Jika user setuju dengan rencana orkestrasi → **RANTAI skill yang relevan** sesuai urutan. Agent mengusulkan alur & meminta konfirmasi sebelum aksi berdampak (terutama high-risk). Jangan mengeksekusi destruktif tanpa approval.
Contoh: "Tolong susun alur skill: design → coding → database → security → testing untuk website toko online." → usulkan workflow, lalu jalankan per persetujuan.

### 3. MINIMUM SKILL SET
Gunakan **minimum set yang mampu selesaikan task dengan kualitas maksimal**.
`MORE RELEVANT = GOOD` · `ALL SKILLS = BAD` (bloat, konflik, overhead, latency, keputusan kabur).

### 4. TASK UNDERSTANDING (template)
Tentukan sebelum pilih skill: GOAL, INPUT, OUTPUT, DOMAIN, COMPLEXITY, TOOLS REQUIRED, CONSTRAINTS, RISK, SUCCESS CONDITION.
Contoh "Perbaiki bug OpenClaw di Termux" → capabilities: TERMUX, DEBUGGING, SYSTEM, OPENCLAW, CLI, NETWORK.

### 5. CAPABILITY MAPPING
Ubah task jadi capability map. "Analisis XAU/USD" → TRADING, MARKET DATA, MACRO, TECHNICAL ANALYSIS, RISK, REPORTING.

### 6. SKILL DISCOVERY
Cari via: NAME, DESCRIPTION, TRIGGER, CAPABILITY, TAGS, DOMAIN, TOOLS, DEPENDENCIES.
Prioritas kecocokan: EXACT > STRONG > PARTIAL > GENERAL SUPPORT.

### 7. SKILL RANKING (rubrik 0–100)
| Dimensi | Bobot |
|---|---|
| Relevance | 0–30 |
| Capability | 0–20 |
| Reliability | 0–15 |
| Compatibility | 0–10 |
| Quality | 0–10 |
| Efficiency | 0–10 |
| Risk (penalti) | 0–5 |
Gunakan score tertinggi; tidak perlu tampilkan ke user.

### 8. PRIMARY + SUPPORTING
Pisahkan PRIMARY (kendali workflow utama) dan SUPPORTING (perkuat). Contoh PRIMARY: WEB DEVELOPMENT; SUPPORTING: UI/UX, CODING, SECURITY, TESTING, DEPLOYMENT.

### 9. SKILL CHAINING & 10. PARALLEL
Berurutan bila ada dependensi (A→B→C). Paralelkan hanya bila independen & aman (A,B,C ─┐→ Synthesis). Jangan paralelkan yang butuh hasil satu sama lain.

### 11. DYNAMIC LOADING
DISCOVER → SELECT → LOAD ONLY RELEVANT → EXECUTE. Tujuannya: LOWER CONTEXT + HIGHER SIGNAL.

### 12. SKILL PRIORITY
EXACT TASK > DOMAIN > EXECUTION > VERIFICATION > RECOVERY > GENERAL.

### 13. CONFLICT DETECTION
DETECT → COMPARE SCOPE → COMPARE AUTHORITY → CHOOSE CONTEXT-APPROPRIATE RULE. Jangan jalankan dua instruksi kontradiktif.

### 14. DEPENDENCY ENGINE
A requires B → LOAD B → VERIFY B → RUN A. Jangan jalankan tanpa dependency kritis.

### 15. CAPABILITY GAP
NO SKILL FOUND → cari skill lain → plugin → tool → manual fallback. Jangan bilang "tidak ada skill" sebelum habiskan alternatif.

### 16. NEW SKILL DISCOVERY
Cari sumber terpercaya (ClawHub, official, trusted OSS). Evaluasi sebelum pakai. Jangan pasang otomatis bila source/code tak terpercaya.

### 17. AUTO COMPOSITION
Bila tak ada skill tunggal cukup → buat COMPOSITE WORKFLOW (mis. RESEARCH → BUILD → TEST AGENT).

### 18. SUBSTITUTION
PRIMARY hilang → ALTERNATIVE SKILL → TOOL → MANUAL WORKFLOW. Pilih fallback terdekat dengan requirement.

### 19. EXECUTION CONTROL
LOAD → INITIALIZE → EXECUTE → OBSERVE. Jangan langsung klaim selesai.

### 20. RESULT VERIFICATION
EXPECTED vs ACTUAL. Tidak cocok → DIAGNOSE → REPAIR → RETRY → FALLBACK.

### 21. HANDOFF
Teruskan hanya context relevan: GOAL, CURRENT STATE, OUTPUT, PROBLEMS, NEXT ACTION.

### 22. AUTO RECOVERY & 23. LOOP PROTECTION
FAIL → CLASSIFY → RETRY (limit) → ALTERNATIVE → REPORT BLOCKER. Gunakan DEPTH/ATTEMPT/TIME LIMIT + STATE CHANGE CHECK. Tanpa progres → CHANGE STRATEGY.

### 24. COMPLETION DETECTION
Berdasarkan SUCCESS CONDITION + VERIFIED OUTPUT, bukan "skill finished".

### 25. AUTO FOLLOW-UP
Hasil A memunculkan kebutuhan baru → DISCOVER B → EXECUTE. (Mis. CODING → build fail → DEBUGGING → fix → TESTING.)

### 26. CONTEXT ADAPTATION
Task berubah → REASSESS → RESELECT. Jangan pakai skill usang.

### 27. SMART SKILL STACK
LAYER 1 BRAIN → 2 DOMAIN → 3 EXECUTION → 4 TOOLS/PLUGINS → 5 VERIFICATION → 6 RECOVERY.

### 28. SPECIALIST ROUTING
Domain spesifik → specialist (TRADING→trading engine, CODING→coding engine, dll). Jangan pakai general bila specialist lebih tepat.

### 29. DOMAIN DETECTION
"buat aplikasi"→SOFTWARE; "analisis emas"→TRADING; "cari info terbaru"→RESEARCH; "perbaiki bug"→DEBUGGING; "buat gambar"→IMAGE; "buat laporan"→DOCUMENT.

### 30. TOOL+SKILL ORCHESTRATION & 31. MODEL ROUTING
Pilih kombinasi SKILL + PLUGIN + TOOL + MODEL berdasar REASONING/CODING/VISION/SPEED/CONTEXT/RELIABILITY/COST.

### 32–34. LEARNING & QUALITY
Post-task: skill mana gagal/tak perlu/paling membantu/capability hilang? Naik/turunkan priority; usulkan replacement via Skill Evolution bila skill lemah.

### 35–38. SECURITY / RISK / RESOURCE / DISABLE
Sensitif → libatkan SECURITY. High-risk → perkuat BRAIN+SECURITY+VERIFICATION+RECOVERY. Sederhana → 1 skill. Skill BROKEN/UNSAFE/INCOMPATIBLE/DEPRECATED → tandai DISABLED, cari alternatif.

### 39. HEALTH CHECK
Sebelum skill kritis: AVAILABLE? COMPATIBLE? DEPENDENCIES OK? KNOWN BROKEN? Bila tidak sehat → route alternatif.

### 44. MASTER ROUTING ALGORITHM
1 Understand · 2 Goal · 3 Domain · 4 Capabilities · 5 Discover · 6 Filter incompatible · 7 Rank · 8 Select primary · 9 Select supporting · 10 Build workflow · 11 Execute · 12 Verify · 13 Recover · 14 Reselect if change · 15 Complete · 16 Evaluate.

### 45. NON-NEGOTIABLE RULES
- SELALU hormati bila user sudah menunjuk skill tertentu; jangan mengganti pilihan user tanpa alasan.
- NEVER load semua skill tanpa need.
- NEVER pakai skill irelevan / broken.
- NEVER klaim eksekusi/selesai tanpa verifikasi nyata.
- NEVER infinite loop.
- ALWAYS reselect bila state berubah; ALWAYS verifikasi hasil kritis.
- UNTUK aksi berdampak (destruktif, kredensial, perubahan sistem): selalu minta approval user.

---

## Concrete Examples (Input → Output)

**Contoh 1 — Web app trading**
- Input: "Tolong orkestrasikan skill research, lalu coding, lalu testing untuk dashboard analisis XAU/USD."
- Deteksi: WEB APP + UI/UX + CODING + XAU/USD + MARKET DATA + ANALYTICS + DATABASE + SECURITY + TESTING.
- Workflow: BRAIN → WEB APP → UI/UX → TRADING XAU/USD → DATA → CODING → DATABASE → SECURITY → TESTING → DEPLOYMENT.
- Output ke user: aplikasi jadi + verifikasi (build lulus, endpoint merespons).

**Contoh 2 — Debug**
- Input: "OpenClaw error saat menjalankan gateway."
- Deteksi: OPENCLAW + TERMUX + DEBUGGING + SYSTEM + NETWORK + RECOVERY.
- Eksekusi: baca log, cek env Termux ARM64, perbaiki, verifikasi gateway jalan.

**Contoh 3 — Research**
- Input: "Cari teknologi AI agent terbaru dan lihat mana yang bisa tingkatkan OpenClaw."
- Deteksi: RESEARCH + WEB + AI TECH + ANALYSIS + SKILL EVOLUTION + SECURITY + RECOMMENDATION.

---

## Edge Cases
- **User sudah sebut skill**: hormati, tapi tetap cek dependensi & konflik sebelum eksekusi.
- **Skill dependen platform (Termux)**: verifikasi binary/path sebelum route; fallback ke tool CLI bila skill gagal.
- **Tool tidak tersedia**: turun ke low-resource mode / ganti tool, jangan gagal total.
- **Dua intent bertentangan dalam satu pesan**: clarifikasi minimal atau pilih intent primer + flag sisanya.
- **Skill menghasilkan requirement baru saat jalan**: lanjutkan dengan mengusulkan skill berikutnya (lihat §25).

## Common Mistakes / Anti-Patterns
| Anti-Pattern | Fix |
|---|---|
| Load semua skill sekaligus | Dynamic loading: hanya skill terpilih |
| Urutan skill sembarangan | Tentukan dependency order dulu |
| Abaikan konflik instruksi | Resolve prioritas explicitly |
| Tak ada fallback | Sediakan alternatif di tiap node kritis |
| Klaim selesai tanpa verify | Jalankan Verification Engine checklist |
| Infinite loop A↔B | Depth/attempt/time limit + state change check |
| Langsung execute skill broken | Health check dulu, tandai DISABLED |

## Failure Modes
- **Wrong routing**: intent ambigu → verifikasi klarifikasi; evaluasi post-task naikkan/turunkan priority.
- **Context overflow**: terlalu banyak skill → minimal set + dynamic load.
- **Silent failure**: exit 0 tapi output kosong → checklist EXISTENCE/CONTENT wajib.
- **Cascading dependency break**: dependency belum siap → load & verify dependency dulu.

## Red Flags
- Chaining tanpa analisis dependensi.
- Mengabaikan konflik skill.
- Tak ada jalur fallback.
- Tak ada verifikasi akhir.

## Rationalization Prevention
| Excuse | Reality |
|---|---|
| "Urutan bebas" | Dependency penting. |
| "Skill tak pernah konflik" | Mereka bisa; selesaikan prioritas. |
| "Pasti aman" | Verifikasi hasil akhir. |

## How to Use
1. **Parse intent** → tentukan skill yang dibutuhkan.
2. **Analyze dependencies** → selesaikan konflik/prioritas.
3. **Execute** skill dalam urutan dependency.
4. **Verify** hasil akhir; recover bila gagal.

## Quick Reference
| Situasi | Aksi |
|---|---|
| Banyak skill relevan | Orchestrate urutan optimal |
| Skill konflik | Resolve prioritas |
| Task kompleks | Dekomposisi ke sub-task |
| Skill gagal | Fallback ke alternatif |
| Selesai | Verifikasi hasil akhir |

## Golden Principle
Bantu user menyusun alur skill secara cerdas, tapi agent tetap bertindak di bawah oversight user: aksi berdampak selalu butuh persetujuan.
