🌐 [中文](README.md) · [繁體中文](README.zh-Hant.md) · **English** · [Français](README.fr.md) · [Español](README.es.md) · [العربية](README.ar.md) · [日本語](README.ja.md) · [Русский](README.ru.md)

<p align="center"><img src="logo.png" alt="Hui Ning IP" width="150"></p>

# Hague Design System · International Design Registration Practice Skill

> *"Ask once. Get a filing-ready Hague design practice answer."*
> *「一句话问清程序，拿回一份能直接用的海牙外观设计实务方案。」*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.10.8-blue.svg)](references/changelog.md)
![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)
[![Hague Members](https://img.shields.io/badge/Hague%20Members-83-green)](https://www.wipo.int/en/web/hague-system)
![No-Fabrication](https://img.shields.io/badge/Principle-No--Fabrication-orange)

**An end-to-end Hague System practice skill for design attorneys, IP lawyers and in-house counsel worldwide — centred on the WIPO international phase and usable from any contracting party's perspective, with an optional CNIPA/China bridge chapter.**

Not an explainer: it delivers check paths for filing and examination milestones, clause-by-clause verifiable legal sources (Geneva Act / Common Regulations / Administrative Instructions / the Guide), hard specifications for reproductions, unity of design and priority, and re-checkable fee and deadline figures (with a bundled fee calculator script).

Built on the universal Agent Skills format (`/SKILL.md`); works with any agent that supports skills.

[What it does](#what-it-does) · [Install](#install) · [Core mechanisms](#core-mechanisms) · [Repository layout](#repository-layout) · [Limitations](#limitations)

---

## Install

### Option 1: sync script (recommended)

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# Common options
py -3 scripts/sync_to_local.py --dry-run                # preview, no writes
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # custom skills directory
```

The script syncs this repository as a single skill into your local skills directory (default `~/.workbuddy/skills`, installed as `hague-design-system/`), one way: new or changed files are overwritten, stale files are removed, and **local metadata such as `_user_meta.json` is preserved**; repo-level files (README, LICENSE, logo, etc.) are never installed into the skills directory.

### Option 2: manual copy

Copy the whole repository folder into your skills directory (e.g. `~/.workbuddy/skills/`) and rename it to `hague-design-system`, then restart or reload the app.

> ⚠️ This is a multi-file skill: the knowledge base under `references/` (Act and Common Regulations, Administrative Instructions, the Guide to the Hague System, the optional China chapter, etc.) is referenced from `SKILL.md` via relative `@` paths — **one missing file breaks the chain**. Copy whole directories; do not take `SKILL.md` alone.

## What it does

| Area | Description |
|------|------|
| International application | Entitlement; DM/1 and eHague filing; reproductions requirements; unity of design; priority; filing routes and procedural milestones |
| Registration & publication | Formality examination and corrections; international registration and registration date; publication and deferment; withdrawals |
| Examination & remedies | Responding to refusals by designated Offices; statements of grant and their effect; invalidation; post-refusal routes |
| Renewal & changes | Term and renewal (including grace period); change in ownership, holder's data, representative, limitation, renunciation |
| Fees | The seven fee transaction types (application / renewal / change in ownership / change in holder's data / change in creator's name and address / limitation / renunciation); Hague fee calculator; CHF fee structure; bundled fee calculator script |
| Search | DesignDB prior-design and legal-status search |
| Optional · China chapter | China's declarations; CNIPA examination and refusal remedies; transmittal and system operations; divisional filings; CNY notes (practitioners outside China may skip it entirely) |

## Core mechanisms

1. **Globally neutral core**: the WIPO international phase (common to all contracting parties) is the main body; the CNIPA/China bridge is an optional chapter that non-China practitioners can skip entirely;
2. **Single-point legal source and data**: volatile data such as fees and declarations converges to a single authoritative source, with version history and a file index kept in one place (`changelog.md`, `11-file-index.md`) to avoid divergent figures;
3. **Progressive disclosure**: long-form texts (including the 286 KB Guide to the Hague System) live in `references/`, load on demand and are navigable via a line-number index, without blowing up the context window;
4. **"None" when not found**: uncertain information is flagged directly — no invented provisions, deadlines or fee figures; delivered answers never use Markdown tables (lists and inline definitions instead).

## Repository layout

```text
HAGUE-SKILLS/                        # Repo root = skill root (single-skill repository)
├── SKILL.md                         # Control plane: role / task / context / process / rules / output
├── references/                      # 12 knowledge files (incl. optional China chapter, changelog, file index)
├── scripts/                         # Skill scripts (fee calculator, fetch helper) + sync_to_local.py
├── README.md                        # 简体中文 (default)
├── README.zh-Hant.md                # 繁體中文
├── README.en.md                     # English (this file)
├── README.fr.md                     # Français
├── README.es.md                     # Español
├── README.ar.md                     # العربية (RTL)
├── README.ja.md                     # 日本語
├── README.ru.md                     # Русский
├── LICENSE                          # MIT License
└── logo.png                         # Brand mark (README header)
```

- The repository root is the skill root; once installed it is a strictly **2-level structure** (`SKILL.md` / `references/` / `scripts/`), compliant with the official WorkBuddy skill structure;
- Repo-level files (`README*.md`, `LICENSE`, `logo.png`, `scripts/sync_to_local.py`) are never installed into the skills directory;
- Skill files: **CRLF, UTF-8 without BOM**.

## Data and provenance

- Legal sources follow the **current official WIPO / CNIPA versions**; the skill records data-as-of dates and recommended re-check cycles (§3.0 timeliness list);
- For volatile data (fees, individual designation fees, declarations, exchange rates), re-check the latest official announcements or the fee calculator before use in a case file;
- Output is practice reference only — **not legal advice**.

## Limitations

- No substitute for official or case-specific judgment: deadlines, fees and procedural conclusions are governed by the designated Office's notices and official announcements;
- No fabrication: data that cannot be found is answered as "none";
- Legal coverage focuses on the Hague System procedure and common rules; the substantive law and examination practice of each designated contracting party follow that party's official positions.

## License

[MIT](LICENSE) © 2026 Hui Ning IP（辉宁知识产权）.

- The skill content itself (curation and annotations in `SKILL.md` and `references/`) is under MIT;
- Official WIPO texts reproduced or quoted in `references/` (Geneva Act, Common Regulations, Administrative Instructions, the Guide, etc.) remain the property of WIPO and are not covered by this license.

## Contact

- Questions and suggestions: open an Issue in this repository;
- Built and maintained by Hui Ning IP (a Chinese patent attorney team).
