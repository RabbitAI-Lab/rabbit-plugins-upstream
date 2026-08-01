# Catalog — Product Data That Every Channel Reads

The catalog is one data model consumed by five audiences: the storefront, site search, product feeds, marketplaces, and the warehouse. **Model an attribute once, in a structured field, and let every audience read it.** An attribute that lives only in the description text is invisible to filters, feeds and marketplaces — which is where most of a catalog's revenue is decided.

**Before restructuring anything**, read `## Unit Economics` in `~/Clawic/data/ecommerce/memory.md` — SKU-level margin decides which products deserve the photography, the copy and the feed attributes, and which should be discontinued instead of improved.

## The Product Data Model

| Level | What it is | Rule |
|---|---|---|
| Product | The thing a customer shops for | One product page per buying decision, not per variant |
| Variant | A purchasable combination (size, colour, capacity) | One SKU per variant, always — a variant without its own SKU cannot be counted, picked, or reordered |
| SKU | The internal identifier | Stable for the life of the item; never reused after discontinuation, never encodes price or supplier |
| GTIN/EAN/UPC | The global identifier | Required by marketplaces and shopping feeds; missing GTINs suppress ads before they suppress rankings |
| Bundle / kit | Sold as one, picked as several | Component-level stock, bundle-level price; a bundle with its own stock number oversells the day the component sells out (`inventory.md`) |

- **SKU scheme**: readable and sortable, e.g. `CAT-MODEL-SIZE-COLOR`. Encode only what never changes. A scheme that encodes the season or the supplier breaks the first time either changes and leaves you renaming inventory that is already on shelves.
- **Options vs attributes**: options change what you ship (size, colour); attributes describe it (material, weight, fit). Options generate SKUs; attributes generate filters and feed fields. Putting an attribute in the option list multiplies your SKU count for nothing.
- **Discontinuation is a state, not a deletion.** Deleting a product 404s a ranking URL and orphans order history; set it out-of-stock-permanent, keep the page, and either redirect it or offer replacements (`storefront.md`).

## Fields Nobody Fills Until It Costs Them

Each of these blocks a channel or a decision downstream:

| Field | Blocked without it |
|---|---|
| Weight and dimensions (packed, not product) | Every accurate shipping rate, every 3PL quote, every marketplace fee estimate |
| GTIN / brand / MPN | Google Shopping and marketplace listings; feeds get disapproved, not degraded |
| Country of origin and HS/tariff code | Customs paperwork and duty estimates on any cross-border order (`tax.md`) |
| Tax class per product | Reduced-rate categories (books, food, children's clothing in some markets) charged at standard rate — refundable to the customer, not to you |
| Hazard/regulatory flags (battery, aerosol, liquid) | Legal carriage; the carrier discovers it at the depot, not at booking |
| Cost (COGS) per variant | Margin on every report; a catalog without cost cannot answer whether the promo worked |
| Supplier and lead time | Reorder points and stockout prevention (`inventory.md`) |
| Canonical image and alt text | Feeds, marketplaces, accessibility, and image search |

## Product Content That Sells

- **The first 60-70 characters of the title do the work** in feeds, search results and marketplace listings. Format: brand + product + defining attribute + variant. The same title should be legible with the tail cut off.
- Structure the description for two readers: a scannable block of specifications for the buyer who already decided, and a short benefit paragraph for the one who has not. Photography answers more objections than either.
- **Images**: main image on plain background (a marketplace requirement and a conversion aid), then scale reference, then in-use, then detail, then what is in the box. Missing scale reference is the most common cause of size-related returns (`returns.md`).
- Every claim that appears in the copy must be defensible: comparative claims, health or environmental claims, and "was" prices are regulated in most markets (`tax.md`).
- Duplicate manufacturer descriptions across resellers means the store competes on price alone in search results. Rewriting descriptions for the top-margin 20% of SKUs is usually the highest-return content work in the catalog.

## Taxonomy, Collections and Filters

- Collections exist for **navigation and landing pages**; tags exist for **filtering and automation**. Mixing them produces a tag list nobody can maintain and a menu nobody can navigate.
- Filters come from structured attributes only. Every filter must map to a field that exists on every product in the collection, or the filter hides valid products — a silent revenue leak nobody reports.
- **Faceted URLs need canonical rules** before they get indexed: filter combinations generate near-infinite URLs, and crawl budget spent there is crawl budget not spent on products (`storefront.md`, `acquisition.md`).
- One product in many collections is fine; one product with two URLs is not. Pick a canonical path and keep it stable across replatforms (`platforms.md`).

## Feeds and Syndication

The feed is the catalog seen by advertising and marketplace systems. It is generated, never hand-maintained.

- Required-attribute failures disapprove items silently: `gtin`, `brand`, `condition`, `availability`, `price` matching the landing page including currency and tax treatment, and `shipping` when rates are not configured in the channel.
- **Price and availability mismatch between feed and page is the top disapproval cause**; a stale feed on a promo day disapproves the exact items being promoted. Sync availability at least as often as stock changes matter (`inventory.md`).
- Feed titles are optimized separately from page titles — feed titles chase query terms, page titles chase the brand's voice. Keep both generated from the same structured fields, not typed twice.
- Excluded items are a decision: out-of-stock, negative-margin, and regulated products stay out of the feed rather than being disapproved by the channel (`marketplaces.md`, `acquisition.md`).

## Catalog Operations at Scale

| Operation | The trap | Do instead |
|---|---|---|
| Bulk price change | An overwrite applied to the wrong filter takes the whole catalog to a rounding error | Export → transform → validate row count and min/max → import; confirm the affected count first (`bulk_change_confirm`) |
| Bulk import | A missing column blanks that field for every row | Import only the columns being changed, keyed by SKU |
| Adding a variant option to an existing product | Some platforms recreate every variant and lose their SKUs and stock | Test on one product, verify SKUs survived, then batch |
| Renaming a product URL | Old URL 404s | Redirect in the same turn (`storefront.md`) |
| Deleting discontinued products | Kills the page and the history | Discontinue state + redirect |
| Translating the catalog | Machine-translated attributes break filters that were built on the source language | Translate content, keep structured values as codes |

Every bulk operation gets a dry run and a stated affected-row count before it runs. Catalog damage is quiet: nobody notices 300 products with a blank weight until shipping rates start failing.

## Digital and Non-Physical Products

- No stock, no shipping — but tax treatment differs sharply for digital services in the EU (place of supply is the customer's country from the first sale, with no distance-selling threshold in the same way physical goods have) (`tax.md`).
- Delivery is a licence and a download or access grant; the "order fulfilled" event must be the access grant, not the payment.
- Right of withdrawal for digital content can be waived only with an explicit, recorded consent at purchase. Without that record, the refund is owed.
- Fraud profile is different: no shipping address to verify, instant value, high chargeback exposure — tighten screening rather than reusing the physical rules (`fraud.md`).

**Write after catalog work**: SKU scheme and taxonomy conventions the user declares into `config.yaml` under `conventions`; COGS, freight and fee changes per SKU or category into `## Unit Economics` with an `as of` date; a supplier learned while sourcing into `## Suppliers` (person into `contacts.md`); and a catalog structure, feed mapping or bulk-edit procedure that finally worked into `artifacts/<kebab-name>.md` with its `## Boxes` line (`memory-template.md`).
