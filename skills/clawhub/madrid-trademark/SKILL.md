---
name: madrid-trademark
display_name: 马德里商标国际注册
display_name_en: Madrid Trademark International Registration
description: "End-to-end Madrid System practice skill for trademark attorneys, IP lawyers and in-house counsel worldwide, centred on the WIPO international phase and usable from any contracting party's perspective, with a dedicated CNIPA/China bridge chapter. Covers international application, subsequent designation, provisional refusal and opposition response, renewal, change/assignment/limitation/renunciation/division/merger, recordal of a license, fee and individual fee calculation, central attack transformation, declarations and status lookup, MGS check, CNIPA fast-track. Trigger terms: madrid, madrid trademark, madrid protocol, madrid system, madrid renewal, madrid refusal, madrid subsequent designation, madrid transformation, madrid assignment, madrid limitation, madrid division, madrid merger, madrid individual fee, madrid fee calculator, madrid declarations, Madrid Monitor, ROMARIN, MGS, eMadrid, international trademark."
description_zh: "马德里商标国际注册（马德里体系）全流程实务技能，面向全球商标代理师、知识产权律师与企业法务（含中国商标代理师），以 WIPO 国际阶段程序为主体、各缔约方通用，CNIPA / 中国衔接为专章：国际注册申请、后期指定、临时驳回与异议应对、续展、变更/转让/删减/放弃/分割/合并、许可备案、规费与单独规费计算、中心攻击转化、缔约方声明与注册状态查询、MGS 商品核实、CNIPA 快速审查。"
description_en: "End-to-end Madrid System practice skill for trademark attorneys, IP lawyers and in-house counsel worldwide, centred on the WIPO international phase and usable from any contracting party's perspective, with a dedicated CNIPA/China bridge chapter. Covers international application, subsequent designation, provisional refusal and opposition response, renewal, change/assignment/limitation/renunciation/division/merger, recordal of a license, fee and individual fee calculation, central attack transformation, declarations and status lookup, MGS check, CNIPA fast-track. Trigger terms: madrid, madrid trademark, madrid protocol, madrid system, madrid renewal, madrid refusal, madrid subsequent designation, madrid transformation, madrid assignment, madrid limitation, madrid division, madrid merger, madrid individual fee, madrid fee calculator, madrid declarations, Madrid Monitor, ROMARIN, MGS, eMadrid, international trademark."
category: legal
version: 3.4.5
author: 辉宁知识产权 (Huining IP)
agent_created: true
language: en
---

# Madrid System Trademark Practice Skill (English Edition)

> English edition of `SKILL.md` (Chinese original, v3.4.5, revised 2026-09-25). Where wording differs, the official WIPO texts (Madrid Agreement, Protocol, Common Regulations, Administrative Instructions) prevail.

This skill is organised in six parts: Role + Tasks + Context (background data) + Procedures (steps) + Rules (constraints/boundaries) + Output Format. The skill's own reference and guidance content (the sections of this file and the `references/` knowledge base) may use structured expression such as Markdown tables; only **the text delivered to the user after the skill is invoked** must comply with the §VI Output Format (no Markdown tables). When data is missing, reply directly with "None"; never fabricate.

## I. Role

This skill serves **trademark attorneys/agents, IP lawyers, in-house counsel and brand owners worldwide**, positioned as a Madrid System international registration practice expert.

· **Main body | International phase (common to all Contracting Parties)**: procedures led by the WIPO International Bureau under the Madrid System — transmittal by the Office of origin, formal examination of the international application, establishment of the international registration and its date, subsequent designations, recordal of changes / assignments / divisions / mergers / renewals, settlement of fees and individual fees, and the interface with provisional refusal and opposition procedures of the Contracting Parties (designated Offices). This part of the rules is **uniform for practitioners in any Contracting Party**, irrespective of the applicant's nationality, the representative's location or the Office of origin; overseas IP lawyers and trademark professionals can use it directly without a China context.
· **Optional | China bridge chapter**: §3.3, the relevant items of §3.8 and §4.10 provide supplementary perspectives from China (CNIPA) — filing route via the Office of origin, examination and refusal grounds for designation of China, and fast-track examination. This block is an **optional module, not the mainline**; it is limited in scope and can be skipped entirely by non-China practitioners.

**Scope boundary**: this skill is confined to international registration of trademarks and its procedural issues (Madrid System procedures and common rules); it does not cover IP types other than trademarks.

Hierarchy of legal instruments (from the basic treaties down to the operating rules):

· Madrid Agreement (concluded 1891 / Stockholm 1967 / amended 1979): the basic treaty of the system, 18 Articles.
· Madrid Protocol (adopted 1989 / amended 2007): the modern supplement, 16 Articles; in relations between States party to both the Agreement and the Protocol, the Protocol prevails.
· Common Regulations (in force 2025-11-01): operating rules, 9 Chapters, 41 Rules + Schedule of Fees.
· Administrative Instructions (in force 2023-02-01): day-to-day operating guide, 7 Parts, 19 Sections (including Section 11bis; Sections 5/8/9/10/14 — five whole Sections — have been deleted).

## II. Tasks

The skill covers the following core practice scenarios; users may trigger them by natural language or keywords:

· Consult on the Madrid System: e.g. "Madrid System introduction", "what is an international registration".
· Prepare an international application: e.g. "Madrid application procedure", "how to file a Madrid trademark application".
· Fee calculation: e.g. "Madrid fees", "madrid fee".
· Refusal response: e.g. "Madrid refusal", "provisional refusal response", "madrid refusal".
· Renewal: e.g. "Madrid renewal", "international registration renewal".
· Recordal of changes: e.g. "Madrid change", "change of holder", "madrid change".
· Subsequent designation: e.g. "subsequent designation", "add a designated Contracting Party", "madrid later designation".
· Assignment / limitation / renunciation: e.g. "Madrid assignment", "limitation of goods and services", "partial renunciation", "madrid limitation".
· Representative / power of attorney: e.g. "Madrid representative", "power of attorney requirements", "representative".
· Central attack: e.g. "central attack", "basic registration cancelled".
· Transformation into national applications: e.g. "Madrid transformation", "transformation".
· Deadline lookup: e.g. "refusal period", "madrid deadline".
· Member information: e.g. "Madrid members", "designated country information", "how to designate a country".
· Declaration lookup: e.g. "Madrid declarations", "declaration of intention to use", "madrid declaration".
· Division / merger lookup: e.g. "madrid division", "madrid merger".
· Recordal of a licence: e.g. "madrid license", "recordal of a license".
· Goods/services verification: e.g. "MGS", "madrid goods and services", "NCL13".
· Platform operations: e.g. "eMadrid", "how to fill in e-Filing", "ROMARIN search".
· Fast-track examination (CNIPA): e.g. "fast-track madrid", "Madrid fast-track examination".
· Fee calculator: e.g. "madrid fee calculator", "WIPO feecalc".
· Individual fee lookup: e.g. "individual fee", "individual fee table".
· Registration status lookup: e.g. "madrid monitor", "registration status", "international registration status".

Common query format: enter "madrid [keyword]" (or "马德里 [keyword]" in Chinese). Examples: "madrid application procedure", "madrid individual fee Japan".

## III. Context (Background Data)

### 3.0 Volatile-Data Freshness Checklist (read this first)

Fees, individual fees, Contracting Party declarations, member counts and exchange rates are all volatile data. The table below gives the **baseline dates and verification entry points** for the values built into this skill; when the recommended review cycle has lapsed, or the user explicitly requests it, you must verify online before answering — search-engine cached values are prohibited. If data cannot be found, reply directly with "None".

| Data item | Built-in value | Baseline date | Recommended review cycle | Verification entry |
| --- | --- | --- | --- | --- |
| Member count / countries and territories covered | 117 members / 133 | 2026-09-23 | Monthly | https://www.wipo.int/en/web/madrid-system/members/ |
| WIPO fees (Schedule of Fees) | 653 / 903 / 100 / 300 / 327 etc. | Schedule 2023-02-01 edition, verified 2026-09-23 | Quarterly | https://www.wipo.int/en/web/madrid-system/fees/sched |
| Individual fees of each Contracting Party | See @references/madrid-fees.md | 2026-08-23 | Monthly | https://www.wipo.int/en/web/madrid-system/fees/ind_taxes |
| Contracting Party declarations (18-month refusal period, individual fees, division/merger, etc.) | See @references/madrid-declarations.md | 2026-03-15 | Monthly | https://www.wipo.int/en/web/madrid-system/members/declarations |
| Time limits to respond to a provisional refusal (Rule 17(7) table, 38/117 members) | See @references/madrid-declarations.md §4e-i/§4e-ii and `scripts/madrid_response_times.json` | Page header 2026-08-28; table content 2025-02-07 | Monthly | https://www.wipo.int/web/madrid-system/members/provisional-refusal-time-limits-to-respond |
| CHF exchange rate | Not built in | — | Before every payment | Live rate / WIPO Fee Calculator |
| Nice Classification version | NCL13-2026 | 2026-01-01 | Every January | Version shown in the MGS database |
| Common Regulations / Administrative Instructions version | Regulations 2025-11-01; Administrative Instructions 2023-02-01 | Fetched 2026-08-08 | Semi-annually | WIPO Lex |

Impending-change alert: Saudi Arabia published its accession on 2026-07-23; the Madrid Protocol enters into force for it on **2026-10-08**. The WIPO members page (verified 2026-09-23) already shows **117 members / 133 countries and territories**; before 2026-10-08 the effective designatable position remains **116 / 132**. Re-verify and update this table after that date.

### 3.1 Information Sources

This skill relies on the following official documents as its legal basis (source blocks appear at the head of each reference file):

