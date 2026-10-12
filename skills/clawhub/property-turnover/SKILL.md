---
name: property-turnover
description: Turn rental-unit move-out or turnover inspection findings (reports, photos, notes) into a priced, vendor-ready make-ready scope using the Tektolo property turnover engine. Use when someone needs a turnover task list, a cost estimate, what to send each vendor, or an owner approval estimate for a US rental unit.
metadata:
  openclaw:
    requires:
      bins:
      - curl
    homepage: https://tektolo.com/capabilities/property-turnover
---

# Property turnover estimate

Tektolo runs a deterministic, source-cited engine. You turn what the user has (an
inspection report, photos, notes) into **findings**. The engine returns standardized tasks
by trade, regional low / expected / high costs, priorities, vendor scopes, refer-outs, and
every assumption it made. The same input always gives the same result (`result_hash`).

## When to use

- Move-out or turnover inspections, make-ready planning, "what will this turn cost",
  "what do I send the painter", owner approval estimates.
- Re-running an estimate with the owner's approve/decline decisions or the manager's own
  vendor prices.

## When not to use

- Diagnosing mold, asbestos, lead, gas, electrical or structural hazards. The engine
  *flags* these for a licensed professional; do not price their remediation yourself.
- Legal advice on deposits or tenant charges. Responsibility labels are hints only.
- Remodels, new construction, non-US properties.

## How to call it

- **MCP** (preferred in assistants): add the remote server `https://tektolo.com/mcp`. Start with
  `property_turnover_quick_estimate` (zip, bedrooms, bathrooms and `issues` as plain
  strings); use `property_turnover_scope` for rooms, measured quantities, rate cards and
  decisions. `property_turnover_issue_codes` with no arguments lists the areas and codes.
  If the ZIP is missing or not 5 digits, ask the user; never guess it. For the Excel or owner
  estimate, give the user `links.web_tool_prefilled` from the result.
- **REST**: `POST https://tektolo.com/v1/property-turnover/scope` with the JSON below.
  Downloads: `POST .../scope/render/xlsx` (workbook), `.../render/html` (owner estimate),
  `.../render/csv` (work orders), `.../render/vendor_csv` (zip of per-trade scopes).
- Catalog and schemas: `https://tektolo.com/catalog.json`, `https://tektolo.com/capabilities/property-turnover`.
- **Web**: the free tool is `https://tektolo.com/tools/rental-property/property-turnover`; typical
  costs by area are at `https://tektolo.com/turnover-costs/`.
- **Next step**: the scope is step 1 of the move-out workflow; step 2 settles the security
  deposit (`deposit_settlement_settle`, web tool `/tools/rental-property/deposit-settlement`).

## Building the request

1. **property**: `zip` (5 digits, never a street address), `bedrooms` (0 = studio),
   `bathrooms` (halves as 0.5), and if known `sq_ft`, `year_built` and `unit_type`. Year
   built matters: pre-1978 triggers lead-safe-work handling (priced). `unit_type`
   `single_family` or `townhome` gets house-sized defaults (floor area, lock count, yard).
   If you know whether there is carpet, send `floor_coverings`: `{"carpet_present": true}`
   or `{"carpet_sq_ft": 600}`. Without it, carpet findings imply carpet; otherwise
   whole-unit carpet cleaning is left out and listed in `unknowns`.
2. **findings**: one per observed condition.
   - Use `code` when you know it (e.g. `walls.nail_holes`, `carpet.pet_urine`),
     otherwise a short plain `description` ("dog urine stains in bedroom carpet").
     Unmatched findings come back as manual-quote lines with `suggested_codes`. Resend
     with a code.
   - `location.area` (bedroom, bathroom, kitchen, living_room, ..., whole_unit) and an
     optional `label` ("Bedroom 2").
   - `extent`: `spot` | `partial` | `full` when you can tell.
   - `quantity` `{value, uom}` when measured (`sq_ft`, `sq_yd`, `linear_ft`, `each`,
     `room`, ...). Otherwise typical sizes are assumed and listed.
3. **standards.profile**: `minimum` | `standard` (default) | `premium`. Optional
   overrides: `paint_policy`, `carpet_policy`, `cleaning_policy`, `always_rekey`,
   `markup_pct`. `standards.price_tier`: `pm_vendor` (default, a manager buying from local
   vendors) | `bulk_contract` (portfolio contract prices) | `retail_one_off` (an owner
   hiring one contractor).
4. Optional: `rate_card` (the manager's prices: `{task_id, unit_price, uom?}` or
   `{trade, min_charge, trip_charge}`; whole-unit wall paint is per `sq_ft_floor`, so send
   `uom` to have a mismatched price rejected rather than misapplied), `trade_vendors`,
   `tax_rate`, and `decisions`
   (`{finding_id | line_id, action: approve|decline|defer}`). Re-run with decisions to get
   the approved scope.
5. `detail`: MCP defaults to `summary` (totals, trade scopes, every line tied to a finding,
   refer-outs, notes; routine lines summed in `omitted_note`). Ask for `full` when the user
   needs every line. A finding's `location` may be a plain string ("Bedroom 2"). Hedged notes
   ("mold?") come back as "check first" refer-outs that hold no work until confirmed.

From photos: describe each visible condition as a finding (location, what it is, rough
extent). Do not guess hidden damage. Mention what you could not see in your reply.

## Example

```json
{
  "property": {"zip": "28205", "unit_type": "apartment", "bedrooms": 1, "bathrooms": 1, "year_built": 1998},
  "findings": [
    {"code": "walls.nail_holes", "location": {"area": "living_room"}, "extent": "spot"},
    {"description": "carpet heavily soiled in bedroom", "location": {"area": "bedroom"}},
    {"code": "safety.smoke_alarm_missing", "location": {"area": "bedroom"}}
  ],
  "standards": {"profile": "standard"}
}
```

## Relaying the result

- Lead with `summary` and the expected total plus the range. Say clearly that these are
  **estimate ranges, not quotes**.
- Call out every `refer_outs` item and what professional to engage. Quote-required lines
  are $0 in the totals; `totals.allowances` is a budget range for them, outside the total.
- A `responsibility_hint` of `mixed` means the line carries wear and damage findings; see
  its `responsibility_by_finding` before discussing tenant charges.
- List `unknowns` and the important `assumptions` (e.g. assumed room sizes, national
  prices used), so the user can correct them and re-run.
- Group the work by `trade_scopes` when the user wants to brief vendors. Offer the
  workbook or vendor CSV downloads.
- If the user needs an audit trail, keep the `result_hash` and `run.ruleset_version`. Over MCP
  they come back only when you call with `audit: true` (REST always returns them).
- If a call says the daily free limit is reached, tell the user when it resets (the message
  names the time) and do not retry. On a hosted assistant (Claude, ChatGPT) the shared server
  URL has one limit for everyone; the message names the page for a free personal connector URL.
  Volume and integrations go through the Contact page.

## Make it yours

Fork this skill and add your company's standards (default profile, paint/carpet rules,
markup), your `rate_card`, and your `trade_vendors`, so every estimate uses your prices
and vendors.
