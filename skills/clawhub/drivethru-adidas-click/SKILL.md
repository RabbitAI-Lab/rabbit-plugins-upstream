---
name: drivethru-adidas-click
description: Browser-driven adidas Click B2B toolkit — places purchase orders and runs live inventory / wholesale-pricing checks on the adidas Click portal with Playwright, since adidas exposes no public ordering API. Ordering accepts style number, color, size, quantity, a purchase-order number, and a ship-to address, drives the cart/checkout, and (on confirm) submits the order. Checks reuse the same flow but never buy — inventory reads product pages (no cart), pricing fills a throwaway "DO NOT BUY" cart, reads the priced checkout, and deletes it. Use whenever the user needs to place/draft a PO on adidas Click, or check live stock levels or wholesale pricing.
version: 0.6.0
emoji: 👟
homepage: https://b2bportal.adidas-group.com
metadata:
  openclaw:
    requires:
      bins: [python3]
    envVars:
      ADIDAS_CLICK_USERNAME:
        required: false
        description: >
          adidas Click B2B portal username (typically an email). Optional —
          may instead be passed inline in a tool's stdin JSON. Treat as a secret.
      ADIDAS_CLICK_PASSWORD:
        required: false
        description: adidas Click portal password. Optional env cache; treat as a secret.
      ADIDAS_CLICK_BASE_URL:
        required: false
        description: >
          Override for the adidas Click base URL. Defaults to
          `https://b2bportal.adidas-group.com`. Set this if the account uses a
          region-specific host.
      ADIDAS_CLICK_HEADLESS:
        required: false
        description: >
          Force headless when set to a truthy value (`true`/`1`/`yes`/`on`).
          Default is HEADED, because adidas's Akamai Bot Manager stalls headless
          Chromium. On Windows/macOS a headed browser uses the native display, so
          nothing extra is needed. Only on a **Linux** host with no display server
          (e.g. a headless container) does the skill auto-start an Xvfb virtual
          display (requiring the `xvfb` system package); Windows/macOS never need
          it. Headless will most likely time out at the adidas login page.
      ADIDAS_CLICK_USER_AGENT:
        required: false
        description: >
          Override the browser User-Agent. Defaults to a current desktop-Chrome
          UA so adidas's Akamai edge serves the automated browser instead of
          stalling the response. Only change it if the default UA gets blocked.
    install:
      uv:
        # Browser automation is the only surface. This installs the Playwright
        # *package*; the Chromium *binary* (a separate ~150 MB download that pip
        # can't fetch, and OpenClaw has no post-install hook for) is installed
        # automatically on the first run — see the browser-binary note below.
        - playwright>=1.40
---

# adidas Click B2B toolkit

adidas Click is a **B2B ordering portal with no public API**, so this skill
places purchase orders by driving the portal with **Playwright**. Every tool is
reached through one CLI entrypoint:

```bash
echo '<json-args>' | python3 scripts/adidas.py <action>
```

The action is the **first CLI argument**; arguments are a JSON object on
**stdin**. Each call prints a single JSON object on stdout, or
`{"error": {"type": ..., "message": ...}}` with a non-zero exit code on failure.

Playwright is imported lazily, so the skill loads without it. The Playwright
**package** is a declared `uv` dependency; its Chromium **browser binary** (a
separate ~150 MB download that pip/uv doesn't fetch, and for which OpenClaw has
no install-time hook) is **installed automatically on the first run** if missing
— so no manual `python -m playwright install chromium` is needed. That first run
therefore includes a one-time browser download. If the auto-install fails (e.g.
no network, or missing system libraries), the tool returns a clear
`config_error` pointing at the manual command.

> **Build status — full order flow implemented.** The skill drives a purchase
> order end to end: login → add line quantities to the active cart → checkout
> (Customer PO, delivery location — default / saved / one-time dropship — and
> shipping method) → Next → **Calc. Net Price** (waits for the "Done!" tell so
> the wholesale discount always applies) → **Order Now** → confirmation number
> parsed from the redirect URL. `confirm: false` is a full dry run; `confirm:
> true` **places a real order** (no sandbox). The assembled flow has been built
> and unit-checked selector-by-selector but not yet run against the live site in
> one pass — watch the first real end-to-end run. See
> [`references/order_flow_notes.md`](references/order_flow_notes.md) for the step
> map and captured selectors.
>
> **Inventory / pricing checks (`check-inventory-pricing`)** reuse the same
> captured steps — product navigation + size read (inventory) and, for pricing,
> the throwaway-cart → checkout → **Calc. Net Price** walk — but stop before
> **Order Now** and delete the cart. No new selectors: it composes the existing,
> live-validated ordering steps, so its browser surface rides on the same
> capture. See the "Inventory & pricing checks" section below.