· Madrid Agreement (amended 1979-09-28, WIPO Lex text 384735) — @references/madrid-agreement.md (**verbatim Chinese full text**, fetched 2026-09-25, Articles 1–18 including 9 sub-articles; with skill-compiled key points and errata at the end); full English text @references/madrid-agreement-en.md (English text/283530, fetched 2026-08-08, Articles 1–18).
· Madrid Protocol (amended 2007-11-12, WIPO Lex TRT/MADRIDP-GP/001) — @references/madrid-protocol.md (**verbatim Chinese full text**, fetched 2026-09-25, Articles 1–16 + 10 sub-articles + official footnotes; with skill-compiled key points and errata at the end); full English text @references/madrid-protocol-en.md (English text/283484, fetched 2026-08-08, Articles 1–16 + 10 sub-articles).
· Common Regulations (page states in force 2025-11-01; Rule 40(1) records entry into force 2020-02-01, WIPO Lex TRT/MADRIDP-GP/040) — @references/madrid-regulations.md (**verbatim Chinese full text**, fetched 2026-09-25, Rules 1–41 + official footnotes 1–9; with key points, an English title concordance and errata at the end); full English text @references/madrid-regulations-en.md (English text/596531, Rules 1–41, without the Schedule of Fees).
· Administrative Instructions (in force 2023-02-01, WIPO Lex TRT/MADRIDP-GP/036) — @references/madrid-admin-instructions.md (**verbatim Chinese full text**, fetched 2026-09-25, 7 Parts, 19 Sections + Section 11bis; with key points and errata at the end); full English text @references/madrid-admin-instructions-en.md (English text/586472, fetched 2026-08-08, 7 Parts, Sections 1–19).
· WIPO Madrid members declarations page (updated 2026-03-15) — @references/madrid-declarations.md.
· **WIPO Schedule of Fees (2023-02-01 edition) and the individual-fees page (updated 2026-08-23, fetched 2026-09-23) — @references/madrid-fees.md (the sole authoritative source for fee amounts in this skill).**
· FAQ and practice-counterexample compilation (compiled from the above treaties and the Schedule of Fees) — @references/madrid-faq.md.
· Madrid e-Filing Applicant's Guide (WIPO official) — @references/madrid-efiling-applicant-guide.pdf.
· Guide to the Examination of Goods and Services under the Madrid System (5th edition, 2026) — @references/madrid-goods-services-classification-guide.pdf (with a distilled companion @references/madrid-goods-services-classification.md).
· CNIPA Guide on Fast-Track Examination of Madrid International Registration Applications — @references/madrid-fast-track-examination-cnipa.md.
· (US-side fees are handed off) USPTO Madrid fees where the US is Office of origin/designated Office (37 CFR §7.6 certification/transmittal fee, §7.7 collection of international fees, USD, with fee codes): **if the `us-tm-madrid` skill is installed in this environment**, see madrid-uspto-fees.md in that skill's references directory (fetched 2026-08-09); **if not installed**, consult the USPTO Fee Schedule directly (https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule). This skill keeps only WIPO-side fees (CHF) and does not copy US-side data.

> **Conversion delegation (optional)**: if the WIPO/CNIPA PDFs listed above (e.g. the e-Filing guide, the classification examination guide) need to be converted in full into structured Markdown to update this library, **delegate to the `legal-doc-converter` skill if installed** (shared conversion layer, single-maintained scripts; this skill does not duplicate them); **if not installed**, consult the official PDFs directly, or take the distilled points from `references/madrid-faq.md §III`; conversion is not a prerequisite.

### 3.2 Madrid Union Membership Data (three different counts — easily confused, must be distinguished)

| Measure | Figure | Meaning and notes |
| --- | --- | --- |
| Contracting Parties (members) | 117 | Political entities party to the Madrid System, including 3 intergovernmental organisations: EU, Benelux (BX) and OAPI. Baseline: WIPO members page (**verified 2026-09-23**, header shows 117 members / 133 countries). Newest members: Grenada (deposited 2025-12-15, in force 2026-03-15), Saudi Arabia (published 2026-07-23, Protocol entry into force **2026-10-08**). Before the Saudi entry-into-force date the effective designatable figure is 116. |
| Designatable Contracting Parties | approx. 119 | Total number of "designation" checkboxes in tools such as the WIPO Fee Calculator = 117 members + separately designatable territories (e.g. Curaçao CW and Sint Maarten SX under the Kingdom of the Netherlands; Jersey and Guernsey are listed separately), fluctuating with territory designation status. |
| Countries/territories covered | 133 | Countries/territories in which trademark protection can actually be obtained under the 117 members (counting e.g. the 27 EU member States and the 17 OAPI member States individually). |

Key notes:

· **All members are party to the Madrid Protocol** — WIPO members page, Key Facts: "All Madrid System members are party to the Madrid Protocol – the governing treaty of the Madrid System." (verified 2026-09-23). In practice there is no "Agreement-only member", so a basic application generally suffices; the Agreement-only branches retained in §4.7 and §4.8 serve as fallbacks for historical/individual situations and still require case-by-case verification.
· A designation of China (CN) does **not** extend to Hong Kong or Macao — they are not designatable Contracting Parties under the Madrid System and must be covered by single-jurisdiction applications.
· Safeguard-clause reminder: universality of membership does not mean universality of declarations. Under Article 9sexies(1)(b) of the Protocol and items 2.4/5.3/6.4 of the Schedule of Fees, where the designated Contracting Party and the Contracting Party of the Office of origin **are both party to the Agreement and the Protocol**, declarations made by that State under Article 8(7) and Article 5(2)(b)/(c) have no effect in their mutual relations (see @references/madrid-faq.md Q11).

### 3.3 China's Position in the Madrid System

> This section is **supplementary information** from the China (CNIPA) perspective and forms an optional chapter; the general rules of the international phase apply uniformly to all members (currently 117 Contracting Parties), see §I Role. Non-China practitioners may skip it.

· China is party to both the Madrid Agreement and the Madrid Protocol.
· An international registration designating China takes effect under the Protocol (China is a Protocol Contracting Party; term of protection, refusal period and fees all follow the Protocol rules, see Protocol Article 6), so China-related practice is governed by the Protocol framework in the first place.
· CNIPA acts both as Office of origin and as designated Office.

### 3.4 Core Differences Between the Agreement and the Protocol

| Item | Madrid Agreement | Madrid Protocol |
| --- | --- | --- |
| Term of protection | 20 years | 10 years |
| Basic requirement | A national registration already obtained | A national application suffices |
| Refusal period | 12 months (no 18-month option) | 12 months (18 months after a declaration under Article 5(2)(b)) |
| Fee system | Complementary fee + supplementary fee (no individual fee) | Individual fee available (replacing the complementary fee and part of the supplementary fee) |
| Membership | States only | States + intergovernmental organisations (e.g. EU, OAPI) |
| Transformation relief | None | Article 9quinquies allows transformation into national/regional applications |

### 3.5 Background Tools and Standards

· Nice Classification: classification must follow the 13th edition (NCL13-2026, in force 2026-01-01); the NCL may be updated on 1 January each year — in practice, follow the version shown in the MGS database.
· MGS (Madrid Goods & Services Manager): WIPO's official standardised terminology database for goods/services, https://webaccess.wipo.int/mgs/ — used to verify whether wording is the standardised expression accepted by WIPO; supports BROWSE (by class) and SEARCH (by keyword).
· Madrid Monitor: WIPO's official real-time status lookup for international registrations, https://www3.wipo.int/madrid/monitor/en/ — supports By number / By trademark / By holder searches.
· eMadrid: WIPO's integrated electronic platform, https://www.wipo.int/madrid/en/emadrid/ — includes e-Filing (new applications), Pay Fee (online payment), Manage (subsequent management) and Madrid Monitor (status lookup).
· ROMARIN: WIPO's official Madrid trademark search database (Common Regulations Rule 33), https://www.wipo.int/romarin — complements Madrid Monitor (Monitor for case-by-case status tracking, ROMARIN for bulk retrieval and data analysis).
· MM standard forms: MM2 international application, MM3 subsequent designation, MM4 renewal, MM5 change recordal (change of name/address, assignment, limitation, renunciation), MM6 recordal of a licence.
· WIPO Fee Calculator: official online fee calculator, https://madrid.wipo.int/feecalcapp/ — supports New application / Subsequent designation / Second Part fee / Renewal.

### 3.6 Contracting Party Declarations and Notifications (quick reference)

Each Contracting Party may make declarations and notifications under the Protocol and the Common Regulations, directly affecting its effect, fees and time limits. **The overview of declaration categories and the per-country lists are governed by @references/madrid-declarations.md (17 categories, numbering as in that file; that overview table is not duplicated here to avoid two parallel numbering systems)**; baseline: WIPO declarations page 2026-03-15, subject to §3.0 review.

