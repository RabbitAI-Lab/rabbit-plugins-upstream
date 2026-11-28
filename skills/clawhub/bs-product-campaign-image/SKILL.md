---
name: bs-product-campaign-image
description: "Create conversion-aware product campaign images from a real product reference, campaign goal, and placement brief. The workflow delivers polished Hero images, promotional Banners, social campaign visuals, and lifestyle scenes while protecting product identity, copy-safe zones, and crop flexibility."
---

# Product Campaign Image

Produce finished marketing images that make the real product recognizable and leave deliberate room for campaign copy. Use this Skill for storefront Hero images, offer Banners, social promotions, launch visuals, listing images, and lifestyle product scenes.

## Approve the Skillry budget

For Skillry execution, check access and permissions with `prepare_skill_execution`. Verify the model and reference support with `list_media_models`. Upload local reference images with image permission. Quote each final specification using `quote_media` or `skillry media --quote-only`. Show the planned steps, their estimated or maximum credits, and the exact combined budget. Wait for the user to confirm that amount in chat.

After confirmation, use the same credential and API base to create one shared run with `start_skill_run`, or `skillry run start --name "Media task" --skill bs-product-campaign-image --budget-points <confirmed-total> --run-id <uuid>`. API-key clients can instead POST `id`, `name`, `skill_slug`, and `budget_points` to `/api/relay/runs`. Set `SKILLRY_RUN_ID` to that registered UUID when running bundled scripts, or pass `--run-id` on CLI media commands. Record one request ID per step and use it to recover interrupted jobs. Report settled credits from the job or run status, including any settlement at the approved ceiling when usage evidence is unavailable.

## Generation provider (ask first)

Before generating any new images, present these 3 options upfront and confirm the user's choice:

1. **Skillry API Key (Default)**: Use Skillry (`--provider skillry`, default when omitted) with `SKILLRY_API_KEY`, a logged-in `skillry` CLI session, or Skillry MCP tools (`upload_image_reference`, `quote_media`, `start_skill_run`, `generate_media`, `media_status`, `download_media`).
2. **Codex Built-in Image Generation (Recommended in Codex)**: When running inside a Codex client (`CODEX_THREAD_ID`, `CODEX_SESSION_ID`, or native `image_gen` tool detected), use Codex's built-in `image_gen` tool directly with this Skill's exact prompt, aspect ratio, and reference rules instead of an API key.
3. **Custom FAL API Key (`FAL_KEY`)**: Generate directly through FAL using `--provider fal` and the user's own `FAL_KEY`.

For the default Skillry API Key route, check `account_status` for `connected: true` (using `SKILLRY_API_KEY` / Skillry MCP credentials) and eligible credits before production, and never paste credentials in chat.

## Required inputs

Collect these before generation. Read existing product-marketing or brand context in the current project first and do not ask for information already available.

- At least one clear product reference image. Prefer a front three-quarter view plus side or packaging views when shape, label, or finish must remain exact.
- The campaign goal, audience, placement, and required output dimensions.
- Approved product claims and exact on-image copy, if any.
- Brand colors, typography, visual references, and prohibited treatments.
- The product details that must not change: silhouette, proportions, materials, cap, controls, label geometry, color, and legally required marks.

If no usable product reference exists, stop and explain that the result can be a concept only; do not claim product fidelity.

## Workflow

### 1. Define the conversion job

Write one sentence that identifies the viewer, the single intended action, and the one product benefit the image should communicate. Choose one primary format:

- Hero image: strong product focus and a large copy-safe zone.
- Promotional Banner: one offer hierarchy, a clear visual path to the CTA area, and small-screen legibility.
- Social campaign image: immediate thumb-stop contrast with crop-safe central information.
- Lifestyle image: the product shown in a credible use moment, not as background decoration.
- Listing image: accurate product presentation and evidence-led callouts rather than mood alone.

Do not combine several messages into one frame. Ask the user to prioritize when claims compete.

### 2. Build the product identity lock

Inspect every supplied reference and create a short identity sheet before prompting. Record:

- silhouette and relative dimensions;
- material, finish, seams, edges, controls, cap, and openings;
- label boundary, dominant colors, and any text that must remain unchanged;
- camera views that are supported by the references;
- details that are hidden or ambiguous and therefore must not be invented as facts.

When fidelity matters, use the image-edit endpoint with the product reference as the first input. State invariants explicitly in every edit prompt: change only the scene, lighting, props, or requested campaign treatment; preserve the product geometry and product-facing details. Use a mask when the background can be isolated reliably.

### 3. Plan composition and safe zones

Use a normalized 100 x 100 frame. Mark the product box, copy-safe box, CTA-safe box, and crop-safe core before generation. Keep critical content at least 6 percent from the edge unless the placement specifies a larger margin.