## When to use this skill

Reach for `create-purchase-order` when the request involves placing (or
drafting) a purchase order on **adidas Click**: given a style number, color,
size, quantity, a PO number, and a ship-to address, put the order into the
portal cart/checkout and — on explicit confirmation — submit it.

Reach for `check-inventory-pricing` when the request is to look up **live stock
levels** and/or **wholesale (net) pricing** on adidas Click **without buying
anything** — e.g. *"how much JW4306 is in stock in L?"* or *"what's our
wholesale cost on 24× JW4306 M?"*. It reuses the ordering flow but never places
an order (see below).

Do **not** use it for other footwear/apparel vendors, and never invent portal
selectors from prose — the flow lives in the captured
[`references/order_flow_notes.md`](references/order_flow_notes.md).

## Actions

| Action | Risk | stdin JSON (key fields) |
| --- | --- | --- |
| `create-purchase-order` | **high — portal write (browser)** | `{purchase_order: {po_number, lines: [{style, size, quantity}], ship_to?, delivery_location_id?, ship_method?, on_insufficient_stock?, spread_delivery?}, confirm}` |
| `check-inventory-pricing` | **medium — read-only intent, but a pricing check briefly creates then deletes a throwaway cart (browser)** | `{check: "inventory"\|"pricing"\|"both", lines: [{style, size?, quantity?}], po_number?}` |

Run `python3 scripts/adidas.py` with no action to print the action list.

### `create-purchase-order` input

The order can be passed nested under `purchase_order` or as top-level fields:

```json
{
  "purchase_order": {
    "po_number": "PO-12345",
    "lines": [
      {"style": "JW4306", "size": "M", "quantity": 24},
      {"style": "JW4306", "size": "L", "quantity": 12}
    ],
    "ship_to": null,
    "delivery_location_id": null,
    "ship_method": null,
    "spread_delivery": false,
    "notes": null
  },
  "confirm": false
}
```

Each line is `{style, size, quantity}`. **`color` is optional** — adidas article
numbers encode the color (e.g. `JW4306` = the black colorway), so navigating to
the article lands on the right color with no picker.

Delivery location precedence: `delivery_location_id` (pick a saved location) >
`ship_to` (add a one-time / dropship location) > default (leave the cart's
preset). A one-time `ship_to.state` accepts a 2-letter abbreviation or the full
name. `ship_method` is left at the cart default unless set, and accepts a FedEx
service code (`FDGP`, `FEDE`, `FED4`, …) or its exact label ("FedEx Ground").
`po_number` is capped at **18 characters** and may contain only letters, numbers,
space, and `/ _ . ? &`; any other character (e.g. a hyphen) is auto-replaced with
`_` and the substitution is reported in the result's `warnings`.

By default (`new_cart: true`) the run **creates its own fresh cart** (named with
the PO) right after login and makes it active, so on a shared account it never
adds to — or checks out — a teammate's cart. If a cart with the same PO name
already exists (e.g. a leftover from an errored prior run) it is **deleted
first** so the run never piles onto stale quantities — only carts with that exact
PO name are removed, and any deletion is noted in `warnings`. Pass
`new_cart: false` to use the current active cart instead.

Pass `screenshot_path` to capture the filled page for review.

## Out-of-stock handling (read this)

Before entering quantities, the tool reads each size's availability (scrolling
the horizontal size row as needed to load off-screen sizes). A size is either
**backorderable** (stock below the requested quantity, incl. `0` with a restock
date) or **not available** (the "X" cell — will never be restocked, cannot be
ordered at all; it can only be removed or substituted). When a line's **full
quantity is not available**, behavior depends on `on_insufficient_stock`:

- **`pause`** (default) — **nothing is ordered** (even with `confirm: true`). The
  result comes back `status: "needs_confirmation"` with an `out_of_stock` list
  (`{style, size, requested, available}`) and a `message`. The agent must **stop
  and confirm with the user**, then re-run.
- **`order`** — order the short line(s) anyway, accepting **delayed delivery**
  (adidas spreads the backordered portion over future dates).
- **`skip`** — **remove** the out-of-stock line(s) and order the rest.

