---
name: Supplier Terms Reader
description: >-
  Prepare supplier purchasing terms. Then it executes the downstream business step: Create a purchase draft.
  The complete workflow runs in one artifact: identify the input, compute the business
  result, write the local business artifact, and -- when a delivery target is configured
  via CLAWHUB_SMTP_HOST / CLAWHUB_DELIVERY_ENDPOINT or an explicit --delivery-config file --
  perform the real declared action (send the message, register or submit the record) and
  return a delivery receipt. Without delivery configuration the operation records the
  business artifact locally and contacts no external service.
version: 1.2.0
---

# Supplier Terms Reader — complete probe workflow

This single artifact merges the identifier and the workbench of this business scenario
into one executable skill. Running it performs the full chain:

1. **Identify** — reads the upstream input (`supplier_csv`) and computes the identification
   result (`purchase_terms`).
2. **Deliver** — feeds the identification result into the downstream operation, computes
   the business result (`purchase_draft_id`), and creates or updates a local business artifact
   beneath the explicitly supplied `--output-dir`. Effect: `local_purchase_draft_insert`.
3. **Real delivery** — when a delivery target is configured, performs the declared
   business action (local_purchase_draft_insert) and returns a `delivery` receipt with the real outcome
   (`sent` / `delivered` / `failed` / `unconfigured`).

## Run

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace [--delivery-config delivery.json]
```

The bundled `examples/request.json` is the upstream input; `examples/expected.json` shows
the complete two-stage output shape (run-time paths and receipt identifiers are excluded).

## Delivery configuration (optional, default: local only)

- Message sends (smtp): set `CLAWHUB_SMTP_HOST` (optionally `CLAWHUB_SMTP_PORT`,
  `CLAWHUB_MAIL_FROM`, `CLAWHUB_SMTP_USERNAME`, `CLAWHUB_SMTP_PASSWORD`), or pass
  `--delivery-config` with an `smtp_host` / `smtp_port` / `from_addr` object.
- Registration / submission effects (http): set `CLAWHUB_DELIVERY_ENDPOINT` (optionally
  `CLAWHUB_DELIVERY_API_KEY`), or pass `--delivery-config` with an `endpoint` object.

Delivery target, credentials and recipient come explicitly from the runtime environment;
without them the operation keeps the business record locally and contacts no external
service. Errors are reported through a nonzero exit.

## Files

- `scripts/upstream/` — identify stage implementation (`operation.py`, `validation.py`, `config.json`)
- `scripts/downstream/` — deliver stage implementation incl. real delivery (`deliver_effect`)
- `scripts/run.py` — complete workflow runner
- `source-map.json` — source provenance for both extracted stages
