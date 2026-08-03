# Working File Templates — Ecommerce

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — Configuration table keys and preference areas alike | `~/Clawic/data/ecommerce/config.yaml` | Key by key, read-modify-write |
| Store facts, channels, current metrics, margins, suppliers, pain points, due dates, box index | `~/Clawic/data/ecommerce/memory.md` | Rewritten in place; stays small |
| Monthly metric rows — sessions, orders, CR, AOV, revenue, CM, refund rate, CAC | `## Metrics` in `memory.md`; `~/Clawic/data/ecommerce/metrics.md` once it outgrows the section | One row per month, never per week |
| Per-SKU or per-category economics — price, COGS, fees, freight, CM, MAP floor | `## Unit Economics` in `memory.md`; `~/Clawic/data/ecommerce/unit-economics.md` once it outgrows the section | One row per SKU or category |
| Sales channels and their fee stack, payout lag, share of revenue | `## Channels` in `memory.md`; `~/Clawic/data/ecommerce/channels.md` once it outgrows the section | One row per channel |
| Suppliers and 3PLs: lead time, MOQ, terms, last price change | `## Suppliers` in `memory.md`; `~/Clawic/data/ecommerce/suppliers.md` once it outgrows the section | One row per supplier, person referenced by name only |
| Wholesale accounts: tier, MOQ, payment terms, credit limit | `## Wholesale Accounts` in `memory.md`; `~/Clawic/data/ecommerce/wholesale-accounts.md` once it outgrows the section | One row per account, person referenced by name only (`b2b.md`) |
| The person behind a supplier, 3PL, agency, or wholesale account | `~/Clawic/data/contacts/contacts.md` (**shared**) | One row per person, every skill's contacts in one file |
| Platform plan, apps, and recurring tool costs | `~/Clawic/data/finances/subscriptions.md` (**shared**) | One row per subscription, amount with currency |
| A launch, replatform, or peak campaign run as a project | `~/Clawic/data/projects/<project>.md` (**shared**) | One file per project from the first one |
| The store domain, its registrar and expiry | `~/Clawic/data/domains/domains.md` (**shared**) | One row per domain |
| The machine a self-hosted store runs on | `~/Clawic/data/servers/servers.md` (**shared**) | One row per host, every provider in one inventory |
| A/B tests and their decision | `~/Clawic/data/ecommerce/experiments/<year>.md` | Append-only, cut by year |
| Promotions, sales and codes with their margin outcome | `~/Clawic/data/ecommerce/promotions/<year>.md` | Append-only, cut by year |
| Chargebacks and disputes with their deadline and outcome | `~/Clawic/data/ecommerce/disputes/<year>.md` | Append-only, cut by year |
| Outages, oversells and other incidents with revenue impact | `~/Clawic/data/ecommerce/incidents/<year>.md` | Append-only, cut by year |
| Things you produced that get re-read — runbooks, a policy that finally worked, the tracking plan, a redirect map, a fraud rule set, a dunning ladder, a peak retro, a decision with its reasoning | `~/Clawic/data/ecommerce/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| **Anything durable this table does not name** | `~/Clawic/data/ecommerce/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind | Nowhere under `~/Clawic/data/` | Pointer only — see Secrets |
| Customer identity of any kind | Nowhere under `~/Clawic/data/` | Aggregate or order id only — see Secrets |

Deciding where something unnamed goes, in this order: (1) would another skill want to read it — a person, a project, a domain, a recurring cost, a machine? Then it belongs in the shared box, not here. (2) Is it a text read whole when its subject comes up — a procedure, a policy, a plan, a decision with its reasoning? Then `artifacts/`, its own file from the first one. (3) Is it one more row of something that accumulates? Then a section of `memory.md` until the split threshold, or a year-cut log if it is dated and append-only.

## When to write

