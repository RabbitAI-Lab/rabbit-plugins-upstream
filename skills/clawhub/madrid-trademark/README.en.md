<sub>🌐 <a href="README.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · <b>English</b> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <a href="README.ar.md">العربية</a> · <a href="README.ja.md">日本語</a> · <a href="README.ru.md">Русский</a></sub>

<div align="center">

<img src="logo.png" alt="Hui Ning IP" width="150">

# Madrid Trademark · Madrid System Practice

> *"Ask once. Get a filing-ready Madrid practice answer."*
> *「一句话问清程序，拿回一份能直接用的实务方案。」*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.4.5-blue.svg)](https://github.com/huiningip/madrid-trademark)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](#install)
[![Madrid Members](https://img.shields.io/badge/Madrid%20Members-117%20%C2%B7%20133%20countries-green)](https://www.wipo.int/en/web/madrid-system/members/)
![Office-Neutral](https://img.shields.io/badge/Perspective-Office--Neutral-orange)

<br>

**An end-to-end Madrid System practice skill for trademark attorneys, IP lawyers and in-house counsel worldwide.**

<br>

Not a "what is the Madrid System" explainer — **something you can put in the case file**: fee schedules that hold up, deadline calculations in two separate tracks, ready-to-fill checklists and response memos, and treaty texts you can verify word by word.

The WIPO international phase works the same from any contracting party. This skill is written from an **office-neutral perspective** — the CNIPA/China bridge is an optional chapter, not the main line. Start from the USPTO, the EUIPO, the JPO or the CNIPA; it works the same.

Every fee figure, deadline and declaration in this skill carries a **data-as-of date and an official verification entry point**. When something cannot be found, it answers "none" — it does not invent one.

```
git clone https://github.com/huiningip/madrid-trademark ~/.workbuddy/skills/madrid-trademark
```

Agent-agnostic — installs into any agent that supports skills.

> 📣 **Volatile data is never hard-coded.** Fees, individual fees, contracting-party declarations, membership counts and legal texts each carry a "as-of date + review interval + official verification entry point". When the interval lapses, the skill prompts re-verification online and refuses to rely on search-engine cache values.

[What it does](#what-it-does) · [Install](#install) · [Core mechanisms](#core-mechanisms) · [Repository layout](#repository-layout) · [Limitations](#limitations)

</div>

---

<p align="center"><sub>

```
Base application/registration ──▶ Office of origin transmittal ──▶ WIPO formal exam ──▶ International registration date
                                                                                              │
                                          ┌───────────────────────────────────────────────────┴───────────────────────────────┐
                                          ▼                                                                               ▼
                        Refusal period per designated office: 12 / 18 / 25 months                     Central attack: 5-year dependency
                                          │                                                                               │
                              No refusal ⇒ protection granted                            Base fails ⇒ transform within 3 months,
                                                                                          filed directly with each designated office
```

</sub></p>

<p align="center"><sub>▲ One main line: application → transmittal → refusal-period monitoring → central-attack fallback. Every 🔴 checkpoint is enforced by the skill.</sub></p>

---

## Install

```bash
# Option 1: skills CLI
npx skills add huiningip/madrid-trademark

# Option 2: git clone (fallback when CLI sync misbehaves)
git clone https://github.com/huiningip/madrid-trademark ~/.workbuddy/skills/madrid-trademark
```

> **Self-check first.** This is not a single-file skill. `references/` (13 Markdown files + 2 official PDFs), `scripts/` (7 Python scripts + 2 JSON data files) and `templates/` (2 templates) are all referenced from the main text by `@` relative paths — miss one and the chain breaks.
>
> After installing, look at the install directory. If only `SKILL.md` is there and the subdirectories are missing, your sync tool grabbed a single file — reinstall with `git clone` above.
>
> Script self-test (Python 3.10+; offline scripts use the standard library only):
>
> ```bash
> py -B scripts/selftest.py     # 9 test groups — all green means a complete deployment
> ```

Then just talk to it in any skill-capable agent:

```
"Individual fee for Japan — calculate a 3-class filing for me"
"Is the China refusal response 15 or 30 days, and from when does it run?"
"My client's base registration from 2021 was just cancelled — can we still transform?"
"Renewal: registered 2016-07-01 for a 10-year term. Is it still in time?"
"Work out the refusal periods for US/JP/ID/IL — which ones need the 18-month watch?"
```

No forms. No wizards. No sign-up. Ask a question, get something that goes straight into the file.

---

## What it does

| Capability | Deliverable | Key constraint |
|-----------|-------------|----------------|
| International application | Procedure steps + `templates/madrid_application_checklist.md` | Gated on the 2-month transmittal period and reproduction specs |
| Fee calculation | Per-party amount list (basic / supplementary / complementary / individual fee) | **Two-track cross-check**: offline snapshot vs official live |
| Refusal-period calculation | 12 / 18 / 25-month countdown | Must check the party's declarations first — **never assume 18 months** |
| Response-deadline calculation | Per-party countdown (incl. China 15 / 30 days) | Recognises 6 starting points; **refuses** to count from receipt date when the official basis differs |
| Provisional refusal response | Procedure characterisation + strategy points + `templates/madrid_refusal_response_memo.md` | Distinguish ex officio refusal from third-party opposition first |
| Renewal management | Renewal window + grace-period surcharge | Grace surcharge = **50% of the basic fee (327 CHF)** |
| Change / assignment / limitation / renunciation | Filing route + registration-number rules (original number + capital letter) | Division and merger go through the office of origin |
| Central attack response | 5-year dependency test + 3-month transformation countdown | Transformation is filed **directly with each designated office**, not with WIPO |
| MGS goods & services check | Standardised-wording verification workflow | Wording must match WIPO MGS exactly |
| Contracting-party declaration review | 17 declaration categories, per-party list + safeguard-clause test | Declarations may be **ineffective** between dual-party states |
| China (CNIPA) bridge | Office-of-origin filing route + fast-track points | Optional chapter — non-China practitioners can skip it entirely |
| Treaty text verification | Full verbatim texts of Agreement / Protocol / Regulations / Administrative Instructions, in Chinese and English | Always cite the body text, never the summary |

---

## Coverage in detail

### Fees: two paths, neither a substitute for the other

`scripts/madrid_fee.py` is the **offline snapshot** — no network, no browser, built-in individual fees for 76 contracting parties, and it applies **announced rate changes** according to `--date`.

`scripts/madrid_feecalc_live.py` is the **official live measurement** — it drives the WIPO Fee Calculator with a real browser, returns authoritative per-party amounts, and is the deciding instrument when amounts are disputed.

> The official calculator is a JSF application: the party list and the results are both rendered by JavaScript, so it **cannot be scraped over plain HTTP**. Every checkbox click triggers an AJAX repaint and a single click may be swallowed, so the script retries up to 4 rounds ("check → read back the checked set → check any that did not take"). If the closing line reports "checked N / M" below M, the result is unusable by design.

```bash
# Offline: first-pass estimate for a quotation
py madrid_fee.py --countries ID,IL --classes 2 --date 2026/11/01

# Live: the deciding measurement when an amount is disputed
py madrid_feecalc_live.py --origin US --classes 1 --countries JP,ID,IL
```

**`--date` is the decisive parameter.** The WIPO individual-fees page shows only the *current* amount, whereas the calculator applies the rates in force on the *intended filing date*. Across a rate-effective date (commonly 1 November, 1 January) you must quote separately by intended filing date — the same application can be two different prices either side of that date. Measured example recorded: **effective 2026-11-01, Indonesia 91 → 125, Israel 471 → 503**.

### Deadlines: two tracks, and this is where practice goes wrong

The **refusal period** is the *office's* deadline to issue a notification, counted in months: baseline **12 months**, **18 months** where the party has made an Article 5(2)(b) declaration, and up to about **25 months** where an Article 5(2)(c) declaration is also in place and an opposition arises. For a subsequent designation it runs from the **date of recordal**.

The **response period** is the *holder's* deadline to answer a provisional refusal, counted in days or months, notified per country under Rule 17(7):

- China (CN): **15 days** for ex officio refusals / **30 days** for opposition-based refusals, running from receipt of the WIPO transmittal
- France (FR): 1 month / 2 months · United Kingdom (GB): 2 months · Germany (DE): 4 months · Japan (JP): 3 months
- United States (US): 6 months (ex officio) / 40 days (opposition, from the date of the TTAB order) · Thailand (TH): 90 days

> **Coverage warning.** The WIPO table covers only **38 members** (of 117), and the starting point differs across **6 variants** (holder's receipt / WIPO transmittal / office dispatch / WIPO receipt / 14th day after dispatch / TTAB order). **Not listed ≠ no response deadline.** When the official basis is not "date of receipt", `madrid_deadline.py` **refuses** to count down from the receipt date — counting from receipt overstates the time remaining — and requires the official starting date instead.

**Do not conflate 15/30 days with 12/18/25 months.** The former is the holder's response deadline; the latter is the office's deadline to issue a notification.

### Central attack: 3 months, and the direction matters

An international registration depends on the base application/registration for its first **5 years**; if the base is cancelled, the international registration falls with it. The remedy is Article 9quinquies: file a transformation request **directly with each designated office** within **3 months** of the cancellation, and the resulting national application keeps the **original international registration date and priority date**.

> The recurring mistake: filing the transformation request with WIPO. Transformation goes to the **designated offices**, not to the International Bureau.

### Declaration review: check the declaration, then set the strategy

Contracting parties may make 17 categories of declaration and notification, each affecting effect, fees and deadlines. When choosing designated parties, check in order: does it charge an individual fee → which refusal period applies → any special requirement (such as a declaration of intention to use) → whether division/merger is available → whether recordal of a licence has international effect.

> **Safeguard-clause warning.** Where both the designated party and the party of origin are **party to both the Agreement and the Protocol**, that party's declarations under Article 8(7) and Article 5(2)(b)/(c) are **ineffective in their mutual relations** (Protocol Article 9sexies(1)(b); Schedule of Fees items 2.4 / 5.3 / 6.4). A Chinese applicant designating France, Germany, Italy, Spain or Switzerland must verify this case by case.

### Treaty texts: verifiable word by word, re-fetchable in one command

The Agreement (18 Articles), the Protocol (16 Articles + 10 sub-rules), the Regulations (41 Rules + Schedule of Fees) and the Administrative Instructions (7 Parts, 19 Sections + Section 11bis) are all included as **full verbatim texts in Chinese** (WIPO Lex official translation) paired with the **official English texts**. When WIPO updates a text, re-fetch it with `wipo_lex_fetch.py`:

```bash
# Inspect the structure first, and verify the leading/trailing articles and article count
py -B wipo_lex_fetch.py --url https://www.wipo.int/wipolex/en/text/384637 --inspect
```

---

## Core mechanisms

### The volatile-data freshness gate

The hardest rule in the skill. Anything that can change — fees, individual fees, contracting-party declarations, membership counts, exchange rates, treaty versions — must be registered in the §3.0 table with an "as-of date + review interval + official verification entry point":

| Data item | As-of date | Review interval | Verification entry point |
|-----------|-----------|-----------------|--------------------------|
| Membership | 2026-09-23 | Monthly | WIPO members page |
| WIPO fees | Schedule of Fees, 2023-02-01 version | Quarterly | WIPO Schedule of Fees |
| Individual fee per party | 2026-08-23 | Monthly | WIPO individual fees page |
| Party declarations | 2026-03-15 | Monthly | WIPO declarations page |
| Response-time table | 2026-08-28 | Monthly | WIPO response time limits page |
| CHF exchange rate | **not built in** | Before every payment | Live rate / Fee Calculator |

When the review interval has lapsed, or the user explicitly asks, the skill **must verify online before answering**. What cannot be found is answered with "none".

### Single-source-of-truth for data

The same data is never stored twice, so two competing versions cannot exist:

- Fees → `references/madrid-fees.md` (machine-readable mirror: `scripts/madrid_fee_data.json`)
- FAQ and counter-examples → `references/madrid-faq.md`
- Declarations → `references/madrid-declarations.md` (17 categories, numbered)

Consistency between each "human-readable ↔ machine-readable" pair is checked per party by dedicated `selftest.py` cases — edit the document without syncing the data and the self-test goes red.

### Two deadline tracks, strictly separated

One command covers both tracks, with the logic kept apart:

- Default mode computes the **refusal period** (12 / 18 / 25 months) — it defaults to 12 months and demands declaration verification; **18 months requires an explicit `--declared-18`**. Claiming opposition-based extension on top of the 12-month baseline is rejected outright (Article 5(2)(c) presupposes an 18-month declaration).
- `--respond` computes the **response period** — built-in WIPO Rule 17(7) data for all 38 members, with the 6 starting-point variants resolved.

### Output-format discipline

The skill's own reference material may use Markdown knowledge tables; but **text delivered to the user after a skill call must not use Markdown tables** — it uses line-by-line "item: value (legal basis)", per-party `·` bullets, or indentation-based alignment instead. Amounts and deadlines never drop their unit or legal basis; anything volatile is flagged as needing a refresh.

### Counter-example library

`references/madrid-faq.md` carries 16 high-frequency counter-examples, including corrections of this skill's own historical errors. Among the most frequent and most damaging: assuming an 18-month refusal period; conflating complementary and individual fees; computing the grace surcharge as "50% of the total payable"; paying on the last day of the grace period; amending the goods list during renewal; filing a transformation request with WIPO after a central attack.

> The bottom line: in Madrid practice, **deadlines and formal compliance matter more than the strength of your arguments**. Miss a deadline and the right is, as a rule, irrecoverable.

---

## Relationship to generic AI chat

Ask a general-purpose model "what are the Madrid fees?" and you get a number with **no as-of date, no traceable source, and possibly expired**. The difference here is threefold:

| | Generic AI chat | madrid-trademark |
|---|---|---|
| Fee figures | A snapshot from training data, no as-of date | As-of date + official entry point + live re-measurement |
| Refusal period | Frequently "18 months" | 12-month baseline, declaration-driven; 25 months has strict preconditions |
| Missing data | Tends to invent a plausible answer | Answers "none" |
| Deadline arithmetic | Mental, error-prone | `madrid_deadline.py` resolves 6 starting-point variants |
| Legal citations | Paraphrased, unverifiable | Verbatim Agreement / Protocol / Regulations / Administrative Instructions, greppable |
| Deliverable | A paragraph of prose | Checklist + response memo + per-party fee breakdown |

Generic chat is **better conversation**; this skill is about **making the "can't find it / can't get it right" uncertainty disappear**.

---

## Data and provenance

- **Zero fabrication.** What cannot be found is answered with "none" — never estimated, never padded with a placeholder.
- **No telemetry.** The skill is a purely local file bundle: it sends nothing out and contains no keys.
- **Citations are verifiable.** All treaty texts come from official WIPO Lex pages, and the fetching script `wipo_lex_fetch.py` is shipped so you can re-fetch and re-verify. The "key points and errata" appendices are skill-compiled material, not official text — **always cite the body text**.
- **Reproducible.** Every date-calculation script supports `--today` for reproduction, so deadline results can be traced back.
- **Disclaimer.** Script output is an estimate and a prompt; the WIPO / CNIPA official notification and official invoice govern.

---

## Limitations

Being straight about what it does not do:

- **It does not cover article-by-article interpretation of designated parties' substantive trademark law or litigation strategy.** National law (specific provisions of the US Lanham Act, the EU trade mark regulation, national refusal-review practice) must be referred to local law or local counsel.
- **It does not handle national or regional trademark applications.** Direct filings with the USPTO, EUIPO or JPO (outside the Madrid route) are outside the main flow and appear only as a Madrid-interface comparison.
- **It does not make subjective similarity judgements or predict success rates.** It provides a refusal-response framework and templates; it does not predict registrability, conflict risk or case outcomes.
- **It does not fetch live exchange rates.** The CHF rate is volatile and must be verified before each payment.
- **It does not replace professional judgement.** This is a practice aid, not an opinion with legal effect.
- **Without the file it cannot give a targeted plan.** Provide the refusal notification, registration number and designated parties first.

**How to ask for the best answer:** state the transaction type (application / renewal / refusal response / change or assignment / transformation / fees / deadlines) + the key facts (designated parties, number of classes, base status, registration date or number, whether a refusal has been received and from where) + the expected deliverable (fee estimate / deadline countdown / response template / procedure steps / risk checklist).

---

## Repository layout

```
madrid-trademark/
├── SKILL.md                          # Main document (read by the agent; six-part structure: role / task / context / process / rules / output format)
├── README.md                         # Simplified Chinese (default)
├── README.zh-Hant.md                 # Traditional Chinese
├── README.en.md                      # English (this file)
├── README.fr.md                      # French
├── README.es.md                      # Spanish
├── README.ar.md                      # Arabic (RTL)
├── README.ja.md                      # Japanese
├── README.ru.md                      # Russian
├── LICENSE                           # MIT License
├── logo.png                          # Brand mark (README header)
├── references/                       # 15 items: 13 Markdown + 2 official PDFs
│   ├── madrid-agreement.md / -en.md           # Madrid Agreement (18 Articles, full text zh/en)
│   ├── madrid-protocol.md / -en.md            # Madrid Protocol (16 Articles + 10 sub-rules, full text zh/en)
│   ├── madrid-regulations.md / -en.md         # Regulations (41 Rules + official footnotes, full text zh/en)
│   ├── madrid-admin-instructions.md / -en.md  # Administrative Instructions (7 Parts, 19 Sections + 11bis, zh/en)
│   ├── madrid-fees.md                         # Single source of truth for fees (individual fees, 76 parties)
│   ├── madrid-declarations.md                 # Single source of truth for declarations (17 categories + 38-member response times)
│   ├── madrid-faq.md                          # FAQ + 16 counter-examples + article index
│   ├── madrid-goods-services-classification.md    # Classification guide digest (5th edition, 2026)
│   ├── madrid-fast-track-examination-cnipa.md     # CNIPA fast-track practice points
│   ├── madrid-efiling-applicant-guide.pdf         # WIPO e-Filing applicant guide (official, 43 pp.)
│   └── madrid-goods-services-classification-guide.pdf  # Official classification review guide (5th ed.)
├── scripts/                          # 9 items: 7 Python + 2 JSON
│   ├── madrid_fee.py                 # Fee calculator (offline snapshot, --date applies effective-date changes)
│   ├── madrid_fee_data.json          # Machine-readable fee mirror (aligned per party with madrid-fees.md)
│   ├── madrid_deadline.py            # Deadline calculator (refusal 12/18/25 months + response, 38 members)
│   ├── madrid_response_times.json    # Response-time data (full WIPO Rule 17(7) table + 6 starting points)
│   ├── madrid_renewal.py             # Renewal window and grace-period surcharge
│   ├── madrid_feecalc_live.py        # Live fee measurement (browser-driven official Fee Calculator; deciding tool)
│   ├── wipo_lex_fetch.py             # WIPO Lex verbatim treaty-text fetcher (to Markdown)
│   ├── madrid_dateutil.py            # Shared date utilities (month arithmetic, month-end, leap-year fallback)
│   └── selftest.py                   # 9 test groups (incl. two consistency comparisons)
└── templates/                         # Copy before use; do not edit the originals in place
    ├── madrid_application_checklist.md      # Pre-filing self-check list for the MM2
    └── madrid_refusal_response_memo.md      # Provisional refusal response memo
```

> **Structure rule.** Strictly 2 levels deep (level 1 = `SKILL.md` / `references/` / `scripts/` / `templates/`; level 2 = files within each), with no deeper nesting.
> **Encoding.** Markdown files are pure CRLF, no BOM; `.py` and `.json` under `scripts/` are LF, UTF-8 without BOM.
> **Maintenance discipline.** Any change to a fee figure must be mirrored across `references/madrid-fees.md` and `scripts/madrid_fee_data.json`, and `py scripts/selftest.py` must pass all cases before committing.

---

## Origin

The pain of a Madrid case is very concrete: **the same thing is written once in the Agreement, once in the Protocol, once in the Regulations, once in the Schedule of Fees, and once again in each contracting party's declarations** — and a revision to any one of them can invalidate last week's correct position. A fee change, one more party declaring an extended refusal period, one new member: in practice, that means re-verifying everything.

So the four layers of legal text (Agreement / Protocol / Regulations / Administrative Instructions), together with the Schedule of Fees, the declarations page and the official guides, were fetched into full verbatim texts; volatile data was stamped with freshness dates; and everything computable — deadlines, fees — was written into reproducible scripts. The goal is to turn "verification" from an afternoon's work into a single call.

---

## License

Released under the **MIT License** ([LICENSE](LICENSE)). You are free to **use, modify and distribute** this project, **including commercially** — internal company use, delivery in client case work, derivative works and redistribution all require no prior authorisation, no fee and no notice. Attribution is not required, though it is welcome.

Copyright **Hui Ning IP (辉宁知识产权)**.

**Scope note.** The MIT licence covers this skill's own code (`scripts/`) and documentation (`SKILL.md`, the READMEs in eight languages, the skill-compiled material in `references/`, and `templates/`). The WIPO Lex official treaty texts reproduced verbatim under `references/`, and the two official WIPO/CNIPA PDFs, remain the property of their issuing bodies; they are bundled for verification convenience and are **not covered by this licence** — observe the source terms when using them.

Any conclusion produced with this skill should be reviewed against the designated party's national law and the facts of the case before it is relied upon; as a practice aid, it does not constitute legal advice.

---

## Contact

Maintained by **Hui Ning IP (辉宁知识产权)** — a Chinese patent and trademark attorney team covering patent prosecution, trademark prosecution and international IP services.

- Issues are welcome for outdated data, citation errata or script problems. **When reporting a volatile-data discrepancy, please attach the official page URL and a screenshot**; the as-of date will be updated once verified.
- If you know a local practice position in a particular contracting party, please share it — this skill is office-neutral by design, and those jurisdictional differences are exactly what it most needs.
