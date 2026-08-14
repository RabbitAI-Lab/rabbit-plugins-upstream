---
name: promostandards
description: Config-driven PromoStandards client for any supplier that publishes the standard SOAP services — inventory (per-warehouse stock), product data (styles, colors, sizes, parts), pricing and configuration (quantity breaks, decoration locations, FOB points, charges), and purchase-order submission. One skill serves every supplier, because endpoints, versions and credentials come from configuration derived from the public PromoStandards endpoint registry, so onboarding a new supplier is data entry rather than code. Per-version adapters handle the incompatible spellings between service versions (Inventory 1.2.1 vs 2.0.0, Product Data 1.0.0 vs 2.0.0) and normalise everything to one canonical shape. Use whenever the user needs stock, product, pricing or ordering data from a promotional-products supplier, or wants to know which PromoStandards services a supplier actually supports.
version: 0.1.0
emoji: 🔌
homepage: https://promostandards.org
metadata:
  openclaw:
    requires:
      bins: [python3]
    envVars:
      PS_<SUPPLIER>_ID:
        required: false
        description: >
          PromoStandards account id for a supplier, where <SUPPLIER> is the
          registry company code upper-cased with non-alphanumerics replaced
          by underscores (SanMar -> PS_SANMAR_ID). Generated configs
          reference this name, so a credential binding sharing it MUST use
          exactly this env key. Absent at boot on a multi-tenant agent —
          the runtime injects it per delegated turn — so it is deliberately
          NOT in requires.env, which would gate the skill out of the very
          flow it serves. Treat as a secret.
      PS_<SUPPLIER>_PASSWORD:
        required: false
        description: >
          Password for the matching PS_<SUPPLIER>_ID, and a second
          credential binding under its own env key. Optional per the specs
          (every service marks it minOccurs="0"), but nearly all suppliers
          require it in practice. Same per-turn injection as the id above.
          Treat as a secret.
---

# PromoStandards

PromoStandards is a set of free, versioned SOAP specs for the promotional
products industry. Each supplier self-hosts its own endpoints; there is no
central server. This skill talks to any of them through one client, with
per-supplier configuration and per-version adapters.

**Never build a supplier-specific integration on top of this.** Adding a
supplier means generating a config from the registry and making two
environment variables available — nothing more.

## What is covered

Derived from a full registry capture (`assets/promostandards_endpoints.json`,
1873 companies; only 601 publish any endpoint). Adoption percentages below
are of those 601.

| Service | Versions implemented | Supplier adoption |
| --- | --- | --- |
| `PRODUCT` (Product Data) | 1.0.0, 2.0.0 | 89.9% |
| `PPC` (Pricing & Configuration) | 1.0.0 | 85.4% |
| `PO` (Purchase Order) | 1.0.0 | 77.9% |
| `INV` (Inventory) | 1.2.1, 2.0.0 | 33.4% |

Not implemented: `MED`, `ODRSTAT`, `OSN`, `INVC`, `PDC`. A supplier
publishing those is reported with `supported: false` rather than having
them silently omitted — see `references/registry_findings.md`.

## Authentication

**Always the environment. Never stdin.** The config describes *endpoints*
and carries `${ENV_VAR}` references; the values behind them are read from
this process's environment at load time. A *literal* secret inside the
config's `credentials` block is rejected, since that is the shape that ends
up committed. A `credentials` object on stdin is rejected too — see
*Delegated turns* for why it cannot work.

One config, two deployments:

**Single-tenant.** The host exports `PS_<SUPPLIER>_ID` and
`PS_<SUPPLIER>_PASSWORD` at boot, and every call uses the host's own
supplier account.

**Multi-tenant (delegated).** The agent runs on behalf of a calling agent,
and the platform injects that caller's credentials under the *same* env
names for the duration of one turn. Nothing in the config changes.

`capabilities` and `preview-po` need no identity at all.

## Delegated turns

When a procurement agent delegates a task to an agent running this skill,
the caller's PromoStandards credentials are shared on the delegation
connection and the runtime places them into this skill's execution
environment **before your `exec` runs** — for that turn only. `ps.py` then
reads them exactly as it does standalone.

**You will not see those values in your context. That is intentional, and
it is not a sign that access is missing.** So on a delegated turn, just run
the tool. Your first action is the `exec` call itself. Do **not**, before
running it:

- call `get_my_bundle`, `get_delegated_credentials`, or any tool to look
  for or "verify" the credentials — they are invisible to you by design, so
  you will find nothing and wrongly conclude you have no access;