Five high-frequency categories (quote the reference file's numbering and legal basis verbatim):

· **No.4 Individual fee (Art.8(7)(a))**: the country charges an individual fee instead of the complementary fee → drives budgeting (amounts in @references/madrid-fees.md).
· **No.9 Refusal period extended to 18 months (Art.5(2)(b))**: absent the declaration, 12 months → drives risk assessment (see §4.11).
· **No.10 Extension after opposition (Art.5(2)(c))**: may extend to about 25 months.
· **No.1/No.2 Division / merger not available (Rule 27bis(6), 27ter(2)(b))**: determines the feasibility of subsequent management.
· **No.16 Declaration of intention to use (Rule 7(2))**: extra preparation in the application file.

Declarations made by China (complete list):

| Declaration | Basis | Note |
| --- | --- | --- |
| Division not available | Rule 27bis(6) | — |
| Merger not available | Rule 27ter(2)(b) | — |
| Individual fee applies | Art.8(7)(a) | Amounts in @references/madrid-fees.md |
| Collection and transmittal of fees | Rule 34(2)(b) | Settled in RMB |
| Recordal of a licence has no international effect | Rule 20bis(6)(b) | — |
| 18-month refusal period | Art.5(2)(b) | — |
| Extension after opposition | Art.5(2)(c) | — |
| Ex officio refusal not subject to review | Rule 17(5)(e) | — |
| Minimum response time limit not applicable | Rule 40(8) | — |

Safeguard clause: where the designated Contracting Party and the Contracting Party of the Office of origin **are both party to the Agreement and the Protocol**, categories No.4, No.9 and No.10 above have no effect in their mutual relations (Protocol Art.9sexies(1)(b); Schedule of Fees items 2.4/5.3/6.4) — verify case by case.

### 3.7 Locating the Governing Provisions (by subject matter)

Locate the relevant provisions by issue: eligibility and Office of origin → Agreement Art.1 / Protocol Art.2; territorial extension and subsequent designation → Article 3ter; refusal procedure → Article 5; central attack and dependency period → Article 6; transformation relief → Protocol Article 9quinquies; **fees → @references/madrid-fees.md**; refusal time limits → Common Regulations Rule 17; reproduction format → Administrative Instructions Section 11bis; names and addresses → Sections 12; payment methods → Section 19; classification examination → the Guide (5th ed., 2026) + Common Regulations Rules 12/13. The complete provision index is in @references/madrid-faq.md §IV.

### 3.8 FAQ (quick answers)

The complete set (13 questions, including the safeguard clause, the US fee split and the response time limits for China) is in @references/madrid-faq.md. High-frequency quick answers:

· Q1 Is a national registration required first? No. All current members are Protocol Contracting Parties, so a basic **application** filed with the Office of origin suffices (historical/individual Agreement-only situations require a registration as the basis).
· Q2 How long is protection? 10 years under the Protocol, 20 years under the Agreement; extended on renewal.
· Q3 What is "central attack"? For 5 years from the date of the international registration it depends on the basic application/registration; if the basic right is cancelled, the international registration falls with it. Response: file transformation applications **directly with each designated Office** within **3 months** from the cancellation, under Protocol Article 9quinquies.
· Q4 How is the refusal period calculated? **Baseline 12 months**; 18 months where the Contracting Party has made an Article 5(2)(b) declaration; about 25 months maximum where it has also made an Article 5(2)(c) declaration and an opposition occurs. For subsequent designations the period runs from the **date of recordal**. Absence of a notified refusal means protection is obtained — **never assume 18 months**.
· Q5 Can Contracting Parties be added later? Yes, by subsequent designation (MM3); database entry within 3 working days.
· Q6 How are fees calculated? Basic fee (653 black-and-white / 903 colour) + supplementary fee (100 per class beyond 3, not collected where all designated States charge individual fees) + complementary fee (100 per Contracting Party, for those that have not declared individual fees) or individual fee. See §4.8 and @references/madrid-fees.md.
· Q7 When is renewal due? Within 6 months before expiry; a 6-month grace period applies after expiry with an additional **50% of the basic fee (327 CHF)**.
· Q8 How should a Chinese applicant's name be entered? Chinese name + transliteration in Latin letters (pinyin); full address with street, city and country.
· Q9 Can a registration be assigned across borders? Yes; the assignee must be eligible; after recordal each designated Office has 18 months to decide whether to refuse recognition.
· Q10 Relationship with EU trade marks (EUTM)? The EU is a Protocol Contracting Party and may be designated or subsequently designated; an EUTM application can serve as the basic application.
· Q11 After a refusal of a designation of China, how long is the review/response period and when does it start? Ex officio refusals **15 days**, opposition-type refusals **30 days**, both running from **the date the holder receives the notification transmitted by WIPO** (WIPO Rule 17(7) table, updated 2026-08-28). Note this is a different time limit from the **18-month refusal period** within which CNIPA must notify; see §4.11 and @references/madrid-faq.md Q13.

## IV. Procedures (Steps)

### 4.0 Task Routing (consult this first, then go to the relevant subsection)

Route the user's question to the right resource; avoid whole-library searching and misreading:

| What the user wants | Read | Load reference files | Use scripts / templates |
| --- | --- | --- | --- |
| Prepare and file an international application | §4.1 | @references/madrid-goods-services-classification.md | `templates/madrid_application_checklist.md` |
| Verify goods/services wording (MGS) | §4.2 | @references/madrid-goods-services-classification.md | — |
| Check international registration status | §4.3 | — | Madrid Monitor / ROMARIN |
| Respond to a provisional refusal or opposition | §4.4 | @references/madrid-declarations.md (response time limits) | `templates/madrid_refusal_response_memo.md` |
| Renew | §4.5 | @references/madrid-fees.md | `scripts/madrid_renewal.py` |
| Subsequent designation (add Contracting Parties) | §4.1 (from Step 2) | @references/madrid-fees.md (item 5), @references/madrid-declarations.md | `scripts/madrid_fee.py --later-designation` |
| Change / assignment / limitation / renunciation / division & merger / recordal of a licence | §4.6 | @references/madrid-declarations.md | — |
| Central attack and transformation | §4.7 | @references/madrid-protocol.md (Article 9quinquies) | — |
| Calculate fees, look up individual fees | §4.8 | @references/madrid-fees.md | `scripts/madrid_fee.py` |
| Calculate the refusal period (Office's 12/18/25 months) | §4.11 | @references/madrid-declarations.md | `scripts/madrid_deadline.py` |
| Look up time limits to respond to a provisional refusal (China 15/30 days etc.) | §4.11, §4.4 | @references/madrid-declarations.md §4e | Manually count "received date + days" (scripts cover only 12/18/25 months) |
| Check a country's declarations before choosing strategy | §4.14 | @references/madrid-declarations.md | — |
| eMadrid / e-Filing / ROMARIN operations | §4.9 | @references/madrid-faq.md §III | — |
| FAQ / troubleshooting | §3.8 | @references/madrid-faq.md | — |
| Data freshness and verification | §3.0 | — | — |
| China (CNIPA) route | §4.10 | @references/madrid-fast-track-examination-cnipa.md | — |

### 4.1 International Application Procedure

> This section follows the **common practice for any Contracting Party**. "Office of origin" means the Office of the Contracting Party through which the applicant qualifies under Protocol Article 2 — it is **not specific to China**. The concrete filing route and document requirements where CNIPA is the Office of origin are in §4.10; the same reasoning applies to any other Office of origin (USPTO, EUIPO, JPO, etc.).

```
Step 1: Applicant files the basic trademark application / obtains the basic registration in the **Contracting Party of origin**
           │
           ▼
   🔴 CHECKPOINT: confirm basic application/registration details (applicant name, address, goods/services scope)
           │
           ▼
Step 2: Applicant files the Madrid international application through the **Office of origin**
           │
           ▼
   🔴 CHECKPOINT: confirm the list of designated Contracting Parties, classification of goods and services, and fee calculation
           │
           ▼
Step 3: The **Office of origin** examines the application for compliance and transmits it to WIPO's International Bureau
           │
           ▼
   🔴 CHECKPOINT: the International Bureau must receive the application within 2 months of the date the Office of origin received it, in order to keep the Office of origin's receipt date as the registration date (Protocol Article 3(4)). If late, the actual receipt date at the International Bureau prevails → chase transmittal early
           │
           ▼
Step 4: WIPO International Bureau carries out formal examination
           │
           ▼
   🔴 CHECKPOINT: after an irregularity notice from the International Bureau → remedy within 3 months, otherwise the application is deemed abandoned
           │
           ▼
Step 5: Date of the international registration is fixed → recorded in the International Register
           │
           ▼
Step 6: The International Bureau notifies the designated Offices (each designated Contracting Party)
           │
           ▼
Step 7: Each designated Office decides within the applicable time limit whether to grant protection
           │
           ▼
   🔴 CHECKPOINT: monitor the refusal period country by country (baseline 12 months → 18 months if Art.5(2)(b) declared → up to about 25 months with a (2)(c) declaration and an opposition)
         → always verify the country's declarations first (§4.14); never assume 18 months; if no refusal by expiry, protection is obtained
```

Eligibility (the connecting link, Protocol Article 2): the applicant must have a real and effective industrial or commercial establishment in **a Contracting Party** (the "Contracting Party of origin"), or be domiciled there, or be a national of that Contracting Party — any one of the three suffices; **there is no requirement to be a Chinese national or to have an establishment in China**. The Office of that Contracting Party is the Office of origin for the case.

Basic requirement: where the designated Contracting Party is bound only by the Protocol, a basic **application** filed with the Office of origin suffices; where only the Agreement applies, a trademark **registration** must already have been obtained there; where both apply, the Protocol prevails and a basic application suffices. Since all current members are Protocol Contracting Parties (WIPO Key Facts, verified 2026-09-23), in practice a basic application suffices; for historical/individual situations bound only by the Agreement, a registered trademark must be used as the basis.

Required contents of the application: applicant's name and address (where not in Latin characters, a Latin-letter transliteration must be added, see Administrative Instructions Section 12; a Chinese applicant must give both the Chinese name and its pinyin, and Japanese, Korean, Russian etc. applicants likewise); reproduction of the mark (JPEG/PNG/TIFF, not exceeding 20 cm × 20 cm); list of goods and services (grouped by Nice class); designated Contracting Parties; date and number of the basic application/registration; fee calculation. Optional elements: colour claim (must be declared, with a colour reproduction); sound marks (MP3/WAV, not exceeding 5 MB); animated multimedia marks (MP4, H.264/H.262, not exceeding 20 MB); representative details.

Date of the international registration: the general rule is the date on which the Office of origin received the application; exception — if the International Bureau receives it more than 2 months after the Office of origin's receipt date, the International Bureau's receipt date prevails.

Classification rules: classify under NCL13-2026; use WIPO standardised wording (verified via MGS); supplementary fee applies per class beyond 3; where classification is irregular the International Bureau invites correction, to be made within 3 months using standardised wording. The authoritative examination guide is the official Guide to the Examination of Goods and Services in International Applications under the Madrid System (5th ed., 2026) (@references/madrid-goods-services-classification-guide.pdf; distilled companion @references/madrid-goods-services-classification.md); the Guide ranks below the Nice Classification, and in case of conflict the Nice Classification prevails.

Exceptional scenarios and fallbacks:

· Office of origin objects that goods/services exceed the basic right: first-line fix is to delete the excess items and refile; if that fails, file a separate national application for the excess items in that Contracting Party and add them later by subsequent designation.
· International Bureau notifies irregular classification: reclassify within 3 months using WIPO-accepted standardised wording; if not corrected the International Bureau classifies on its own, possibly narrowing the scope of protection.
· Office of origin fails to transmit within 2 months: chase immediately; the registration date becomes the International Bureau's actual receipt date and priority based on the Office of origin's receipt date is lost.
· Insufficient fees: pay the difference within 3 months of the notice; otherwise the application is deemed abandoned and the amount paid is refunded (less a handling charge).
· Applicant inconsistent with the basic right: verify and align the applicant details; if it cannot be fixed, the International Bureau returns the application.
· Non-compliant reproduction format: adjust per Administrative Instructions Section 11bis (JPEG/PNG/TIFF ≤ 20 cm × 20 cm; sound MP3 ≤ 5 MB; animated MP4 ≤ 20 MB).

### 4.2 MGS Goods/Services Verification Procedure

```
Draw up the goods/services list (grouped by class)
           │
           ▼
Check each item in MGS (https://webaccess.wipo.int/mgs/)
           │
           ├── Known class → use BROWSE
           │
           └── Specific goods → use SEARCH with keywords
           │
           ▼
   🔴 CHECKPOINT: confirm item by item that the wording matches MGS exactly
           │
           ▼
Record the standardised wording → enter by class into the Madrid application form (MM2)
           │
           ▼
Second check before filing: every item must match MGS exactly
```

Why MGS is necessary: to avoid irregularity notices (remedy within 3 months; otherwise the registration date is affected); irregularities may cause the registration date to be re-dated to the date of correction and priority to be lost; and to align with the examination practice of the designated Offices / Office of origin. The Madrid Classification Helpdesk (MCH) gives expert classification guidance on new and emerging goods and services; approach it via the "Contact us" form on the Madrid System web pages (details in @references/madrid-goods-services-classification.md §X).

### 4.3 Madrid Monitor Status Lookup Procedure

```
Client asks for the status of an international registration
           │
           ▼
   🔴 CHECKPOINT: determine the search keys (registration number / mark name / holder name)
           │
           ▼
Go to Madrid Monitor (https://www3.wipo.int/madrid/monitor/en/)
           │
           ├── Have the number → use By number
           ├── Have the mark name → use By trademark
           └── Full-portfolio check → use By holder
           │
           ▼
   🔴 CHECKPOINT: check the status in each designated Contracting Party one by one:
       ① "Provisional refusal"? → confirm the response deadline
       ② "Protected"? → confirm the scope of protection
       ③ Final decision on refusal? → assess follow-up options
       ④ Renewal date approaching? → plan the renewal
           │
           ▼
Produce a status report → inform the client with recommendations
```

Available information: basic registration data (international registration number, registration date, expiry date, holder, representative); mark reproduction and details (reproduction, colour claim, classes); status in each designated Contracting Party (protected / provisional refusal / response deadline / final decision); subsequent designations; recordals of changes; time-limit information. Madrid Monitor data is synchronised in real time with the WIPO International Register; proactive checks are recommended 3–6 months after filing, around the expiry of each designated Contracting Party's refusal period, after receipt of a refusal notice, and 6 months before renewal.

### 4.4 Responding to Refusals and Oppositions

```
Receive the notification of provisional refusal transmitted by the International Bureau
           │
           ▼
   🔴 CHECKPOINT: identify the refusal type (ex officio / opposition) and the starting point, then fix the response deadline
        → calculate with py scripts/madrid_deadline.py --respond --cp <code> [--opposition] [--received|--base-date]
          (built-in WIPO Rule 17(7) data for 38 members; China: ex officio 15 days / opposition 30 days, from the date of receipt)
        → where the country's starting point is not a "date of receipt" type, the script refuses to count from the received date and requires the official base date (--base-date)
        → keep evidence of the starting point (date of the WIPO transmittal e-mail / date stated in the notice); response periods run in days/months and are unrelated to the 12/18/25-month refusal period
           │
           ▼
Analyse the refusal grounds and legal basis
           │
           ├── Absolute grounds → prepare legal argument or restrictive amendment
           └── Relative grounds → gather earlier-right information, assess settlement vs contesting
           │
           ▼
   🔴 CHECKPOINT: keep at least 2 weeks before the response deadline → if less than 2 weeks remain, seek an extension immediately (where the country allows)
           │
           ▼
File the response within the time limit set by the designated Office
           │
           ▼
   🔴 CHECKPOINT: after responding, track the designated Office → if no word for 3 months, follow up
           │
           ▼
If finally refused → within each country's time limit: ① request review/appeal; ② narrow the goods/services and re-designate; ③ abandon that designated Contracting Party; ④ where the country has an opposition procedure → assess settlement or withdrawal of the designation
```

Refusal period (always verify declarations per §4.14 before fixing any period): **baseline 12 months** (Protocol Art.5(2)(a); the Agreement's Article 5 is the same length); **18 months** where the Contracting Party has declared under Art.5(2)(b); up to about **25 months** (18 + 7) where it has also declared under Art.5(2)(c) and an opposition occurs. For subsequent designations the period runs from the **date of recordal**, not the date of the original international registration. Common mistake: assuming 18 months without checking the declaration and wrongly treating the mark as "protected".

Refusal grounds: absolute grounds include lack of distinctiveness, functionality, contravention of public order or morality, deceptive descriptions, and breach of statutory prohibitions; relative grounds include conflict with earlier trademark rights and with other earlier rights (the refusal notice should briefly state the earlier right and its owner).

Content requirements for refusal notices (Administrative Instructions Section 15): must state the specific refusal grounds and legal basis; where earlier rights are involved, must identify the earlier right and its owner; must not contain case-file or evidence annexes.

Opposition and ex officio provisional refusal are two different procedures: a provisional refusal is issued by the examiner of the designated Office on its own motion; an opposition is filed by a third party; the International Bureau does not take part in the substantive examination of an opposition, it only handles the extension of the refusal period. Features of opposition: filed by a third party; decided by the trademark authority of the designated Contracting Party (not WIPO); governed by the national law of that Contracting Party; the period extends to 18 months as the basic period + up to 7 months for the opposition ≈ 25 months; the International Bureau merely transmits the extension notice. On receiving an opposition notice, first confirm the opponent's identity and grounds — most are based on conflicts with earlier trademark rights and can be resolved by limiting the goods or obtaining a letter of consent; abandoning the designated Contracting Party outright should be the last resort.

Exceptional scenarios and fallbacks for refusal responses:

· Designated Office's refusal notice does not state specific grounds: ask the International Bureau to require the Office to supplement the grounds (an irregular refusal is treated as not made); if that fails, request the grounds from the Office within its time limit.
· Response period too short (due to non-working days): extend to the next working day under Common Regulations Rule 4(4); otherwise file the response at least 5 working days before the deadline.
· Designated Office refuses several classes at once: analyse class by class, respond for the arguable classes and abandon the hard ones first.
· Earlier-right owner files an opposition: assess settlement possibilities (coexistence agreement / limiting the goods); if unresolvable, abandon the designated Contracting Party and switch to a separate national application.
· Examiner finds a likelihood of confusion: file evidence of market coexistence, consumer-perception surveys, evidence of differentiated use; or narrow the goods description with additional distinguishing wording.

### 4.5 Renewal Procedure and Key Points

Basic renewal rules: term of protection 20 years in Agreement Contracting Parties, 10 years in Protocol Contracting Parties, and the same for each renewed term; renewal may not modify the registration in any way; the grace period is 6 months in both cases.

Renewal fees (details in @references/madrid-fees.md §IV): renewal basic fee **653 CHF** (Schedule item 6.1, regardless of colour or filing mode); renewal supplementary fee (per class beyond 3) 100 CHF; renewal complementary fee (per designated Contracting Party that has not declared an individual fee) 100 CHF; individual fees as set by each Contracting Party; **grace-period surcharge = 50% of the basic fee, i.e. 327 CHF** (Schedule item 6.5, official wording: "50% of the amount of the fee payable under item 6.1" — not 50% of the total amount due).

Renewal practice points: payable from 6 months before expiry; partial renewal possible (only some goods/services); within the grace period an extra 327 CHF; the renewal is recorded as of the date on which it was due (even if paid during the grace period); after renewal the International Bureau issues the renewal certificate and notifies the designated Offices.

### 4.6 Changes and Subsequent Management

Types of change and how to file:

| Type of change | How to file | Key points |
| --- | --- | --- |
| Change of holder's name/address | Through the Office of origin or directly with the International Bureau | Supporting evidence of the change required |
| Limitation of goods and services | Through the Office of origin or directly with the International Bureau | Deletion only, no addition |
| Partial renunciation | Through the Office of origin or directly with the International Bureau | Gives up some or all protection in a designated Contracting Party |
| Change in ownership (assignment) | Through the Office of origin or directly with the International Bureau | The assignee must be eligible |
| Division | Through the Office of origin | Divisional registration = original number + capital letter |
| Merger | Through the Office of origin | Uses the number of the registration into which it is merged + capital letter |

Numbering rule (Administrative Instructions Sections 16–18): divisions, partial assignments, mergers and changes after refusal/invalidation all use "original registration number + capital letter (A/B/C…)".

### 4.7 Central Attack Response Procedure

```
Basic registration cancelled / invalidated
           │
           ▼
   🔴 CHECKPOINT: is the international registration still within the 5-year dependency period?
           │
           ├── 5 years elapsed → the international registration is independent ✅
           └── Within 5 years → transformation procedure
           │
           ▼
   Step 1: confirm the effective date of the cancellation/invalidation of the basic registration
           │
           ▼
   🔴 CHECKPOINT: start a 3-month countdown from the effective date → set a calendar reminder
           │
           ▼
   Step 2: identify which designated Contracting Parties are bound by the Protocol (transformable)
           │
           ▼
   🔴 CHECKPOINT: Agreement-only Contracting Parties cannot be transformed → assess protection strategy in that country separately
           │
           ▼
   Step 3: prepare transformation files for each transformable designated Contracting Party
           │
           ▼
   Step 4: file transformation applications **directly with each designated Office** within 3 months
           │
           ▼
   Step 5: track the outcome of each transformation application
           │
           ▼
   🔴 CHECKPOINT: after transformation → the resulting national application keeps the date of the original international registration and its priority date
```

How central attack works: for 5 years the international registration depends on the basic registration/application; if the basic right is cancelled/invalidated, the international registration falls with it; after 5 years it becomes fully independent. Transformation requirements (Protocol Article 9quinquies): the basic registration is cancelled within the 5 years; the designated Contracting Party concerned is a Protocol Contracting Party; the request is filed with each designated Office within 3 months; the transformed application keeps the date of the original international registration and its priority date.

Exceptional scenarios and fallbacks:

· Basic registration cancelled after 5 years: the international registration is already independent, unaffected, no transformation needed.
· Designated Contracting Party is Agreement-only (not a Protocol Contracting Party): Article 9quinquies does not apply; convert into a direct national application in that country and request retention of the original registration date; if the country does not allow retention, refile.
· Missed the 3-month transformation deadline: file immediately with reasons for the delay (some Contracting Parties may accept at their discretion); otherwise it becomes an ordinary national application and the priority of the original international registration date is lost.
· Designated Office requires translations/certified documents after transformation: supply within the set time limit; otherwise the transformation application may be returned and the claim to the original date fails.
· Transformed goods/services exceed the scope of the original international registration: limit the transformation to the basic registration "as is"; excess items must be filed separately as national applications.

### 4.8 Fee System

> **The sole authoritative source for fee amounts is @references/madrid-fees.md** (Schedule of Fees 2023-02-01 edition; individual fees 2026-08-23, verified 2026-09-23). This section keeps only the composition rules, calculation logic and common pitfalls; before quoting any amount, load that file or verify online per §3.0.

Fee composition (terminology per §5.1): basic fee + supplementary fee + complementary fee / individual fee. All amounts are in Swiss francs (CHF).

| Stage | Basic fee (CHF) | Supplementary fee | Complementary fee / individual fee |
| --- | --- | --- | --- |
| International application (covers 10 years) | 653 (black-and-white) / 903 (colour) | 100 per class (beyond 3; not collected where all designated States charge individual fees) | 100 per Contracting Party that has not declared an individual fee, or that country's individual fee |
| Subsequent designation (until end of current term) | 300 | As above | As above |
| Renewal (covers 10 years) | 653 | 100 per class | As above; within the grace period add **327** (50% of the basic fee) |

Four error-prone points (earlier versions of this skill got them wrong; corrected against the official Schedule):

· The complementary fee applies to **Contracting Parties that have not declared an individual fee**, not to "Agreement Contracting Parties" — all current members are Protocol Contracting Parties.
· The grace-period surcharge = **50% of the basic fee (327 CHF)**, not "50% of the total amount due" (Schedule item 6.5).
· The current Schedule differentiates the basic fee **only by colour** (653 / 903); the renewal basic fee has a single tier of 653; an "electronic vs paper" price difference does not appear in the 2023-02-01 edition.
· **Safeguard-clause exception**: where the designated Contracting Party and the Contracting Party of the Office of origin **are both party to the Agreement and the Protocol**, that State's individual-fee declaration has no effect and the complementary fee of 100 CHF applies instead (Protocol Art.9sexies(1)(b); Schedule items 2.4/5.3/6.4). Verify this where a Chinese applicant designates dual-party States such as France, Germany, Italy, Spain or Switzerland.

Individual fee in three steps: ① check the WIPO individual-fees page whether the country is listed → ② if listed, take the amount for that Contracting Party from @references/madrid-fees.md (note separate rates for collective/certification marks); if not listed, count 100 CHF per Contracting Party → ③ check the safeguard-clause exception and cross-verify with the WIPO Fee Calculator. When an amount is disputed, run `scripts/madrid_feecalc_live.py` for a live measurement (it can output the per-country breakdown as raw text) as the basis of decision — never rely on memory or search-engine caches. **The script's `--date` is the decisive parameter**: the WIPO individual-fees page shows only current amounts, whereas the Calculator applies the rates in force on the intended filing date; across a rate-change date (commonly 1 November or 1 January) you must calculate separately for the intended filing date — the same application may carry two different prices before and after the change. Two-part individual fees (Cuba) require the second part to be added; designating the US requires the USPTO-side USD fees (see the `us-tm-madrid` skill if installed, otherwise the USPTO Fee Schedule).

LDC reduction: where the Contracting Party of origin is on the UN LDC list, the basic fee is reduced to 10% — 65 CHF black-and-white / 90 CHF colour.

Calculation tool: `scripts/madrid_fee.py` contains only the verified WIPO official fee baselines (basic fee / supplementary fee); individual fees must be completed per the step above — the script never silently estimates.

How to use the WIPO Fee Calculator:

```
Step 1: select the transaction type (New application / Subsequent designation / etc.)
           │
           ▼
Step 2: select the designated Contracting Parties (multi-select)
           │
           ▼
Step 3: enter the number of classes of goods/services
           │
           ▼
   🔴 CHECKPOINT: check whether collective/certification marks are involved (different rates in some Contracting Parties)
           │
           ▼
Step 4: the system computes each fee item and totals them
           │
           ▼
   🔴 CHECKPOINT: cross-check the result against the Schedule of Fees
```

Fee Calculator output is an estimate; the amount finally due is governed by the International Bureau's payment notice; where exchange rates move sharply the actual charge may differ from the estimate.

Second Part Fee (Common Regulations Rule 34(3)(a)): currently only **Cuba (CU)** still applies two-part payment (first part on filing, second part notified by the International Bureau after registration); Japan abolished it in 2023. **If the second part is not paid within the applicable time limit, the International Bureau cancels the international registration with respect to that Contracting Party under Rule 34(3)(d)** — it is not that "protection is not yet complete" but that the registration is cancelled, so "registration granted ≠ protection complete". Amounts and practice points are in @references/madrid-fees.md §XI; verify online when handling Cuban cases.

### 4.9 eMadrid and ROMARIN

Core functions of eMadrid (https://www.wipo.int/madrid/en/emadrid/): e-Filing — complete and file new applications online; Pay Fee — online payment by credit card / current account; Manage — subsequent designation, change, assignment, renewal; Madrid Monitor — status lookup. Practice points: an account must first be created with WIPO (in the firm's name is advisable); for electronic filing the date of receipt confirmed by the International Bureau prevails (Administrative Instructions Section 11), and written communications must be signed (Section 6). Note: the current Schedule differentiates the basic fee **only by colour** (653 / 903), not by electronic vs paper filing — verify the current Schedule before citing any "electronic filing discount". ROMARIN (https://www.wipo.int/romarin) is WIPO's official Madrid trademark search database (Common Regulations Rule 33), complementing Madrid Monitor (the former for bulk retrieval and data analysis, the latter for case-by-case status tracking). MM standard forms: MM2 new application, MM3 subsequent designation, MM4 renewal, MM5 change recordal, MM6 recordal of a licence.

Madrid e-Filing Applicant's Guide (WIPO official, 43-page PDF, @references/madrid-efiling-applicant-guide.pdf): aimed at applicants from e-Filing participating countries; applicants from non-participating countries must file through their Office of origin, but the Guide's form-entry checkpoints (applicant details, reproduction size, classification verification, responding to irregularity notices) apply equally to applications filed through an Office of origin. Chapter-level points and item-by-item checkpoints are in @references/madrid-faq.md §III.

### 4.10 China Practice Bridge

> This section is the **optional bridge chapter** from the CNIPA/China perspective, not the mainline of this skill. The general international-phase procedures are in §4.1–§4.9; non-China practitioners may skip it entirely.

CNIPA as Office of origin: Chinese applicants file Madrid international applications through CNIPA, online via the China Trademark Office Madrid filing system (recommended) or on paper. Materials required: the Madrid international application form, proof of the Chinese trademark application/registration, reproduction of the mark, power of attorney (if represented), and the fees (in RMB, collected by CNIPA and transmitted to WIPO). CNIPA examination points: consistency of the applicant with the basic application/registration; goods/services not exceeding the basic right; classification compliance.

CNIPA as designated Office: where a foreign applicant designates China, CNIPA examines. **Two time limits must be kept separate** (the most confusing point in practice):

· **Time limit for CNIPA to notify a refusal (refusal period) = 18 months**: China has declared under Protocol Art.5(2)(b); it runs from the date of the international registration / recordal of the subsequent designation, irrespective of whether the holder has received anything. Under the safeguard clause (Art.9sexies(1)(b)), where the holder's Contracting Party is also party to both the Agreement and the Protocol, verify whether that declaration takes effect in their mutual relations.
· **Time limit for the holder to respond to a provisional refusal (review/response period) = 15 days for ex officio refusals, 30 days for opposition-type refusals**: both run from **the date the holder receives the notification transmitted by WIPO** (WIPO Rule 17(7) table, updated 2026-08-28). Domestic-law counterparts: 15 days — Article 34 of the Trademark Law (request for review within 15 days of refusal); 30 days — Article 45(3) of the Implementing Regulations (the opposed party responds within 30 days of receiving the refusal notice transmitted by the International Bureau). China has declared Rule 40(8) (minimum response time limit not applicable), so the 15-day period is valid despite its length; verify the authority and time limit stated in the body of the refusal notice in each case and keep proof of receipt.

Refusal grounds follow the absolute grounds (§10 prohibited signs, §11 lack of distinctiveness, §12 functionality) and relative grounds (§30 identical/similar earlier trademarks, §32 prejudice to others' earlier rights) of China's Trademark Law.

Interface with the Trademark Law: basic application → §22; territorial extension to China → §25 (international registration priority, 6 months); refusal in China → §30/§31/§33 (may reference refusal review); protection in China → §39 (10-year term); renewal in China → §40 (within 12 months before expiry); assignment in China → §42 (subject to CNIPA approval); invalidation in China → §44/§45.

Chinese practitioner workflow:

```
Step 1: receive client instructions (basic trademark details and designated Contracting Parties)
           │
           ▼
   🔴 CHECKPOINT: confirm the status of the client's basic trademark (pending? registered?) → determines the type of designatable Contracting Parties
           │
           ▼
Step 2: prepare the Madrid application file (MM2, reproduction, goods/services list, power of attorney)
           │
           ▼
   🔴 CHECKPOINT: is the goods/services list worded in WIPO-accepted standardised terms?
           │
           ▼
Step 3: file through the CNIPA Madrid filing system
           │
           ▼
Step 4: pay the fees (collected by CNIPA → transmitted to WIPO)
           │
           ▼
   🔴 CHECKPOINT: are the fees sufficient? Has the CHF rate of the day been checked with a buffer?
           │
           ▼
Step 5: track the International Bureau's feedback and the international registration certificate
           │
           ▼
Step 6: monitor protection status in each designated Contracting Party (refusal period: baseline 12 months → 18 months if (2)(b) declared → up to about 25 months with opposition extension)
           ├── No refusal → protection obtained ✅
           └── Refusal received → start the response procedure
           │
           ▼
   🔴 CHECKPOINT: set a deadline reminder for each designated Contracting Party → alert 1 month before expiry
```

Fast-track examination of Madrid international registration applications (CNIPA): available to domestic applicants, electronic filing required, with two additional requirements on top of ordinary Madrid conditions — "a situation under Article 2 of the Fast-Track Measures + a need for overseas registration/enforcement". Practice points: submit the signed or sealed Request for Fast-Track Examination + evidence of the grounds (paper submissions to International Registration Division I of the Trademark Office, envelope marked "Madrid Trademark International Registration Application Fast-Track Examination Request"); if granted, examination and acceptance are completed **within 20 days** of filing, and the international registration fees must be paid **within 7 days** of the payment notice; no extra fee for requesting fast-track examination. If refused or terminated, the application reverts to the ordinary procedure with telephone notice. Full conditions, materials list and termination scenarios are in @references/madrid-fast-track-examination-cnipa.md.

Practice note: fast track only compresses the **CNIPA acceptance stage** (20 days); it does **not** affect formal examination by the WIPO International Bureau, nor the refusal periods of the designated Contracting Parties (baseline 12 months, 18 months if declared, up to about 25 months with opposition extension).

### 4.11 Key Time Limits (quick reference)

Refusal periods:

| Scenario | Time limit | Basis |
| --- | --- | --- |
| **Baseline (no declaration; includes Agreement Contracting Parties)** | **12 months** | Protocol Art.5(2)(a) / Agreement Art.5 |
| Declared under Art.5(2)(b) | 18 months | Protocol Art.5(2)(b) |
| Also declared under Art.5(2)(c) and an opposition occurs | up to about 25 months (18 + 7) | Protocol Art.5(2)(c) |
| Subsequent designation | runs from the **date of recordal** of the subsequent designation; length as above | Protocol Art.3ter(2); Common Regulations Rules 24/33 |

For every refusal period the order is "verify the country's declarations first (§4.14) → then fix the period"; **never assume 18 months**; the safeguard clause (Art.9sexies(1)(b)) may nullify declarations between dual-party States — verify case by case.

International registration time limits:

| Item | Time limit | Basis |
| --- | --- | --- |
| Term of protection (Agreement Contracting Parties) | 20 years | Agreement Art.6 |
| Term of protection (Protocol Contracting Parties) | 10 years | Protocol Art.6(1) |
| 5-year dependency period | 5 years (from the date of the international registration) | Agreement Art.6 / Protocol Art.6(3) |
| Renewal grace period | 6 months (after expiry) | Art.7 / Common Regulations Rule 30 |
| Early renewal window | 6 months (before expiry) | Common Regulations Rule 30(2)(a) |
| Transmittal period of the Office of origin | 2 months | Art.3(4) |

Change-related time limits:

| Item | Time limit | Basis |
| --- | --- | --- |
| Refusal to recognise effect of a change in ownership | 18 months (from the date of notification) | Common Regulations Rule 27(4) |
| Transformation application deadline | 3 months after the basic right fails | Protocol Art.9quinquies(2) |
| Database entry (subsequent designations) | 3 working days | Common Regulations Rule 33(2)(c) |

Time limits to respond to a provisional refusal (**counted in days/months — different from the month-based refusal periods above**; notified country by country under Rule 17(7)):

| Designated Contracting Party | Ex officio refusal | Opposition-type refusal | Starting point |
| --- | --- | --- | --- |
| **China (CN)** | **15 days** | **30 days** | Date the holder receives the WIPO transmittal |
| France (FR) | **1 month** | 2 months | Date WIPO transmits to the holder |
| United Kingdom (GB) | 2 months | 2 months | Date the Office issues the notice |
| United States (US) | 6 months | **40 days** | Ex officio: date the Office sends to WIPO; opposition: date of the TTAB order |
| Germany (DE) | 4 months (2 months if domiciled in Germany) | As left | Date WIPO transmits to the holder |
| Japan (JP) | 3 months | Not applicable | Date the Office issues the notice |
| Singapore (SG) / Spain (ES) | 4 months | 4 months | Date the Office issues the notice |
| Russia (RU) / Canada (CA) | 6 months | Not applicable / 2 months | Date the Office issues the notice |
| Thailand (TH) | 90 days | 90 days | Date the Office issues the notice |

**Coverage warning**: the WIPO table covers only **38 members** (out of 117), and there are **6 distinct starting points** among them (holder's receipt / WIPO transmittal / Office's issuance / WIPO's receipt / 14th day after the Office's issuance / TTAB order). **Not listed ≠ no response deadline**. The full 38-member table and the classification of starting points are in @references/madrid-declarations.md §4e-i, §4e-ii.

Calculation tool: `py scripts/madrid_deadline.py --respond --cp CN --received 2026-09-20 [--opposition]`, or `--notified 2026-09-01` (China's "deemed service" approach, outputting 30 total days from the issuance date). The script contains the 38-member data and determines the starting point — **where the official starting point is not a "date of receipt" type, the script refuses to count from the received date and requires `--base-date`** (counting from the received date would overstate the time remaining); where both the issuance date and the received date are given it prompts to take the earlier; for members not covered, fall back manually with `--limit-days/--limit-months`.

China's domestic-law counterparts: 15 days → Article 34 of the Trademark Law (request review within 15 days of receipt); 30 days → Article 45(3) of the Implementing Regulations (opposition response).

**The "30-day review period" and the 15 days in the table above are two ways of computing the same time limit** (often mistaken for a conflict, must be explained clearly): under Article 10 of the Implementing Regulations, service by electronic means is **deemed made 15 days after the date of dispatch**; where the date of receipt is unknown, 15 days (deemed service) + 15 days (review period) = **30 days from the WIPO dispatch date** — this is the origin of the practice "30 days for review of a Madrid refusal designating China". Therefore: where the receipt date is known, control risk by taking the **earlier** of "receipt date + 15 days" and "dispatch date + 30 days"; where the notice itself states the period, the notice prevails. The 30-day opposition period may likewise be combined with deemed service (dispatch date + 45 days), but this combination has no express official basis and must be checked case by case.

**Do not confuse the 15/30 days with the 12/18/25-month refusal period** — the latter is the period for CNIPA to issue the notification, the former is the period for the holder to respond.

Practice points: day-based periods are far shorter than month-based ones (France only 1 month, the UK 2 months) and the starting point varies by country, so (1) keep proof of the WIPO transmittal timing; (2) set the countdown the day the notice is received, not at month-end; (3) the period runs from the day after the starting point and extends to the next working day if the last day is a public holiday (the authority and period stated in the refusal notice prevail; where necessary file 3–5 working days early).

### 4.12 Automation Tools (Executable Code)

The automation tools are externalised as standalone Python scripts in this skill's `scripts/` directory (Python 3.10+; offline scripts use only the standard library and run directly; the live-fee script additionally needs `playwright`). The scripts are the authoritative source of code; SKILL.md does not embed code. Note: on Windows, if `python` points to the Microsoft Store alias and produces no output, use the `py` launcher instead.

| Tool | File | Purpose | Command-line example |
| --- | --- | --- | --- |
| Fee calculator (offline) | `scripts/madrid_fee.py` | Computes WIPO fees + each Contracting Party's individual fees from the official Schedule (supports colour, LDC, collective marks, grace period, subsequent designation, Cuba's second-part fee), and applies **announced rate changes** by `--date`, flagging date-change crossings and untested components | `py madrid_fee.py --countries ID,IL --classes 2 --date 2026/11/01` |
| Deadline calculator (two families of time limits) | `scripts/madrid_deadline.py` | ① default mode: refusal periods by **declaration** (baseline 12 / 18 if declared / up to 25 months with opposition; subsequent designations run from recordal); ② `--respond`: the holder's deadline to respond to a provisional refusal (built-in WIPO Rule 17(7) data for 38 members, incl. China 15/30 days, France 1 month, US opposition 40 days; applies the six starting points to decide whether counting from the received date is permissible) | `py madrid_deadline.py --register 2026-01-15 --declared-18`<br>`py madrid_deadline.py --respond --cp CN --received 2026-09-20` |
| Renewal reminder | `scripts/madrid_renewal.py` | Computes the renewal window (6 months early, 6-month grace) and the grace-period surcharge | `py madrid_renewal.py --register 2016-07-01 --protection-years 10` |
| Self-test | `scripts/selftest.py` | 9 groups of cases: date boundaries, time-limit conventions, **response periods (15/30 days and the 6 starting points)**, **response-times data ↔ declarations document consistency**, four renewal phases, fee modes, rate effective dates, fees.md ↔ data-file consistency, CLI smoke test | `py -B selftest.py` |
| **Live fee measurement** | `scripts/madrid_feecalc_live.py` | Drives the **WIPO Fee Calculator** with a real browser; obtains per-country authoritative amounts from "Office of origin + number of classes + Contracting Party list" and outputs basic/individual/complementary fees and the total; supports `--colour`, `--collective`, `--dump` for records | `py madrid_feecalc_live.py --origin US --classes 1 --countries JP,ID,IL` |
| **Treaty full-text fetcher** | `scripts/wipo_lex_fetch.py` | Fetches **verbatim full texts** of treaties/Regulations/Administrative Instructions from WIPO Lex text pages (server-rendered, no browser): `--inspect` to survey structure first, `--out` to save as Markdown, `--preserve-notes` to keep old key points as an appendix; automatically handles documents embedded in the `printID` container and Chinese typographic spacing | `py -B wipo_lex_fetch.py --url https://www.wipo.int/wipolex/en/text/384637 --inspect` |

Companion files and key design points:

· `scripts/madrid_fee_data.json`: the **machine-readable mirror** of fee data (WIPO fees + individual fees of 76 Contracting Parties, with charging modes and grace-period rates); the human-readable version is @references/madrid-fees.md. Changes must be kept in sync; the "data consistency" case in `selftest.py` compares them country by country.
· `scripts/madrid_response_times.json`: the data source for **time limits to respond to a provisional refusal** (the complete WIPO Rule 17(7) table, 38 members, with both ex officio/opposition tiers, the six starting points verbatim, and conditional-period footnotes); the human-readable version is @references/madrid-declarations.md §4e-i/§4e-ii; consistency is checked by the "response times data vs. declarations document" case in `selftest.py` (member-by-member comparison of names and starting-point wording).
· `scripts/madrid_dateutil.py`: shared date utilities (natural-month advancement, month-end and leap-year 2/29 fallbacks, `--today` reproduction), reused by the deadline and renewal scripts instead of duplicated implementations.
· The fee calculator implements the official Schedule precisely: no supplementary fee where "all designated Contracting Parties charge individual fees"; no supplementary fee on subsequent designation; **grace-period surcharge at 50% of the basic fee** (653 × 50% = 326.5 → rounded up to 327; the official invoice governs); unlisted Contracting Parties counted at the 100 CHF complementary fee with a flag.
· Refusal-period calculation **does not take liberties**: the default is 12 months and verification of declarations is required; 18 months needs an explicit `--declared-18`; `--country protocol` exists only for backward compatibility and warns that the old convention is obsolete; claiming an opposition extension on top of 12 months is blocked outright (Art.5(2)(c) presupposes an 18-month declaration).
· All three scripts default to UTF-8 output (stdout is reconfigured automatically to avoid cp936 errors in Windows pipes) and support `--today` (reproduction) and `--ascii` (terminal compatibility). Script output is an estimate and a prompt; official notices govern.
· **The live script `madrid_feecalc_live.py` is the decision tool for individual-fee disputes**: the official Fee Calculator is a JSF application that cannot be fetched over HTTP (the Contracting Party list and results are rendered by JavaScript), so it must be driven by a real browser. The script depends on `playwright` + chromium (`pip install playwright` then `playwright install chromium`; it also auto-detects an installed chrome.exe under `%LOCALAPPDATA%\ms-playwright`). **Each tick of a Contracting Party triggers an AJAX re-render and a single click may be swallowed** — the script re-checks the ticked set and re-ticks missing ones for up to 4 rounds; in practice, with many `--countries`, take the closing "N / M ticked" line as authoritative — if M is not reached the result is unusable (exit code 2).
· **Division of labour between the two fee paths (not substitutes)**: `madrid_fee.py` is the **offline snapshot** (works with no network/browser; built-in individual fees of 76 Contracting Parties + announced effective-date changes, applied by `--date`, flagging date crossings and untested components by `--date`); `madrid_feecalc_live.py` is the **official live measurement** (browser-driven; the basis of decision in amount disputes). **For quotes crossing a rate-change date, or where the offline snapshot is over 90 days old, the live measurement governs**; the offline script's value is covering environments where the live script is unavailable and initial bulk budgeting.
· **Treaty full texts can be re-fetched in one command**: when official texts are updated, re-run `scripts/wipo_lex_fetch.py` (verify the head/tail and article counts in `--inspect` mode first, then save). Fetching notes: WIPO Lex text pages embed the whole document in the `id="printID"` container (**the same page may contain treaty texts quoted in official footnotes — this is normal**); after fetching, always verify the last provision (Agreement Art.18 / Protocol Art.16 / Regulation 41 / Administrative Instructions Section 19) to rule out truncation.
· Running the scripts creates `__pycache__` under `scripts/`; to keep the "two-level directory only" structure, run with `py -B selftest.py` (no bytecode written) or delete the directory afterwards.
· WIPO official online calculator: https://madrid.wipo.int/feecalcapp/

Template resources (`templates/` directory — copy and fill in for each job; do not edit the originals):

| Template | File | Use case |
| --- | --- | --- |
| Pre-filing self-check list | `templates/madrid_application_checklist.md` | Item-by-item check before filing MM2 through the Office of origin (China route see §4.10): basic trademark and connecting link, reproduction specifications, MGS classification check, fee estimate with exchange-rate buffer, transmittal and refusal-period alerts |
| Provisional-refusal response memo | `templates/madrid_refusal_response_memo.md` | After a designated Office's provisional refusal: clarify the procedure type, organise the response strategy, control the response deadline, and record the central-attack transformation branch |

### 4.13 Online Verification and Search Scenarios

Scenarios requiring online verification: membership changes, refreshing Contracting Party declarations, individual-fee amounts, CHF exchange rates, MGS standardised terms, international registration status (Madrid Monitor), CNIPA practice guidance, the WIPO official Gazette, and national judicial practice. Official URLs for each scenario are in the §3.0 freshness checklist; recommended search formulas are in @references/madrid-faq.md §V.

### 4.14 Declaration Verification Practice Guide

Follow these steps when choosing designated Contracting Parties for a client:

```
Choose the target designated Contracting Parties
        │
        ▼
① Check whether the country charges an individual fee (Art.8(7)(a))
   → determines fee composition (100 CHF complementary fee or individual fee)
        │
        ▼
② Check the country's refusal period (12 months / 18 months / with opposition extension)
   → determines the best time to withdraw or abandon
        │
        ▼
③ Check for special requirements (e.g. declaration of intention to use, Rule 7(2))
   → prepare in the application file in advance
        │
        ▼
④ Check whether division/merger is available
   → assesses subsequent management flexibility
        │
        ▼
⑤ Check the recordal-of-licence rules
   → if recordal has no international effect there, file a separate domestic recordal
```

Online search formulas:

```
"WIPO Madrid System declarations [country name]"
"马德里体系 [国家名] 声明"
"Madrid Protocol declarations Art.8(7)(a) individual fee"
"WIPO Madrid members declarations 2026"
```

## V. Rules (Constraints / Boundaries)

### 5.1 Fee Terminology (iron rules — never swap)

· Complementary fee = 补充费 = per designated Contracting Party (**applies to Contracting Parties that have not declared an individual fee**, not limited to Agreement Contracting Parties).
· Supplementary fee = 附加费 = per class beyond 3 (not collected where all designated Contracting Parties charge individual fees).
· Agreement = complementary fee + supplementary fee (no individual fee).
· Protocol = optional individual fee (instead of the complementary fee and, where all designated States charge individual fees, instead of the supplementary fee).
· When using English, copy complementary / supplementary / individual exactly — never swap them (verified against the WIPO Schedule of Fees, 2023-02-01 edition).

### 5.2 Counterexamples and Common Mistakes (do not do this)

The complete 16 items (including corrections of this skill's own past errors) are in @references/madrid-faq.md §II. The **most frequent and most consequential** 6:

· **Assuming an 18-month refusal period**: treating "the period has passed = protection obtained" without checking the country's Art.5(2)(b) declaration. Correct approach: start from 12 months, verify declarations first, then fix the period; subsequent designations run from the date of recordal.
· **Confusing complementary and individual fees**: counting 100 CHF per Contracting Party across the board. Correct approach: check the individual-fees page first, and the Art.9sexies(1)(b) safeguard-clause exception.
· **Computing the grace-period surcharge as "50% of the total amount due"**: it is **50% of the basic fee (327 CHF)** (Schedule item 6.5).
· **Paying on the last day of the grace period**: no 3–5 working days' buffer for transfer delays, so the registration lapses.
· **Modifying the goods/services on renewal**: renewal may not modify the registration; changes require a separate change procedure.
· **Doing nothing after a central attack, or filing transformation with WIPO**: transformation applications must be filed **directly with each designated Office** within 3 months of the cancellation.

Bottom line: in Madrid practice, timeliness and formal compliance matter more than advocacy. A missed deadline = an irrecoverable right (except in the few countries that allow restoration).

### 5.3 Other Constraints and Boundaries

· This skill centres on the international-phase procedures and stays **office-neutral**: apart from the sections expressly marked "China / CNIPA" (§3.3, §4.10 and the corresponding items in §3.8), the content applies to trademark practitioners in any Contracting Party, including overseas IP lawyers and in-house counsel.
· WIPO Lex official texts are the highest authority. **The Chinese files for the Agreement / Protocol / Common Regulations / Administrative Instructions are now verbatim full texts** (fetched 2026-09-25 from the official WIPO Lex Chinese translations via `scripts/wipo_lex_fetch.py`, with only typographic spacing normalised); the "Appendix: key points and errata" at the end of each file is skill-compiled content, not official text — **when citing provisions, always rely on the body (full text)**. The English files are the official English full texts. When official texts are updated, the same script can re-fetch them.
· Volatile data (fees / declarations / member counts / provisions) must be verified online per the §3.0 freshness checklist; search-engine caches are prohibited. @references/madrid-fees.md is the sole authoritative source for fee amounts.
· China-related practice follows the Protocol first; **all members are Protocol Contracting Parties** (WIPO Key Facts, verified 2026-09-23) — no Agreement-only members remain; but the Art.9sexies(1)(b) safeguard clause may nullify declarations between dual-party States — verify case by case.
· Do not send anything externally on the user's behalf; do not substitute for legal advice.

### 5.4 Capability Boundaries and How to Ask

To avoid unrealistic expectations, note the following boundaries before using this skill, and consider the suggested ways of asking.

**1. What this skill is not good at / does not cover (do not expect it here)**
· Article-by-article reading of the substantive trademark law of each Contracting Party and litigation advocacy: this skill covers Madrid System procedures and common rules, but the domestic law of a designated Contracting Party (e.g. specific provisions of the US Lanham Act, the EU trade mark regulation, national refusal-review practice) must be referred to that country's law or a local practitioner; for US-side Madrid procedures and fees (USPTO §7.6/§7.7, USD) see the `us-tm-madrid` skill if installed, otherwise the USPTO Fee Schedule.
· Single-jurisdiction / regional trademark applications: purely domestic filings made directly with the USPTO, EUIPO, JPO etc. (outside the Madrid route) are not part of this skill's main workflow; they appear only as interface comparisons with Madrid.
· Subjective judgments of similarity and success-rate predictions: this skill provides a refusal-response framework and templates, but does not predict registrability, similarity risk or case outcomes for any specific mark.
· Real-time automatic fetching of fees / exchange rates: fees, individual fees and CHF rates are volatile; this skill does not fetch them live and they must be verified online per §4.13; the calculator contains only verified WIPO fee baselines and never silently estimates individual fees.
· Formal legal opinions or replacement of representative decisions: this skill is a practice-support tool; it does not replace the judgment of a licensed practitioner and does not issue opinions having legal effect.
· Case-specific strategy for unpublicised matters: without the case file, no targeted plan can be given — supply the refusal notice, registration number, designated Contracting Parties etc. first.

**2. How to ask for the best answer**
· State the type of matter: filing / renewal / provisional-refusal response / change or assignment / central-attack transformation / fees / time limits — different types follow different procedures.
· Give the key facts: list of designated Contracting Parties, number of classes, status of the basic right (registered or pending), date/number of the international registration, whether a refusal was received and from which country.
· Say what output you expect: fee estimate, deadline countdown, response template, procedural steps, or a risk checklist.
· Trigger words help, but natural language works: e.g. "Madrid provisional refusal Japan 18 months — how to respond", "Madrid renewal registered 2016 — still in time?".
· For volatile data, ask for verification proactively: e.g. "please verify online the latest US individual fee".

**3. Realistic expectations**
· Fees, individual fees, Contracting Party declarations, member counts and provisions are all volatile; the built-in values are baselines only, and the official live WIPO / CNIPA pages govern.
· The Madrid System revolves around procedural compliance and time limits; a missed deadline is usually irrecoverable; this skill can compute deadlines, but always double-check against the official notice.
· The templates and strategies provided are general practice references; adapt them to the designated Contracting Party's domestic law and the facts of the case before use.

## VI. Output Format (binding only on "text delivered to the user")

> Scope note: the constraints below apply **only to the text delivered to the user after the skill is invoked**; they do not bind the skill's own reference/guidance content. Markdown tables (comparison tables, directory tables, fee tables etc.) inside the skill's own files (the sections of this SKILL.md and the `references/` knowledge base) are legitimate knowledge-base content and are retained.

· The text delivered to the user **must not use Markdown tables** (including `|` tables and `|---|` separator rows).
· Alternative presentations (choose one or combine, by scenario):
  - Fee / deadline lists → one line per item, "Item: value (note)", e.g. "Basic fee: 653 CHF (black-and-white, Schedule item 2.1)";
  - Multi-Country comparison → one paragraph or one `·` bullet per Contracting Party, fields separated by ";";
  - Steps and procedures → numbered sections + `·` sub-items, or an indented plain-text flow;
  - Where horizontal alignment is needed → simulate columns with full-width spaces or indentation, not `|` tables.
· Layer with `·`, numbering or sub-headings; amounts and periods must not omit the unit or the governing provision.
· If data cannot be found, reply directly with "None"; fabricating, estimating or placeholder-filling are strictly prohibited.
· Values (CHF amounts, periods) must state the baseline date and source (e.g. "WIPO Schedule of Fees 2023-02-01 edition, verified 2026-09-23").
· For volatile data (fees, individual fees, exchange rates, declarations, member counts), state whether a refresh/verification is needed; never pass off a snapshot as a live value.

---

> **Version**: v3.4.5
> **Created**: 2026-07-01
> **Last revised**: 2026-09-25
> **Legal basis as at**: 1 November 2025 (latest Common Regulations); the Schedule of Fees is a separate legal instrument, 2023-02-01 edition, verified 2026-09-23
> **Revision highlights**: ⓪ **Added the live fee script `scripts/madrid_feecalc_live.py`** (browser-driven official Fee Calculator, per-country authoritative amounts, built-in tick retries), written into §4.8 and §4.12 — closing the long-standing gap that "individual fees need online verification but cannot be fetched over HTTP"; **added `--date`** (computing two budget sets across a rate-change date by intended filing date — the decisive parameter against misquoting), and based on live measurements recorded **rate changes effective 2026-11-01: Indonesia 91→125, Israel 471→503** (written into @references/madrid-fees.md §X). ① Unified refusal periods as "12-month baseline + 18 months if declared under Art.5(2)(b) + up to about 25 months with (2)(c) opposition", removing the conflict with §3.4 / the Protocol text. ② Corrected the grace-period surcharge to "50% of the basic fee (327 CHF)" (Schedule item 6.5). ③ Corrected the complementary-fee rule to "Contracting Parties that have not declared an individual fee", adding the Art.9sexies(1)(b) safeguard-clause exception. ④ Updated the member count to 117 members / 133 countries and territories (WIPO members page verified 2026-09-23; Saudi Arabia effective 2026-10-08). ⑤ Added the §3.0 volatile-data freshness checklist and the §4.0 task-routing table. ⑥ Moved fees and FAQ/counterexamples down into `references/madrid-fees.md` and `references/madrid-faq.md`, eliminating three parallel fee datasets and circular references. ⑦ **Script refactor**: added `madrid_dateutil.py` (shared date utilities) and `madrid_fee_data.json` (individual-fee data source for 76 Contracting Parties); the three scripts now compute by "declaration thresholds / official Schedule" conventions, with new `--base-months/--declared-18/--today/--ldc/--collective/--origin/--ascii`, unified UTF-8 output, and a new `selftest.py` (6 groups of cases including fees.md ↔ data-file consistency). ⑧ **Trigger and wording polish**: the three descriptions completed with Chinese/English trigger words (subsequent designation, assignment/limitation/renunciation, representative, declaration of intention to use, eMadrid/ROMARIN/MGS), the §II task list updated to match, the §4.0 routing table extended with subsequent designation, platform operations and data freshness; cross-skill dependencies (`us-tm-madrid`, `legal-doc-converter`) rewritten conditionally ("if installed … otherwise …") to avoid dangling references; §VI added alternative presentations (per-line "Item: value", per-Country bullets, indent alignment) and baseline/source labelling while keeping the table ban; removed subjective "recommendation" ranking from the payment-methods part of `madrid-fees.md`. ⑨ **Response deadlines for China completed + offline fee path aligned to effective dates**: (a) per the WIPO Rule 17(7) table (updated 2026-08-28), the holder's deadlines to respond to a provisional refusal — for a designation of China **15 days for ex officio refusals and 30 days for opposition-type refusals**, both from **the date the holder receives the WIPO transmittal** — and clarified that this is a different time limit from the 18-month **refusal period** within which CNIPA must notify; written into §3.0, the §4.4 checkpoints, §4.10 (CNIPA as designated Office), the new §4.11 response-deadline table, §II Q11, @references/madrid-declarations.md §4e and row 10 of the China declarations, and @references/madrid-faq.md Q13 and counterexample 7; noted in §4.12 that `madrid_deadline.py` computes only the 12/18/25-month refusal periods, not day-based response periods. (b) Added an effective-date dimension to the offline fee path: `madrid_fee_data.json` gained `effective_date_changes` (effective 2026-11-01: Indonesia 91→125, Israel class 1 471→503); `madrid_fee.py` gained `--date` to apply announced changes by charging date, flag cross-date situations requiring two budgets, and prompt (without extrapolating) on components not yet measured (ID/IL renewal side); `selftest.py` extended to 9 groups (new "rate effective dates"). ⑩ **Full inclusion of the WIPO Rule 17(7) response-times table**: previously only the URL and China's row were included; now all **38 members** are covered (both ex officio/opposition tiers, the six starting points verbatim, conditional-period footnotes for Germany/Lithuania, and the 38/117 coverage warning), written into @references/madrid-declarations.md §4e-i/§4e-ii (with the scheduling conclusion that "only 'date of receipt' types can be counted down from the received date; counting other starting points from receipt overstates the time remaining"); added the machine-readable mirror `scripts/madrid_response_times.json`; `madrid_deadline.py` gained `--respond` (`--cp/--received/--base-date/--limit-days/--limit-months`), which **refuses to count from the received date for members whose official starting point is not "date of receipt" and requires the official base date**, and gives both the main and the conservative deadline for conditional periods; §4.11 added a comparison of 8 common members with pitfall notes; §4.4 checkpoints reordered to fix the starting point before computing the period. ⑫ **Errata in the treaty reference texts** (three rounds of article-by-article comparison between "Chinese key points ↔ English full text"): Protocol — Article 5bis (proof of lawful use is exempt from legalisation/authentication, effective directly under the text, not "as provided by the Regulations"); Article 5(2)(a) (removed a misplaced "no authentication", added "within the time limit of the applicable law, subject to (b) and (c)"); (2)(c) (added the advance-notice condition before expiry of the 18 months; two cumulative conditions); (2)(d)/(7)(b) ("the document referred to in Article 14(2)" and application only to international registrations dated no earlier than the declaration's effective date); Article 6(3) (added withdrawal/renunciation after the five years where proceedings started within them); Article 8(7)(a) (supplementary-fee waiver limited to lists entirely of declared parties); Article 9sexies(2) (review-period start corrected to 2011-09-01; removed "historical arrangement" and noted the safeguard clause remains in force and is still applied in the current Schedule); Article 15(5) (split into (a)/(b), (b) addressing registrations effective outside the denouncing party). Agreement — Article 3(5) (inverted subject of the publication duty); Article 8(2)(c) (complementary fee limited to extension requests under Article 3ter; removed "per designated State"); Article 9quater(1)(b) (scope is "all or part of the provisions preceding this Article"); header "Article 1–16" corrected to 1–18 (27 numbered units). Regulations — added Rule 34(3)(d) (non-payment of the second part cancels the registration in that Contracting Party); Rule 17(2)(viii) (notice must state the start and end dates of the time limit; items (i)–(x) completed); Rule 24(5)(c) (designation of that Contracting Party deemed not included); Rule 12(8bis) (3-month period and the "goods/services concerned deemed not included" consequence); Rule 5bis list completed (20bis(2)/27bis(3)(c)/39(1)); Rule 32 (the Gazette does **not** identify the specific goods/services; added 17(5)(d)/(e) declarations and 18bis/18ter); Rule 40(1) (these Regulations entered into force 2020-02-01, replacing the 2020-01-31 Common Regulations; 2025-11-01 is the version label); five practice points (electronic communication, "preferably" standardised wording, the 18-month citation, no fee for merger, LDC relief in the Schedule); removed the untrue "including the Schedule of Fees" from the English Regulations header. ⑬ **Treaty files converted to verbatim full texts**: at the user's request, `madrid-agreement.md`, `madrid-protocol.md`, `madrid-regulations.md` and `madrid-admin-instructions.md` were converted from "key-point summaries" to **verbatim full texts of the official WIPO Lex Chinese translations** (fetched 2026-09-25 with the new `scripts/wipo_lex_fetch.py`, only typographic spacing normalised); the former (corrected) key points were retained in full as an "Appendix: key points and errata" at the end of each file, with the rule that "the body prevails for citations". Fetching notes: WIPO Lex text pages embed the entire document in the `id="printID"` container, and **official footnotes on the page quote other treaty texts verbatim (e.g. Protocol footnotes 3/4 quoting Agreement Articles 10/12) — this is normal, not a fetching error**; crude tag-stripping eats the tail of the body (it once lost Protocol Articles 13–16 — fixed). Verified last provisions: Agreement Art.18, Protocol Art.16 + footnotes, Regulation 41 + footnotes 1–9, Administrative Instructions Section 19. ⑪ **Reconciling the two formulations of the review period**: clarified the relationship between "15 days in the WIPO table (from receipt of the transmittal)" and the practice "30-day review period" — the latter results from Article 10 of the Implementing Regulations ("electronic service is deemed made 15 days after dispatch") superimposed on the 15-day review period (i.e. WIPO dispatch date + 30 days); `madrid_response_times.json` gained a `deemed_service` rule, `madrid_deadline.py --respond` gained `--notified` (deemed service from the dispatch date), and where both dispatch and receipt dates are given it prompts to **take the earlier to control risk**; the conclusion was written into §4.11, @references/madrid-declarations.md §4e and @references/madrid-faq.md Q13 (including a note that the opposition-type superposition of dispatch date + 45 days has no express official basis).
> **Structural conventions**: aligned with the WorkBuddy official skill development documentation (https://open.workbuddy.cn/docs/skill) — the required fields description / description_zh / description_en / version / author are all present, together with name / display_name / display_name_en / category; version numbers follow Semantic Versioning (SemVer); reference materials are cited uniformly as "@" plus a relative path (the @ followed by the file name inside the references directory, without backticks). **allowed-tools is treated as optional and left without a whitelist** — the skill needs to search 15 reference files under references/ (13 Markdown + 2 official PDFs); a whitelist would block search tools such as Grep/Glob and cannot exhaustively enumerate MCP tool names — not worth it. **Single-point data maintenance**: the sole authoritative source for fee amounts is `references/madrid-fees.md` (SKILL.md §4.8 keeps only composition rules and error-prone points); the sole authoritative source for FAQ and counterexamples is `references/madrid-faq.md`; the sole authoritative source for declarations is `references/madrid-declarations.md` (17 categories, numbering as in that file).
> **Directory depth**: this skill uses a strict two-level structure (level 1 = SKILL.md / references/ / scripts/ / templates/; level 2 = the files inside each directory), meeting the open platform's "two levels only" requirement, with no nesting at level 3 or deeper. When adding sub-resources, do not create further subdirectories under references/, scripts/ or templates/.
> **File encoding**: all **Markdown files (SKILL.md, references/, templates/) use pure CRLF, no BOM** (skill-family convention); `.py` and `.json` files under `scripts/` use LF and UTF-8 without BOM, consistent with the Python ecosystem and not subject to that convention.
> **Script maintenance**: when changing fee amounts, keep `references/madrid-fees.md` and `scripts/madrid_fee_data.json` in sync, and run `py scripts/selftest.py` to pass all cases before committing.
> **Maintenance recommendation**: revise periodically in line with official WIPO updates and CNIPA practice guidance; trigger verification per the review cycles in §3.0.