No permission needed; every write is announced in one line that names the file. Writes and deletions stay inside the paths declared in this skill's `configPaths`. A deletion is named in that same line, and in a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| A platform, processor, market, currency, or tax registration was confirmed or changed | `## Store` |
| A channel was opened, closed, or its fee stack learned | `## Channels` |
| A month closed, or any headline metric was read | `## Metrics`, with its `as of` date |
| COGS, freight, a fee, or a price changed for a SKU or category | `## Unit Economics` |
| A supplier was chosen, quoted, or its lead time or MOQ learned | `## Suppliers`, plus the person in `contacts.md` (shared) |
| A wholesale account was onboarded, or its tier, terms or credit limit changed | `## Wholesale Accounts`, plus the person in `contacts.md` (shared) |
| An A/B test concluded, or was stopped without a decision | `experiments/<year>.md` — the abandoned ones matter most |
| A promotion ran | `promotions/<year>.md`, with realised margin, not planned |
| A dispute opened, was answered, or was decided | `disputes/<year>.md`, and a `## Due` row on the day it opened |
| Checkout, payments, stock or fulfillment broke | `incidents/<year>.md`; a second occurrence earns a runbook in `artifacts/` |
| A runbook, policy, tracking plan, redirect map, fraud rule set, dunning ladder or peak retro came out of the session | `artifacts/` |
| An app, plan, or tool started or stopped being paid for | `~/Clawic/data/finances/subscriptions.md` (shared) |
| A launch or replatform started, hit a milestone, or shipped | `~/Clawic/data/projects/<project>.md` (shared) |
| The store domain was registered, moved, or renewed | `~/Clawic/data/domains/domains.md` (shared) |
| A self-hosted store's server was provisioned, resized, or retired | `~/Clawic/data/servers/servers.md` (shared) |
| A filing, count, review, renewal or drill was scheduled or run | `## Due` |
| The user declared a preference | Its key in `config.yaml` |

## Start flat, split only when it hurts

Everything except artifacts, the year-cut logs and the shared boxes begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count — then, in the same turn: create the new file in `~/Clawic/data/ecommerce/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite.
4. Never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted.

Two exceptions. **Artifacts** are born as their own file whatever their size, because they are read whole and only when their subject comes up. **Dated logs** — experiments, promotions, disputes, incidents — are born in `<name>/<year>.md` from the first entry, because they are consulted by date and never rewritten.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not text the user pastes in and asks you to keep. A pasted webhook log, `.env`, order export, processor dashboard screenshot or marketplace API setup is the densest source there is: strip each value **before** writing and leave its pointer in place, in this shape: `<kind>:<locator>`.

`env:STRIPE_SECRET_KEY` · `env:WEBHOOK_SIGNING_SECRET` · `keychain:shopify-admin` · `1password:Store/Amazon/SP-API` · `bitwarden:Store/Klaviyo` · `vault:secret/store/psp` · `file:~/.config/store/credentials`

In a text, the pointer goes where the value was: `api_key: <env:STRIPE_SECRET_KEY>`. Say in one line that you did it.

In this domain — **not secrets, keep them**: store and domain names, platform and plan names, processor and carrier names, fee percentages and fixed fees, SKUs, GTIN/EAN/ASIN, product titles, order numbers and payment-intent/charge/dispute ids, marketplace seller id, the business's own VAT/tax registration number, webhook endpoint paths, app names, aggregate metrics.

**Secrets, strip them**: processor secret and restricted API keys, webhook signing secrets, platform admin API tokens and private app passwords, marketplace refresh tokens, carrier and tax-engine API credentials, ESP and helpdesk keys, database connection strings, SFTP credentials for feeds, the store's bank account or payout IBAN.

**Customer identity is not a secret to be pointer-ised — it simply does not come here.** No names, emails, addresses, phone numbers, IPs, tracking numbers, or order exports. An incident row records "38 orders affected", never who they were. **Card number, CVV and expiry are never written, repeated, or stored anywhere, in any form**: if they appear in pasted text, delete them, keep the last four digits only if the user needs them to identify the order, and say so in one line.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [shared boxes](#shared-boxes) · [artifacts/](#artifacts) · [dated logs](#dated-logs) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/ecommerce/` if it does not exist.

