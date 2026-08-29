---
name: skill-curator
description: "Gunakan saat user ingin audit atau mengkurasi skill OpenClaw — deteksi bahasa god-mode (PRIME DIRECTIVE/overrides all), cek keberadaan _meta.json/CHANGELOG/GUARDRAILS, temukan kebocoran token/secret (dengan allowlist token legitimate), atau hasilkan proposal perbaikan massal."
metadata:
  openclaw:
    emoji: "🧹"
    version: 1.1.1
    requires:
      bins: ["python3"]
---

# 🧹 Skill Curator — Agent Pengkurasi Skill (Production-grade)

Agent meta yang **membantu mengaudit** skill OpenClaw di workspace (read-only scan). Bukan menjalankan skill dan bukan mengubah skill — ia hanya **memastikan skill tetap sehat, aman, dan siap publish** melalui proposal.

## Kapan Dipakai
- User: "audit semua skill", "cari yang god-mode", "cek skill yang belum punya GUARDRAILS"
- Sebelum publish batch ke ClawHub
- Periodic maintenance (cron bulanan)

## Cara Kerja
Jalankan `scripts/curator.py` — ia scan `$WORKSPACE/skills/*`, lalu untuk tiap skill:
1. **Frontmatter** valid (`name`, `description` task-scoped)
2. **_meta.json** (version untuk publish)
3. **GUARDRAILS** section ada
4. **CHANGELOG** ada
5. **God-mode language** (`PRIME DIRECTIVE`, `overrides all`, `authority too broad`, `BEFORE every response`, `you MUST`, `mandatory`)
6. **Token/secret leak** — dengan **allowlist** token legitimate (mis. `sk-244…0e53` di `web-search-9routers-backup` TIDAK diflag). Curator hanya membaca file lokal; tidak mengirim apa pun ke jaringan.
7. **Hidden unicode** (ZWJ/bidi) — potensi serangan
8. **Exec/network raw** (`exec(`, `subprocess`, `curl`, `rm -rf`)
9. **Duplicate slug** (nama skill kembar di workspace)
10. **Namespace protection** — `openclaw-*` dilindungi, jangan rename/merge sembarangan
11. **Decorative emoji** — di body (kecuali `∞` & `X∞` & `❌` yang sengaja)

Output: **quality score 0-100** + **severity findings** (CRITICAL/HIGH/MEDIUM/LOW/INFO) + ringkasan + (opsional) JSON.

## ⚠️ GUARDRAILS (Wajib — batasi otoritas)
- **JANGAN** ubah isi skill tanpa instruksi eksplisit user. Curator hanya **scan & proposal**, bukan auto-edit.
- **JANGAN** sentuh file token/secret (`openclaw.json`, `models.json` berisi apiKey, env berisi token).
- **JANGAN** hapus skill — hanya laporkan; penghapusan butuh konfirmasi user (atau trash, bukan `rm`).
- **LINDUNGI** namespace `openclaw-*` — jangan rename/merge tanpa consent owner.
- **PRESERVE** marker `X∞` & `❌` (bukan korupsi) dan token legitimate di allowlist.
- Ikuti ASK/STOP/VERIFY: konfirmasi sebelum apply proposal massal.

## CHANGELOG
- v1.1.1 (2026-08-25): Frontmatter multiline valid (hilangkan inline JSON); lunakkan wording "MENGELOLA" → "membantu mengaudit"; tegaskan curator read-only (tidak ada transmisi jaringan). Kepatuhan SkillSpector.
- v1.1.0 (2026-08-25): Upgrade level tertinggi — quality score, severity, allowlist token legitimate, proteksi namespace `openclaw-*`, deteksi unicode tersembunyi/exec/duplicate-slug/description non-task-scoped, preserve `X∞`/`❌`.
- v1.0.0 (2026-08-25): Rilis perdana — scanner audit skill dasar.
