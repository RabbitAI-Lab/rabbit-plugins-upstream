# dhl-tracking

Read-only DHL parcel tracking. Tracks one or more shipments by polling the public DHL tracking endpoint and reporting changes.

## What it does

- Maintains a list of tracked shipments in `store.json`
- Re-queries DHL on demand via `refresh`
- Reports only status changes (status, date, progress)
- Translates DHL's English status strings to the configured locale (de, en)

## What it does NOT do

- Read mail of any kind (no IMAP, no Nextcloud, no Gmail)
- Execute external provider scripts
- Log in to any service
- Modify anything on DHL's side (no "Wunschtag", no Zustelländerung, no login)

## Usage

```powershell
powershell -File <skill-root>\bin\dhl-track.ps1 <command> [flags]
```

Commands:

- `setup` — interactive configuration (notifyOn, locale, country)
- `setup show` — print current configuration as JSON
- `add <piececode> [--plz <nr>] [--description "..."] [--international]` — add a shipment
- `refresh` — re-query all shipments, report changes
- `show` — list all shipments with current status
- `remove <piececode>` — remove a shipment
- `doctor` — diagnostics (endpoint reachability, JSON validity, invariants)
- `test` — sanity test that does not hit DHL

Flags:

- `--plz <nr>` — postal/ZIP code (required for national, optional with `--international`)
- `--description "<text>"` — friendly label for the shipment (default: shipper name from DHL)
- `--international` — mark as international shipment (no PLZ required)

## Setup

On first `add`, `setup` runs automatically if no `setup.json` exists. It asks:

1. **notifyOn** (when you want to be notified about status changes):
   - `user_message` — on every user message (live)
   - `daily_digest` — only in the 21:00 daily digest
   - `heartbeat` — 3-4x/day via heartbeat cron
   - `silent` — no notifications, you run `refresh` manually
2. **country** (ISO-2): DE, AT, CH, GB, US, NL, FR, IT, ES, PL, BE, CA, AU. Default: DE.

`notifyOn` defaults to `silent` (no auto-refresh).

`setup.json` is stored in the skill root (or your `baseDir` if you set one). You can edit it directly or run `setup` again.

## Configuration / State

- `store.json` — list of shipments + last cached status
- `setup.json` — notifyOn, locale, country, baseDir
- `bin/dhl-countries.json` — country-code → DHL host map (DE, AT, CH, GB, US, NL, FR, IT, ES, PL, BE, CA, AU)
- `bin/locales/` — `de.json`, `en.json`, `dhl-status.{de,en}.json` for CLI strings and status translations

All paths are in the skill root by default. Set `baseDir` in `setup.json` to relocate state files.

## Lessons

- **Endpoint:** `POST https://<host>/int-verfolgen/data/shipment` (Body JSON, host from `bin/dhl-countries.json`).
- **PLZ required** for national DE shipments (5-digit). For international or other countries, see `dhl-countries.json` for the `zip_format` regex, or pass `--international`.
- **Accept-Header** must be `application/json`, else 406.
- **Origin/Referer** are not strictly required for the POST, but DHL's web routing can reject with 403/406 without them. The skill does not send Origin/Referer — it relies on the public POST endpoint being open.
- **Storage-based-Status:** when the recipient has chosen a preferred delivery day, the status reads "Storage based on requested delivery day (order by the recipient)" — **not** "In Zustellung". Storage at the depot ≠ out for delivery.
- **Encoding (Windows):** PowerShell's default console codepage is cp437/cp1252 and `[Console]::OutputEncoding = UTF8` does not always apply under `powershell -File`. On Linux/macOS or in IDE terminals with UTF-8, this is a non-issue. The skill always reads/writes JSON as UTF-8, so stored data is correct even if the terminal output looks like mojibake.

## Privacy

Outbound traffic per `refresh`/`add`:

- The configured DHL host (e.g. `www.dhl.de`)
- POST body: `piececode` (tracking number) and either `zip` (postal code) or `international: true`
- `User-Agent: dhl-tracking-skill/1.1`

DHL stores nothing about the requester (no cookies, no auth). The skill does not send any other data anywhere.

## What the skill does NOT promise

- It does not guarantee that DHL will accept every request format forever. If DHL changes their public endpoint, `doctor` will report the change in status code and the `refresh` output will surface the error.
- It is not affiliated with DHL. The endpoint is public but undocumented; use at your own discretion.

## Bezug zu anderen Skills

None. This skill is self-contained.