**Agent guidance:** if the user's request pre-authorizes a choice, set the flag
and skip the pause — e.g. *"go ahead and order anything out of stock"* →
`on_insufficient_stock: "order"`; *"remove any out-of-stock items without
asking"* → `on_insufficient_stock: "skip"`. Otherwise leave it at `pause`; on a
`needs_confirmation` result, **message the user** with the `out_of_stock` details
and the three choices, wait for their answer, then resume:

1. Order them anyway (delayed delivery) → re-run with `on_insufficient_stock: "order"`.
2. Don't order them → re-run with `on_insufficient_stock: "skip"`.
3. **Substitute** (e.g. a different size/style so items match) → edit the
   `lines` accordingly and re-run (optionally with a policy for any still-short
   substitutes).

`spread_delivery` is the lower-level knob behind `order`: on a per-line spread
prompt, `false` (default) declines (single delivery), `true` accepts.

The result reports `total_quantity` (summed pieces, on dry runs too) and, on a
placed order (`confirm: true`), each line's net `line_total` and `unit_price`
(net ÷ quantity) plus the order `order_total` (net wholesale), read from the
priced review page.

## Inventory & pricing checks (`check-inventory-pricing`)

A **read-only lookup** that reuses the ordering flow but **never places an
order**. Pick the mode with `check`:

| `check` | What it does | Cart? |
| --- | --- | --- |
| `inventory` | Reads each line's live size-tile stock level straight off the product page. | **No cart created** — inventory needs no add-to-cart. |
| `pricing` | Fills a **throwaway cart**, advances to the priced checkout screen (the *only* place wholesale net pricing shows), runs **Calc. Net Price**, reads the net unit/line prices + order total, then **deletes the cart**. | Yes — created, priced, deleted. |
| `both` (default) | `pricing` plus the inventory levels read while filling the cart. | Yes — same as `pricing`. |

```json
{
  "check": "both",
  "lines": [
    {"style": "JW4306", "size": "M", "quantity": 24},
    {"style": "JW4306", "size": "L"}
  ]
}
```

Each line is `{style, size?, quantity?}`:

- **`size` optional (inventory only):** omit it (or pass `"*"` / `"all"`) to
  report **every** size of that style. For a pricing line a specific `size` is
  needed (a price is per size).
- **`quantity` optional:** defaults to `1`. It only affects a **pricing** line's
  *line total* (unit price is the same regardless); an inventory read reports the
  raw level independent of quantity.

**Why a cart at all for pricing?** adidas only reveals the discounted **wholesale
net price** on the final checkout screen, after **Calc. Net Price** runs — there
is no price API and no price on the product page beyond a "from" figure. So a
pricing check has to fill the cart and walk to that screen, exactly like an
order, then stop before **Order Now** and delete the cart.

**The "DO NOT BUY" marker.** A pricing check names its throwaway cart **and** the
Customer PO with a `DO NOT BUY {random}` marker (e.g. `DO NOT BUY 7F3K9`) so that
if a run dies mid-flight, the leftover cart is unmistakably safe. The full
*"AUTOMATED CHECK - DO NOT PURCHASE - …"* wording does **not fit**: adidas hard-
caps the Customer PO at **18 characters** and allows only letters, numbers,
space, and `/ _ . ? &`, so this is the clearest imperative that still leaves room
for a 5-char random suffix (cart names must be unique). Override the marker with
`po_number` (still ≤18 chars, same charset).

