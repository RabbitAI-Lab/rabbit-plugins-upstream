# Slot and Dimension Contract

## General rules

- Treat platform and category requirements as higher priority than these defaults.
- Treat exact A+ image dimensions as module-specific; there is no universal A+ canvas.
- Distinguish `delivery_size` from `generation_size`.
- Record width before height using `WIDTHxHEIGHT`.
- Never stretch an image to reach delivery size. Recompose or crop only when the slot permits it.

## Default production matrix

| Group | Default slot | Production default | Notes |
|---|---|---:|---|
| MAIN | `MAIN` | `2000x2000` | Shared across desktop and mobile Listing surfaces |
| Listing | `L1-L7` | `2000x2000` | Use only the number of defensible roles needed |
| Video | `V1` | `1920x1080` | Cover or storyboard frame, not a substitute for Listing images |
| Standard A+ | `A1-An` | Exact selected module size | Verify the module specification before final delivery |
| Premium A+ desktop | `A1-An` | Common full-width preset `1464x600` | Use only for a matching Premium module |
| A+ mobile | `M1-Mn` | Exact selected mobile module size | Common presets vary; never assume one universal size |

Common A+ planning presets such as `970x300`, `970x600`, `1464x600`, `600x450`, and `1200x900` are not interchangeable. Attach each size to a named module or an explicitly supplied template.

## MAIN contract

Primary objective: immediate product recognition.

- Use a pure white background when required by the marketplace/category.
- Show the exact item and quantity being sold.
- Keep the product complete and uncropped.
- Target roughly 80%–90% effective frame occupancy unless category rules require otherwise.
- Exclude added text, decorative badges, watermarks, borders, and confusing props.
- Do not show accessories that are not included.

## Listing secondary role library

Select distinct roles according to product evidence:

| Role | Customer question | Typical composition |
|---|---|---|
| Lifestyle hero | What does it look like in use? | Product-led realistic scene |
| Core benefits | Why should I buy it? | Product plus 2–4 concise evidence-backed callouts |
| Feature operation | How does the feature work? | One function or controlled state comparison |
| Material detail | Is the build credible? | Macro/detail views tied to the real product |
| Dimensions | Will it fit? | Complete product with confirmed measurement lines |
| Usage or installation | How is it used or installed? | Clear steps or a natural interaction |
| Package contents | What will I receive? | Confirmed items only, clearly separated |
| Comparison or trust | Why this option? | Factual, defensible comparison without attacking competitors |

Do not fill all roles automatically. Replace unsupported roles, merge weak roles, or reduce the set.

## A+ narrative roles

A+ should extend the decision journey rather than repeat Listing images at another aspect ratio. Common roles include:

1. Brand or product promise.
2. Core differentiator.
3. Feature explanation.
4. Lifestyle or use context.
5. Material, construction, or detail.
6. Size, installation, or compatibility.
7. Brand trust, range comparison, or closing story.

Choose module count and type from the actual Standard or Premium A+ template available to the seller.

## Slot manifest fields

Every planned slot must contain:

| Field | Requirement |
|---|---|
| `slot_id` | Unique identifier |
| `group` | MAIN, LISTING, APLUS_DESKTOP, APLUS_MOBILE, or VIDEO |
| `narrative_role` | One primary purpose |
| `customer_question` | Decision question answered by the slot |
| `delivery_size` | Final required size |
| `generation_size` | Model request size, if different |
| `text_policy` | FORBIDDEN, OPTIONAL, REQUIRED, or NATIVE_MODULE_TEXT |
| `product_state` | Exact state shown |
| `fact_keys` | Facts used by this slot |
| `reference_roles` | Required reference images |
| `paired_slot` | Device counterpart or NONE |
| `missing_evidence` | Explicit list |
| `status` | READY, NEEDS_REVIEW, or BLOCKED |