```yaml
platform: shopify
business_model: dtc
home_market: ES
currency: EUR
psp: stripe
monthly_orders: 900
target_margin_pct: 45
max_discount_pct: 20
target_ltv_cac: 3
fraud_posture: balanced
pci_scope: hosted-fields
bulk_change_confirm: true

# Preference areas — free-form keys added as the user reveals them.
# A preference the user states is a declaration and belongs here, never in memory.md.
integrations:
  esp: klaviyo
  helpdesk: gorgias
  threepl: none            # self-fulfilled from the office
  reviews: judge.me
conventions:
  sku_scheme: "CAT-MODEL-SIZE-COLOR"
  order_prefix: "ES-"
platform_and_markets:
  ships_to: [ES, PT, FR, DE]
  incoterms: DDP
  channels: [own-store, amazon-es]
brand_and_policy:
  discounting: "twice a year, never sitewide above 20%"
  returns: "free returns within 30 days, above the legal 14"
restrictions:
  never_sell: [food, batteries]
cadence:
  metrics_review: "monthly, day 3"
  cycle_count: monthly
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the user's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# Ecommerce Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- Monthly metrics (26 months) → `metrics.md`; read before any comparison or trend claim
- Per-SKU economics (41 SKUs) → `unit-economics.md`; read before any discount, bid or channel decision
- Suppliers and terms (17) → `suppliers.md`; read before any reorder or lead-time promise
- A/B tests and decisions (2026) → `experiments/2026.md`; read before proposing a test that may already have run
- Promotions and realised margin (2026) → `promotions/2026.md`; read before planning any promo
- Disputes (2026) → `disputes/2026.md`; read when a chargeback arrives or the dispute rate is questioned
- Incidents (2026) → `incidents/2026.md`; read when checkout, stock or fulfillment breaks, and before peak planning
- Checkout outage runbook → `artifacts/runbook-checkout-down.md`; read the moment orders stop
- Return policy that finally worked → `artifacts/policy-returns.md`; read before changing returns or answering a refund edge case
- Tracking plan → `artifacts/tracking-plan.md`; read before touching analytics or trusting a number

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Metrics review (close last month) | month, day 3 | 2026-07-03 | 2026-08-03 |
| OSS VAT return | quarter | 2026-07-20 | 2026-10-20 |
| Dispute deadline sweep | week | 2026-07-24 | 2026-07-31 |
| Stuck-order and failed-payment sweep | week | 2026-07-24 | 2026-07-31 |
| Cycle count (A items) | month | 2026-07-06 | 2026-08-06 |
| Dead-stock sweep (no sale in 90d) | quarter | 2026-06-30 | 2026-09-30 |
| COGS and freight refresh | quarter | 2026-06-30 | 2026-09-30 |
| App and plan cost review | quarter | 2026-06-30 | 2026-09-30 |
| Peak readiness kickoff | year, September | 2025-09-08 | 2026-09-07 |

## Store
Shopify, DTC, home market ES, EUR. Ships ES/PT/FR/DE, DDP. Stripe + PayPal + Bizum.
OSS-registered since 2025-04. 340 active SKUs, 6 categories. Self-fulfilled from the office.
Domain: see `~/Clawic/data/domains/domains.md`.

## Channels
| Channel | Share of revenue | Commission | Payment fee | Payout lag | Notes |
|---|---|---|---|---|---|
| own-store | 78% | — | 1.5% + 0.25 EUR | 2 days | Stripe, Bizum for ES |
| amazon-es | 22% | 15% referral | included | 14 days | FBM; return rate 2× the store's |

## Metrics
| Month | Sessions | Orders | CR | AOV | Revenue | CM% | Refund rate | CAC | As of | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06 | 84,200 | 1,910 | 2.27% | 47 EUR | 89,770 EUR | 44% | 9.1% | 21 EUR | 2026-07-03 | closed |
| 2026-07 | 22,600 | 480 | 2.12% | 44 EUR | 21,120 EUR | 41% | 9.8% | 25 EUR | 2026-07-08 | month-to-date |

## Unit Economics
| SKU / category | Price | COGS | Payment fee | Freight | Pick/pack | Returns cost | CM | CM% | As of |
|---|---|---|---|---|---|---|---|---|---|
| BAG-01-BLK | 50 EUR | 18 EUR | 1.00 EUR | 4.50 EUR | 1.50 EUR | 0.48 EUR | 24.52 EUR | 49% | 2026-06-30 |

A supplier MAP or resale-price floor is a per-SKU constraint, not a policy paragraph: add a `MAP floor` column (amount with currency) to this table the first time any SKU has one, and leave it blank for the rest. The contract wording and the enforcement stance live in `artifacts/policy-pricing.md` (`pricing.md`, `b2b.md`).

## Suppliers
| Supplier | Contact | Lead time | MOQ | Terms | Last price change | Notes |
|---|---|---|---|---|---|---|
| Tannery Sur | tannery-sur (contacts) | 35 days | 120 units | 50% deposit, 50% on ship | 2026-04, +6% | Closes all August |

## Pain Points
2026-03: oversold 38 units of BAG-01 during a sale — Amazon sync ran every 30 min. Buffer now 2× peak per interval.
2026-05: two months of ad reporting were unusable after a consent-mode change. Tracking plan written after that.

## How They Work
Two people, no developer on staff. Wants the exact setting or the exact code, plus the margin figure. Will not run a bulk change without seeing the affected count first.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Every dated obligation this skill meets (SKILL.md Rule 8) belongs here, and the cadences come from `cadence` in `config.yaml` when the user has declared them.
- **`## Metrics`**: `As of` is the day the number was read. A row whose `As of` is not the last day of the month is month-to-date and is never compared against a closed month. Re-reading the current month **overwrites** its row; never a second row for the same month. Amounts carry their currency, rates carry their denominator, and the definitions are the ones in SKILL.md Metrics That Decide — if a tool reports something else, record the tool in `Notes` rather than changing the definition.
- **`## Unit Economics`**: the row is only useful with `As of`, because COGS and freight move. A row older than the last `COGS and freight refresh` in `## Due` is a hypothesis; recompute before quoting a margin from it.
- **`## Channels`**: the fee stack is the point — commission, payment fee, fulfillment fee, ad levy, and payout lag, which is a cash-flow fact, not an accounting one. Share of revenue is what makes channel concentration visible before it becomes a dependency.
- **`## Suppliers`**: lead time is measured from order placed to goods received, including customs, not the supplier's quoted production time. The person lives in `contacts.md`; here only their key.
- **`## Pain Points`**: one line each, dated, with what changed as a result. This is the section that stops the same oversell or the same tracking break from being rediscovered every quarter.
- These headings are exactly the ones `metrics.md`, `unit-economics.md`, `channels.md` and `suppliers.md` get when their sections outgrow this file, so each split stays a copy-paste.