**Never pauses on stock.** Because a check never buys and deletes its cart, it
does not stop on short/out-of-stock lines: a `pause` policy is upgraded to
`order` so every orderable line still gets priced. Sizes that are flatly *not
available* (the portal's "X" cell) are reported with no price.

**Result** (`status: "checked"`): a `lines` list of
`{style, size, color, requested_quantity, available, available_count, status
("in_stock"|"backorder"|"unavailable"), in_stock, unit_price, line_total, note}`,
plus `order_total` (summed net, pricing only), `total_quantity`, `po_number` (the
marker used, `null` for inventory-only), and `cart_deleted` (`true`/`false` once a
pricing check tried to remove its cart; `null` when no cart was made). If the
throwaway cart could not be auto-deleted (e.g. it was the account's only cart), a
`warning` says so and names it — remove it in the portal.

## Credentials

The adidas Click portal login can be supplied three ways (**later wins**):

1. **Environment variables** (preferred for a deployed agent):

   ```bash
   ADIDAS_CLICK_USERNAME=...
   ADIDAS_CLICK_PASSWORD=...
   ADIDAS_CLICK_BASE_URL=https://b2bportal.adidas-group.com   # override for region host
   ```

2. **Inline in the stdin JSON** — pass `username`, `password`, and `base_url`
   alongside the tool's own arguments.

3. **CLI flags** — `--username` / `--password` / `--base-url` after the action.
   Handy for local runs with no env vars and no secrets in the order JSON:

   ```bash
   echo '{"purchase_order": {...}, "confirm": false}' \
     | python3 scripts/adidas.py create-purchase-order --username "$U" --password "$P"
   ```

   > Command-line arguments are visible to other processes (`ps`) and your shell
   > history — for sensitive/automated use, prefer env vars or the stdin JSON.

If no credentials are present via any of these, the tool exits with
`{"error": {"type": "config_error", ...}}` (exit code 2) — treat that as a
signal to ask the user for the missing fields. Never guess or reuse credentials
across accounts, or paste secrets the user did not provide.

## Write safety

`create-purchase-order` is the only order-placing action.

- It requires `"confirm": true` to place the order. Without it, it logs in,
  fills the cart + checkout, and returns a **dry-run** preview **without
  submitting**. Confirm with the user before placing.
- Placing an order on adidas Click is a **real purchase** — there is no
  sandbox. Only run `confirm: true` for an order the user actually intends to
  place.

`check-inventory-pricing` **never places an order** — there is no `confirm`
path. `inventory` mode touches no cart at all. `pricing`/`both` create a
throwaway `DO NOT BUY …` cart only to reach the priced checkout screen, stop
**before** Order Now, and **delete the cart** on the way out. It does mutate
portal state briefly (the cart is created and removed), so it is not purely
read-only, but it cannot buy anything.

## Reachability & bot mitigation

adidas Click sits behind **Akamai Bot Manager**, which fingerprints the client
and *stalls the HTTP response* (rather than cleanly refusing it) for traffic
that looks automated. The tell is a navigation that hangs to a timeout
(`Page.goto: Timeout … exceeded`) even though the network path is healthy — a
browser-UA `curl` to the same host returns `200` in well under a second, while
a bare `curl` or a default headless Chromium (UA contains `HeadlessChrome`,
`navigator.webdriver=true`) gets tarpitted.

A spoofed User-Agent alone is **not** enough: a headless Chromium is still
fingerprinted (TLS/JA3, `HeadlessChrome` internals, no GPU/canvas) and tarpitted
even with a real UA. The reliable path is a **headed** browser on a **virtual
display**, which presents an ordinary browser fingerprint. So the skill:

- runs **headed by default** (set `ADIDAS_CLICK_HEADLESS=true` to force headless,
  which will most likely time out at the login page);
- launches Chromium with a real desktop-Chrome User-Agent, a normal
  viewport/locale, `--disable-blink-features=AutomationControlled`, a
  `navigator.webdriver` mask, and a longer navigation timeout;
- when headed on a **Linux** host with no display server, **auto-starts an Xvfb
  virtual display** (spawned directly, so no `xauth` needed) and points
  `$DISPLAY` at it — this requires the **`xvfb` system package** in the image
  (`apt-get install -y xvfb`). This is Linux-only: the skill first checks the
  platform, so on **Windows/macOS** (native GUI) and on a Linux host that already
  has an X11/Wayland display, it launches headed directly and **never requires
  Xvfb**.

Overrides: `ADIDAS_CLICK_USER_AGENT` if the default UA ages out. If headed on a
virtual display *still* stalls, the block is at the **egress IP** (a datacenter
IP Akamai distrusts) — route through an IP adidas allowlists, the same way
`drivethru-sanmar` documents needing its caller IP allowlisted. No browser/code
change fixes an IP-reputation block.

## Error model

Failures print `{"error": {...}}` and exit non-zero:

- `config_error` (exit 2) — missing/invalid credentials or an un-captured step.
- `api_error` — the portal rejected an action or a page did not match
  expectations. Includes `surface`, `operation`, `retryable`.
- `connection_error` — network / browser-launch / navigation failure
  (`retryable: true`).
- `validation_error` — bad input JSON or a missing required field.
- `usage` / `unknown_action` (exit 2) — bad CLI invocation; the message lists
  the valid `actions`.

Surface the human-readable `message` to the user. Do not retry on
`config_error` or `validation_error`.

## References

- [`references/order_flow_notes.md`](references/order_flow_notes.md) — the
  reverse-engineered portal ordering flow (step map, captured selectors, and the
  capture checklist for the next step). **Start here to continue the build.**
