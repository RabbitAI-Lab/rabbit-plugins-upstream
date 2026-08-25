---
name: web-search-9routers-backup
description: "Gunakan saat user ingin mengambil/membaca URL tapi skill `9router-web-search` utama gagal, atau butuh fallback web fetch via layanan internal 9Router di `localhost:20128`. Aktif saat user minta "fetch URL pakai backup" atau primary web search error."
metadata:
  openclaw:
    version: 1.1.0
---

<!-- ===== X∞ COMPLIANCE LAYER (auto-applied by skill-architecture-standard) ===== -->
# web-search-9routers-backup — X∞ Compliance Layer

## 1. IDENTITY
Skill milik user: `web-search-9routers-backup`. Mengikuti Skill Architecture Standard X∞ (wajib).

## 2. PURPOSE
Menyediakan fallback web fetch via layanan internal 9Router (localhost:20128) saat skill web-search utama gagal—dengan token dari env $NINEROUTER_KEY, tidak pernah hardcode.

## 3. METADATA
- version: 1.0.0
- name: web-search-9routers-backup
- standard: Skill Architecture Standard X∞ (21-node)
- scope: lihat body domain
- depends_on: tidak ada (mandiri)

## 4. TRIGGER ENGINE
Aktif ketika user meminta hal yang cocok dengan deskripsi di atas.
Negative trigger: di luar scope deskripsi.

## 5. CONTEXT ENGINE
Baca OS/ARCH/runtime sebelum bertindak. Termux Android ARM64 ≠ Ubuntu x86_64.

## 6. DECISION POLICY
IF uncertainty VERIFY
IF high risk ASK/STOP
IF tool unavailable ALTERNATIVE
IF action fails RECOVER

## 7. REASONING POLICY
Evidence-first. Bedakan FAKTA vs HIPOTESIS. Confidence: CONFIRMED/LIKELY/POSSIBLE/UNKNOWN.

## 8. EXECUTION POLICY
Ambil tindakan relevan, lalu VERIFY. Jangan klaim sukses sebelum diverifikasi.

## 9. TOOL POLICY
Pilih tool berdasar kebutuhan+konteks. Jangan asal panggil semua tool.

## 10. MEMORY POLICY
Ingat hal relevan; abaikan noise. Retrieve saat dibutuhkan, update bila berubah.

## 11. VERIFICATION ENGINE
ACTION VERIFY SUCCESS? Jika tidak: DIAGNOSE RETRY/CHANGE STRATEGY.

## 12. ERROR RECOVERY
transientretry; timeoutbackoff; authcredential check; dependencydiagnosis; unknowninvestigate.

## 13. SECURITY GUARDRAILS
NEVER log secret. REDACT API KEY/TOKEN/PASSWORD/SECRET sebelum simpan. PII: MINIMIZEREDACTHASH.

## 14. EVALUATION
Self-eval: capai goal? terverifikasi? ada asumsi? ada gagal? Kirim ke Agent Evaluation Engine.

## 15. OBSERVABILITY
Emit: START/PROGRESS/TOOL CALL/ERROR/RETRY/SUCCESS/FAILURE + TRACE_ID (tanpa secret).

## 16. PERFORMANCE OPTIMIZATION
FULLOPTIMIZEDLOW RESOURCE mode bila terbatas. Prioritas: TASK>SAFETY>RELIABILITY.

## 17. SELF-IMPROVEMENT
USEOBSERVEEVALUATEFIND WEAKNESSIMPROVETESTNEW VERSION (via evaluasi+regresi).

## 18. VERSIONING
Semver. Perubahan struktur = MAJOR. CHANGELOG wajib.
**CHANGELOG**
- 1.1.0 — Light upgrade: frontmatter `description` rusak (berisi teks changelog) diganti deskripsi trigger; Node 2 (PURPOSE) & Node 3 (METADATA) diisi; `metadata.openclaw.version` diset 1.1.0. Body domain dipertahankan.

## 19. COMPATIBILITY
Tahu OS/ARCH/RUNTIME/versi/tool/API tersedia.

## 20. KNOWLEDGE SOURCES
Trust hierarchy: OFFICIAL>PRIMARY>REPUTABLE>COMMUNITY>UNKNOWN. Tandai VERIFIED/LIKELY/UNCERTAIN/OUTDATED/CONFLICTING.

## 21. EXIT CONDITIONS
Berhenti pada: SUCCESS/FAILURE/BLOCKED/NEED USER/NEED CREDENTIAL/NEED TOOL/NEED VERIFICATION.
<!-- ===== END X∞ COMPLIANCE LAYER ===== -->



# Web Search 9routers Backup Skill

## When to Use

User provides a URL to fetch/read, or the primary `9router-web-search` skill fails. This wraps the internal 9Router backup web fetch service on `localhost:20128`.

## Usage

Provide URL and optional parameters to fetch content via the internal 9routers backup web fetch service.

### Parameters

- `url`: target URL to fetch
- `model`: model to use (default: exa)
- `format`: output format (html or text, default: html)
- `max_characters`: maximum characters to return (0 for unlimited, default: 0)
- `authorization_token`: bearer token (if not set, uses default from environment or config)

### Example

```bash
curl -X POST http://localhost:20128/v1/web/fetch \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $NINEROUTER_KEY" \
 -d '{"model":"exa","url":"https://example.com","format":"html","max_characters":0}'
```

## Implementation Notes

- This skill wraps the internal web fetch endpoint.
- Ensure the endpoint is accessible (localhost:20128) within the OpenClaw environment.
- The token may need to be refreshed periodically.

## Error Handling

| Scenario | Response |
|---|---|
| Connection refused on :20128 | 9Router backup service is down — report to user, suggest primary skill |
| HTTP 401/403 | Token expired — ask user to refresh `NINEROUTER_KEY` |
| Empty content | Retry with `format:text` or report page as unreadable |

## Red Flags — STOP

- Never hardcode the bearer token in commands or output — use `$NINEROUTER_KEY`
- Never fetch URLs from untrusted user input without confirmation (SSRF risk)

## Version

sha256:PLACEHOLDER