| Status | Meaning |
|-------|---------|
| `ongoing` | Still learning the store, its numbers and its constraints |
| `complete` | Know the platform, channels, margins and workflow well |

## Shared boxes

These live outside the skill's folder and are shared with every other Clawic skill. The user may have none of the owning skills installed, so the format and the protocol travel with this one. Three rules apply to all of them: **read the file before adding**; if the identity key already exists, **update that row in place** rather than appending a second; and **if the file already exists with different columns, match its columns** and add anything missing as a trailing note — never rewrite someone else's header.

### contacts/ — suppliers, 3PLs, agencies, wholesale accounts

`~/Clawic/data/contacts/contacts.md`

```markdown
# Contacts

| Name | Key | Role | Preferred channel | Context | Last contact | File |
|------|-----|------|-------------------|---------|--------------|------|
| Tannery Sur | ventas@tannerysur.example | supplier | email | Leather goods, 35d lead, MOQ 120 | 2026-07-14 | — |
| Lisa Braun | lisa@thirdparty.example | 3PL account manager | email | DE warehouse, onboarding Q4 | 2026-07-02 | — |
```

- **Identity is `Key`**: lowercase email, else a handle, else `<kebab-name>` plus a stable disambiguator. The key is a column of the row, never implicit.
- Only business relationships go here — suppliers, 3PLs, agencies, freelancers, wholesale buyers. **Retail customers never do** (SKILL.md Rule 9).
- Retiring a relationship deletes the row and notes the date in `## Suppliers` of `memory.md`. A contact list that only grows stops being one.
- **Scale cut**: one row per person while there are ≤15, or until one no longer fits its row. Past that, `~/Clawic/data/contacts/<name>.md` per person and `contacts.md` becomes the index, keeping the `File` pointer.
- Terms, lead times and MOQs stay in the ecommerce box; the person stays here. Never duplicate either side.

### finances/ — what the store pays every month

`~/Clawic/data/finances/subscriptions.md`

```markdown
# Subscriptions

| Service | What for | Amount | Cycle | Renews | Cancel by | Owner |
|---------|----------|--------|-------|--------|-----------|-------|
| Shopify | store platform, Grow plan | 89 EUR | monthly | 2026-08-04 | — | store |
| Klaviyo | email + SMS, 30k profiles | 180 EUR | monthly | 2026-08-01 | — | store |
```