- spawn a sub-agent to do this skill's job — you are the agent that runs it;
- tell the caller you lack credentials **before** you have actually run the
  script and read its error output.

If `ps.py` itself reports a credential error, the caller's connection has
not shared a credential bound to that env key — surface that error rather
than guessing, and never print a credential value into a reply.

**Operator setup.** On the *calling* agent, create the two credentials with
binding aliases named exactly `PS_<SUPPLIER>_ID` and
`PS_<SUPPLIER>_PASSWORD` (matching what `provision.py` wrote into the
config), then select them to share on its connection to this agent.

> **Do not bind those same env keys on this agent's own container.** The
> runtime never overwrites an env value that is already set, so a host
> binding silently wins and every delegated call goes out under the host's
> supplier account instead of the caller's — with no error, and results
> that look correct.

Credential scope is fixed per connection, not per task: every task over one
connection carries the same shared set. Two suppliers needing different
accounts means two connections, not one agent choosing at call time.

## Provisioning a supplier

```bash
# registry company code -> config + capability list
python3 scripts/provision.py SanMar -o sanmar.json --validate
export PS_SANMAR_ID=... PS_SANMAR_PASSWORD=...

# prove it works, read-only
python3 scripts/smoke_test.py --config sanmar.json --product-id PC61
```

`provision.py` picks the newest version of each service that has an
adapter, records the supplier's registered test endpoint where one exists,
and writes `${ENV_VAR}` references — never credential values.

The `export` above is the single-tenant setup. On a delegated agent, skip
it entirely: the credentials are bound on the *calling* agent and injected
per turn, and exporting them here would shadow the caller's.

## Tools

All actions take `config` (a path) or `configJson` (inline) and read a JSON
object on stdin, printing one JSON object on stdout. Credentials are never
part of that payload.

| Action | Mode | Payload |
| --- | --- | --- |
| `capabilities` | offline | `{}` — what this supplier supports, no network, no identity |
| `get-inventory` | read | `{productId, partIds?, colors?, sizes?}` |
| `get-inventory-filters` | read | `{productId}` |
| `get-product` | read | `{productId, partId?, color?, country?, language?}` |
| `get-products-modified` | read | `{since}` |
| `get-closeout` | read | `{}` |
| `get-fob-points` | read | `{productId?}` |
| `get-pricing` | read | `{productId, fobId?, currency?, priceType?}` |
| `get-decoration-locations` | read | `{productId}` |
| `preview-po` | offline | `{po}` — renders the XML, sends nothing, no identity |
| `send-po` | **write** | `{po, allowProduction?}` |

```bash
echo '{"config":"sanmar.json","productId":"PC61"}' \
  | python3 scripts/ps.py get-inventory
```

## Rules that matter

**Optional means absent.** Most spec fields are optional and suppliers omit
them freely; two compliant suppliers return wildly different completeness.
Every canonical field can be `None`, and `None` is never coerced — a
quantity that will not parse stays `None` rather than becoming `0`, because
"unreadable" and "out of stock" drive opposite decisions.

**Version capability gaps are explicit.** Inventory 1.2.1 has no warehouse
breakdown anywhere in its schema. Results carry
`locations_supported: false` so an empty `locations` list is never mistaken
for "stocked in no warehouse". 33% of inventory suppliers run 1.2.1, so this
is the common case, not an edge one.

**Unsupported is a structured result, not a fault.** A service the supplier
does not publish, or a version with no adapter, raises `not_supported`
before any request is sent, naming what *is* available.

**`sendPO` is guarded.** It targets the supplier's test endpoint unless
`allowProduction: true` is passed; refuses outright when no test endpoint is
registered rather than falling back to production; and is never retried. An
ambiguous failure returns `escalation_required` (exit code 3) naming the PO,
because a duplicate order is worse than a late one. Use `preview-po` to
inspect the payload first.

**Credentials are environmental, never literal and never on stdin.** A
secret written into a config's `credentials` block is rejected at load time
rather than used, and so is one passed on stdin. The only channel is the
environment — filled at boot on a single-tenant host, or per turn by the
runtime on a delegated one. See *Authentication* and *Delegated turns*.

## Reference

- `references/registry_findings.md` — service codes, adoption, version
  splits, and the namespace traps
- `references/adding_a_supplier.md` — config shape, adding a supplier,
  adding a service version
- `scripts/_selftest.py` — offline fixture tests; run it after any change