- For a left-copy Hero, reserve approximately x=6–48 and y=12–82 for text, with the product on the right.
- For a right-copy Banner, reserve approximately x=62–94 and y=14–82 for the offer and CTA.
- For multi-format campaigns, keep the product and primary visual cue inside the central 60 percent so 1:1 and 4:5 crops remain viable.
- Keep texture, highlights, props, and limbs out of the copy-safe box. Negative space must be calm enough for readable type.

### 4. Write the generation brief

Use `references/campaign-brief.md`. Describe the real product first, then the environment, action, camera, lighting, composition, palette, safe zones, invariants, and exclusions. A useful prompt is concrete enough that another reviewer can predict the frame.

Prefer a clean plate with no generated words when the campaign needs more than a very short headline. Add typography deterministically in the user's existing design workflow after the product scene is approved. If the user explicitly wants generated lettering, quote the exact text, keep it short, and verify every character before delivery.

### 5. Use the managed image connection and approve cost

Call `list_media_models` and require an enabled `gpt-image-2` route supporting the exact quality, dimensions, reference count and editing operation. Preserve the selected GPT Image model, product references and quality; a channel choice is a server detail, not permission to downgrade to provider-default quality or invent exact dimensions. If no priced route preserves these requirements, stop before generation.

For a product-preserving variation via Skillry MCP/CLI, first upload each local image privately with `upload_image_reference` (returning a private UUID `reference_id`) rather than using external `image_urls`: pass `reference_id` for 1 reference or `reference_ids` (array, 2-16 UUIDs, ordered with the primary product reference first) for multi-reference edits. Note `max_reference_edge` limits from `list_media_models` (1024px for `gpt-image-2`, 4096px for `gpt-image-2.5-flare` and `nano-banana-pro`) and all 18 supported pixel sizes with `low`, `medium`, or `high` quality tiers.

Quote each final input with `quote_media` before creating a run, show the combined fixed or maximum credits, and wait for the user to confirm that exact budget. Save a UUID runId, one requestId per paid image, prompts and output paths before submission. Use `start_skill_run` with the user-approved total `budgetPoints`, this Skill's slug and a descriptive name. Keep the master, corrections and approved variants in that run.

Call `quote_media` with the full input and matching run/step. Show the fixed points and exact specification. Call `generate_media` once with unchanged input, saved requestId, quoteToken and approvedPoints exactly equal to the quote. Expired quotes or specification/rate changes require a refreshed price and explicit approval. Never increase the total budget automatically. Skill access and generation credits are separate.

Use `media_status` with the saved job/request ID and obey its polling interval. For an owned completed result, call `download_media` with its job ID and a new absolute output filename. The tool downloads through the configured connection and never sends the user's key to an asset host. Inspect the actual format and dimensions and preserve the original. Unsupported asset hosts or download failures require read-only recovery, not a new generation.

Unknown results retain their request IDs and reservations; do not invent a refund, retry a paid request or switch providers automatically. A user-approved correction is a separate paid request with its own record.

### 6. Review one master before variants

Generate and review one master composition first. Compare it against the identity sheet at 100 percent zoom. Reject changed geometry, label drift, implausible reflections, extra accessories, warped hands, unreadable text, or a safe zone contaminated by detail.

Make one targeted correction at a time. A correction is a new paid task, so obtain approval before submitting it and preserve the previous run record and output.

### 7. Adapt the approved master

Create each requested placement from the approved art direction. Do not merely stretch one export.

- Recompose for each aspect ratio while preserving the product's scale and visual priority.
- Keep approved copy and CTA zones within the placement's safe area.
- Match lighting, palette, product details, and prop language across the set.
- Export descriptive filenames such as `product-launch-hero-16x9.webp`.

### 8. Run quality control

Use `references/quality-checklist.md`. Check product identity, composition, claims, typography, crop safety, accessibility, technical dimensions, file format, and visible source identity. View every final at full size and at its likely mobile display size.

Deliver the approved images, a short usage note for each placement, the prompt and run record for reproducibility, and any unresolved fidelity limitations. Never describe an invented or uncertain product detail as verified.

## Guardrails

- Do not use a third-party logo, slogan, branded packaging, copyrighted character, or recognizable campaign asset unless the user supplies it and confirms the right to use it.
- Do not fabricate certifications, reviews, discounts, performance numbers, ingredients, sustainability claims, or product capabilities.
- Do not alter regulated label information or hide required warnings.
- Do not infer protected traits or create deceptive before-and-after evidence.
- Do not overwrite source images. Preserve originals and save every approved variant separately.
- Do not expose `SKILLRY_API_KEY`, request headers, or secret-bearing logs.