- **Identity is the service name.** Update the row in place when the plan or amount changes; do not keep the old amount as a second row.
- **Amounts carry their currency inside the value** (`89 EUR`), because rows written by other skills are in other currencies and someone will add the column up. An estimate carries the date it was estimated.
- A cancelled tool has its row deleted and the date noted in `## Store` of `memory.md` — the app stack is the second-largest recurring cost after COGS and only a shrinking list proves it was reviewed.
- `subscriptions.md` is a single table and is not split: the list stays short because cancelling deletes the row.

### projects/ — a launch, a replatform, a peak campaign

`~/Clawic/data/projects/<project>.md`, one file per project from the first one. Contains objective, status, milestones and the decisions taken with their reasoning. Closing sets `status: done | cancelled — <date>` inside the file; the file is never deleted, because it is the record of what shipped. **Scale cut**: past ~20 closed projects, move them to `~/Clawic/data/projects/archive/<project>.md` without renaming the file, so the active folder stays readable. The full artifact (redirect map, cutover checklist) stays in `artifacts/` and is referenced from the project file by name.

### domains/ — the store's address

`~/Clawic/data/domains/domains.md`

```markdown
# Domains

| Domain | Registrar | Expires | Auto-renew | DNS | Used for |
|--------|-----------|---------|------------|-----|----------|
| example-store.com | registrar-name | 2027-03-11 | yes | cloudflare | storefront + email |
```

- **Identity is the domain name.** Update the row in place when the registrar, expiry, DNS or use changes; never add a second row for the same domain, and never touch a row for a domain the store does not use.
- An expiring store domain is a total outage with a slow fuse: whenever a domain is added, put its renewal in `## Due` a month before `Expires`.
- **Removal**: a domain sold, transferred out, or deliberately allowed to lapse has its row deleted and the date noted in `## Store` of `memory.md`, along with its `## Due` renewal row. A dead domain left in the table gets renewed by accident, and a redirect nobody owns keeps pointing at it.
- **Scale cut**: one row per hostname while there are ≤40; past that, group by apex domain in `~/Clawic/data/domains/<apex>.md` with the same columns, and `domains.md` becomes the index (`Apex | Registrar | Expires | → file`). If the folder already looks like that, follow it.
- Redirect maps and migration cutover plans are ecommerce artifacts, not domain rows — they go to `artifacts/` and are referenced here by name.

### servers/ — only when the store is self-hosted

`~/Clawic/data/servers/servers.md`, shared with every infrastructure skill.

- **Identity is `Name` + `Provider`.** Update your own row in place; never touch a row whose `Provider` you did not write, and never start a parallel file.
- Columns: `Name | Provider | Account / Project | Region | Type | Role | Monthly | Access reference`. `Role` says what it runs (`woocommerce prod`, `staging`). `Monthly` carries its currency in the value.
- Access reference is a pointer only (`file:~/.ssh/id_ed25519`, `1password:Store/VPS`), never a key or password.
- Retiring a host deletes its row and notes the date in `## Store` of `memory.md`.
- **Scale cut**: one row per host while there are ≤15; past that, `~/Clawic/data/servers/<name>.md` per host with the same fields and `servers.md` becomes the index (`Name | Provider | Role | → file`). If the folder already looks like that, follow it.

## artifacts/

One file per thing, at `~/Clawic/data/ecommerce/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **a runbook for a failure that recurred**, **a policy that finally worked** (returns, discounting, fraud rules, dunning ladder, compensation), **the tracking plan and metric definitions**, **a migration or redirect map**, **a peak retro**, **a decision with what was rejected**. Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn. Every secret inside is already a pointer, and no customer appears by name.

```markdown
# Runbook — orders stopped
*Read the moment order volume drops to zero or checkout errors. Written 2026-07-26.*

Check in order, with the expected answer for each: payment method status → shipping-rate
endpoint → app that last changed → theme deploy → DNS/CDN. Ends with who to tell and the
holding message to publish.
```

```markdown
# Policy — returns
*Read before changing returns or answering a refund edge case. Working as of 2026-07-26.*

The published window and why it exceeds the legal minimum, the inspection grid, the partial-refund
percentages, the per-customer abuse thresholds, and the two cases that always go to a human.
```

```markdown
# Decision — Amazon as a second channel, not a first
*Read before adding or dropping a channel. 2026-07-26.*

