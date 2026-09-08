# Web-image routine — per-color storefront thumbnails (blank + decoration)

This is the workflow the **Mockup Artist Agent** runs on its schedule for the
routine **"General Purpose Web image generation routine."** No user is watching
each run. The agent sweeps the storefront catalog for decorated products that
have no web image (or only one shared image across colors), generates a
per-color mockup (the product's decoration composited onto that color's blank),
and writes it back to the `product.template` / `product.product` image field.

The rendering is the same deterministic pipeline the interactive skill uses
(`compose_mockup.py` + the mandatory [self-review loop](self_review.md)). This
doc only wraps it in a catalog sweep plus the Odoo read/write plumbing. **Same
rules still apply:** no model-generated pixels, always self-review before
writing back.

> **Runtime note.** Every Odoo read/write below is a `drivethru_mcp` MCP tool
> call (`product_read`, `product_write`, `decoration_get_image`,
> `storefront_list_sites`, …). Call them as native tools. Images move as
> base64 through `product_write` / `decoration_get_image`, or as a plain URL
> when a CDN link is available (preferred — see [§6](#6-writing-the-web-image-back)).

## What the routine does on each fire

1. **Find the candidate products** (see [§1](#1-finding-the-candidate-products)).
2. **For each product, decide if it needs images** — no template image, or every
   color variant falls back to the same shared image (see
   [§2](#2-does-this-product-need-images)). Skip the rest.
3. **Resolve the two inputs** — the product's decoration graphic, and, per color,
   the matching blank image (see [§3](#3-resolving-decoration--per-color-blank)).
4. **Compose + self-review** one mockup per color (see [§4](#4-compose--self-review)).
5. **Write each mockup back** to the color's variant image (and the template's
   default image) (see [§6](#6-writing-the-web-image-back)).
6. **Log one outcome per product/color** plus a run summary (see
   [§7](#7-per-outcome-logging--run-summary)).

## 1. Finding the candidate products

Storefront (decorated) products are `product.template` records with
**`product_type = 'bacon_item'`**. Each one carries the two things a mockup
needs:

- **`blank_product_tmpl_id`** → the blank style `product.template` (its variants
  hold the per-color vendor product photos).
- **`linked_decorations`** → the `decoration` record ids (the graphics printed on
  the blank). `end_item_key` encodes the same thing, e.g. `b717:d358.367`
  (blank template 717, decorations 358 + 367).

**Preferred scope — draft storefront sites.** The intent is to image the stores
being built. When the `storefront_list_products` tool is available, walk the
draft sites and take their catalogue:

```jsonc
storefront_list_sites { "state": "draft" }        // → site ids
storefront_list_products { "site_id": <id> }      // → product_tmpl_id per catalogue line
```

**Fallback scope — direct `bacon_item` sweep (works with today's tools).** If
`storefront_list_products` is not deployed yet, sweep decorated products
directly and cap the queue:

```jsonc
product_read {
  "model": "product.template",
  "domain": [["product_type","=","bacon_item"], ["active","=",true]],
  "fields": ["id","name","blank_product_tmpl_id","linked_decorations",
             "attribute_line_ids","product_variant_ids","product_type"],
  "limit": 25
}
```

Either way, **cap the per-fire queue** (start at 10 products). Better to run
often than to blow a run on the long tail.

## 2. Does this product need images?

Read the template's image state without pulling full binaries — `image_128`
(the small thumbnail) is enough to test *presence*, and `image_url` is a cheap
CDN string. A product needs work when **either** is true:

- **No image at all** — template `image_1920` empty *and* `image_url` empty.
- **One shared image across colors** — no color variant has its own
  `image_variant_1920`, so every color falls back to the single template image.
  Check by reading the variants' `image_variant_1920` presence (via `image_128`
  on each `product.product`, or a targeted binary read). If none of the colours
  carry their own image and the product has more than one colour → it needs
  per-color images.

If the product already has a distinct image per color, **skip it**
(`skipped:already_imaged`). The routine is idempotent — never overwrite a good
per-color image.

## 3. Resolving decoration + per-color blank

**Decoration graphic.** Take the first entry in `linked_decorations` (or the
one named in `end_item_key`). Fetch its art:

```jsonc
decoration_get_image { "model": "decoration", "record_id": <deco_id>, "field": "image" }
```

It returns `data_base64` (save to a temp `.png`) or a `cdn_url` (GET it to a
temp file — keeps the base64 out of the token stream). Read the decoration's
`decoration_location` to choose a **placement** key (`full_front`, `left_chest`,
`full_back`, `back_yoke`, …); default to `full_front` and note it.

**Per-color blank.** For each colour on the decorated product (the `Color`
attribute values on its `attribute_line_ids`):

1. Find the blank template's variant with the **same colour name** —
   `blank_product_tmpl_id`'s `product.product` whose Color value matches (match
   by name, e.g. `default_code ilike "<color>"`, not by attribute-value id — the
   decorated product and the blank wrap the same colour under different
   `product.template.attribute.value` ids).
2. Take that blank variant's image. **Prefer a flat, no-model front:** a
   `vendor_image_url` / `image_url` that ends `_flat_front` (SanMar) or is a
   `colorFrontImage` (S&S). If the only image is a legacy on-model / low-res
   shot (`.../catalog/images/..._model_front.jpg`), the mockup will look wrong —
   record `skipped:blank_needs_flatfront` for that colour and move on. Fixing
   those blanks is the vendor-sync routine's job (prong 1), not this one.
3. GET the blank image URL to a temp file (or pull the variant's `image_1920`
   via `product_read include_binary` only if there is no URL).

**When an input is missing — skip that colour** with a reason
(`skipped:no_decoration`, `skipped:no_blank_for_color`). Unattended: never ask a
human, never guess.

## 4. Compose + self-review

Same as the interactive workflow. Pass the garment `--category` when the blank
is obviously a tee/hoodie/hat/etc.; otherwise omit it and let the `_defaults`
rules apply.

```bash
python3 scripts/compose_mockup.py \
    --blank /tmp/blank_<color>.jpg \
    --decoration /tmp/deco.png \
    --category <category-or-omit> \
    --placement <placement>
```

Then run the **[self-review loop](self_review.md)** — `Read` the rendered PNG,
judge the placement, layer corrective deltas (`--width-delta-pct`,
`--offset-x-pct`, `--offset-y-pct`, `--rotate-deg`), re-compose. **Hard cap at 3
attempts.** Never loop past 3, never ping-pong a delta's sign.

Use the background-removal / cleanup helpers only when the decoration obviously
needs it (a solid plate behind flat art, or degraded / AI-generated art) — same
rules as the SKILL's [Background removal](../SKILL.md#background-removal-flat-art-vs-photos)
and [Cleaning up degraded art](../SKILL.md#cleaning-up-degraded--ai-generated-art).
Skip them by default so a clean PNG doesn't take the scenic route.

## 5. Keep the web image web-sized

A storefront thumbnail is not a print file. Before uploading, **downscale the
reviewed PNG to a web size** (longest edge ~1000&ndash;1200 px) and save as JPEG
(quality ~85). This keeps the base64 out of a huge token payload **and** keeps
the Odoo DB from ballooning across thousands of variants. (The scale-proof
answer is to store a CDN link in `image_url` instead of a DB binary — see the
storage note in [§6](#6-writing-the-web-image-back).)

## 6. Writing the web image back — use the HTTP upload, NOT product_write

**Never write the image as a base64 argument** — not `product_write` with
`image_1920` in `values`, not `decoration_set_image`. A real web JPEG exceeds the
MCP tool-argument size cap and arrives **truncated**: Odoo stores a broken,
half-grey image. Send the bytes through the deterministic **multipart upload
route** instead (`POST <ODOO_MCP_URL>/upload`) — the file goes up as a *file
part* and the **server** base64-encodes it, byte-exact. Use
`scripts/upload_production_file.py` (it reads `ODOO_MCP_URL` / `ODOO_MCP_TOKEN`,
which must point at the environment you are writing to):

- **Template default** (and single-colour products):

  ```bash
  python3 scripts/upload_production_file.py \
      --model product.template --field image_1920 --record-id <tmpl_id> \
      --file /tmp/web_<color>.jpg
  ```

- **Per colour** → upload to the representative `product.product` variant of that
  colour (`image_variant_1920` is the per-variant field):

  ```bash
  python3 scripts/upload_production_file.py \
      --model product.product --field image_variant_1920 --record-id <variant_id> \
      --file /tmp/web_<color>.jpg
  ```

The script prints the server's JSON (`present`, `web_url`, `bytes_received`).
**Confirm `present` is true and `bytes_received` matches the file's byte size**
before logging `image_written` — that check is what catches a truncated write.
Odoo auto-generates `image_128/256/512/1024` from the stored binary.

> **Storage / DB-size note.** The storefront renders `product.template.image_url`
> (a CDN string) in preference to the DB `image_1920` binary. At volume, prefer
> uploading the web JPEG to the CDN and setting `image_url` (and the variant
> `image_url`) rather than storing binaries — it avoids ballooning the database.
> Until that CDN-write path is wired, `image_1920` is the working target for the
> first pass.

**Do not** advance any state, edit other fields, add chatter, or touch the
decoration/blank source records. This routine only writes the web image.

## 7. Per-outcome logging + run summary

Emit one outcome per product (and per colour where useful):

| Outcome | When |
|---|---|
| `image_written` | Compose + self-review passed and the write succeeded. |
| `skipped:already_imaged` | Product already has a distinct image per colour. |
| `skipped:no_decoration` | No usable `linked_decorations` graphic. |
| `skipped:no_blank_for_color` | No blank variant matched the colour. |
| `skipped:blank_needs_flatfront` | Only a legacy on-model/low-res blank exists (prong-1 dependency). |
| `failed:<reason>` | Compose/upload/HTTP error — put the real error in the outcome. |

Then a single run summary: `queue=<N>, written=<w>, skipped=<s>, failed=<f>`.
An empty queue is a `nothing_to_do` verdict — the desired steady state once the
catalogue is imaged.

## Rules specific to this routine

- **Idempotent.** Never overwrite an existing good per-color image. A second run
  either fills a gap or skips.
- **Unattended.** No `AskUserQuestion`. Ambiguity or a missing input → skip with
  a reason.
- **Bounded.** Cap the per-fire queue (start at 10 products); cap colours per
  product if a product is enormous.
- **Non-destructive.** Only the web-image binary (or `image_url`) is written.
  No state changes, no edits to blanks or decorations.
- **Eyes-on.** Even in batch mode, the self-review loop is required. A silent bad
  mockup is worse than a skip.
- **Good blanks first.** A mockup is only as good as its blank. If a colour's
  blank is still a legacy on-model/low-res shot, skip it — the vendor-sync
  routine replaces those with flat, no-model fronts.

## The routine (paste into the Mockup Artist Agent's Routines page)

- **Name:** `General Purpose Web image generation routine`
- **Schedule:** daily (or as configured)
- **Prompt:**

  ```
  Generate per-color storefront web images. Follow
  references/web_image_routine.md in the drivethru-graphic-artist skill.

  Scope: storefront (decorated) products — product.template with
  product_type='bacon_item'. Prefer products in draft storefront.site
  catalogues (storefront_list_sites state=draft → storefront_list_products);
  if that tool isn't available, sweep bacon_item templates directly. Cap the
  queue at 10 products per run.

  For each product that has no template image OR whose color variants all
  share one image: read its decoration (linked_decorations → decoration_get_image)
  and, per color, the matching blank image from blank_product_tmpl_id (prefer a
  flat, no-model front; skip the color if only a legacy on-model/low-res blank
  exists). Compose a mockup with compose_mockup.py, self-review up to 3 attempts,
  downscale to a ~1000px web JPEG. Write it back with the byte-exact multipart
  upload — scripts/upload_production_file.py — NOT product_write/base64 (that
  arrives truncated): --model product.product --field image_variant_1920
  --record-id <variant> for the color, and --model product.template --field
  image_1920 --record-id <tmpl> for the default. Confirm bytes_received matches
  the file size before logging image_written. Never overwrite a good per-color
  image, never advance state, never ask a human. Log one outcome per
  product/color (image_written / skipped:<reason> / failed:<reason>) plus a run
  summary.

  For testing, use the staging-2 Odoo MCP and start with a small queue. Note:
  upload_production_file.py posts to <ODOO_MCP_URL>/upload using ODOO_MCP_URL /
  ODOO_MCP_TOKEN, so those env vars must point at the same environment
  (staging-2) you are testing against.
  ```