Decision: ...one sentence...
Margin: CM 49% own store → 27% on Amazon after 15% referral and the doubled return rate.
Rejected: FBA — freight in plus long-term storage took two SKUs negative at the observed velocity.
Revisit when: the store's own paid CAC exceeds 30 EUR, or Amazon share passes 35% of revenue.
```

If the user tracks this work as a project, the one-line decision summary also belongs in `~/Clawic/data/projects/<project>.md`, with the full artifact staying here and referenced by name.

## Dated logs

Append-only, one file per year, never rewritten. Each is born with its first entry.

`experiments/<year>.md` — every A/B or holdout test, including the ones stopped early.

```markdown
# Experiments — 2026

| Started | Ended | Where | Hypothesis | Metric | Sample/arm | Result | Decision |
|---------|-------|-------|-----------|--------|-----------|--------|----------|
| 2026-05-04 | 2026-05-19 | PDP | Delivery date above the button lifts add-to-cart | RPS | 61,000 | +6.1% RPS, p 0.03 | shipped |
| 2026-06-02 | 2026-06-09 | Cart | Free-shipping progress bar lifts AOV | AOV | 18,400 | inconclusive, underpowered | stopped, not rerun |
```

- The `Decision` column is the reason the file exists: an inconclusive test that nobody recorded gets proposed again next quarter by someone who was not there.
- Record the pre-declared sample, not only the achieved one — that is what makes a peeked result visible later.

`promotions/<year>.md` — every promo with its realised, not planned, margin.

```markdown
# Promotions — 2026

| Dates | Mechanic | Scope | Redemptions | Revenue | CM% during | Baseline CM% | Verdict |
|-------|----------|-------|-------------|---------|------------|--------------|---------|
| 2026-06-13→16 | 20% code SUMMER | sitewide | 412 | 17,900 EUR | 31% | 44% | repeat, but exclude bundles |
```

`disputes/<year>.md` — chargebacks and their deadlines.

```markdown
# Disputes — 2026

| Opened | Respond by | Order | Amount | Reason | Evidence sent | Outcome |
|--------|-----------|-------|--------|--------|---------------|---------|
| 2026-07-11 | 2026-07-18 | 10442 | 89 EUR | product not received | delivery scan + AVS match + policy | won 2026-08-02 |
```

- `Respond by` is copied from the processor the day the dispute opens and becomes a `## Due` row the same turn. No customer name appears — the order number identifies it.
- Record losses with their reason: three losses for the same reason is a process fix, not bad luck.

`incidents/<year>.md` — anything that stopped or corrupted the money path.

```markdown
# Incidents — 2026

| Date | What broke | Detected by | Duration | Orders affected | Revenue impact | Root cause | Fix |
|------|-----------|-------------|----------|-----------------|----------------|-----------|-----|
| 2026-03-21 | oversold BAG-01 across channels | customer emails | 6 h | 38 | 340 EUR refunds + goodwill | 30-min sync, no buffer | buffer = 2× peak per interval |
```

- `Detected by` is the field that improves the store: "customer emails" appearing twice is an alerting gap, not an incident detail.
- Read this file before peak planning — last year's incidents are this year's checklist.

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings it had inside `memory.md`.

`metrics.md` — `## Metrics`, plus `## Definitions` copied from the tracking plan artifact once the store has its own wording. This is the file that makes a year-on-year comparison possible without re-querying anything.

`unit-economics.md` — `## Unit Economics`, plus `## Fee Stack` (the per-channel fees the CM rows depend on) so a fee change can be applied to every row at once.

`channels.md` — `## Channels`, plus `## Concentration` (share of revenue by channel, per month) — the early warning that one marketplace has become the business.

`wholesale-accounts.md` — `## Wholesale Accounts`, plus `## Credit Exposure` (account, limit, currently outstanding, oldest unpaid invoice date). Only exists in stores that sell B2B; the section is created in `memory.md` with these exact headings the first time an account is onboarded (`b2b.md`).

`suppliers.md` — `## Suppliers`, plus `## Price History` (supplier, date, change, affected SKUs). Price history is why this file exists: without it nobody can say whether margin fell because of freight, COGS, or discounting.
