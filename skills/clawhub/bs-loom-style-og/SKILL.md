---
name: bs-loom-style-og
description: Create Loom-style OG images. Use them for social media posts.
---

# Loom Style OG Image

Create original 16:9 Open Graph images with this observable visual system:
A vertical split divides a cream typographic pitch from a product-window screenshot over a muted landscape, with a circular webcam portrait overlapping the lower-right and bold black copy leading the hierarchy. The result must fit a new brand and message; it
must not recreate a supplied campaign, logo, person, character, interface, or
piece of source artwork.


## Approve the Skillry budget

For Skillry execution, check access and permissions with `prepare_skill_execution`. Verify the model and reference support with `list_media_models`. Upload local reference images with image permission. Quote each final specification using `quote_media` or `skillry media --quote-only`. Show the planned steps, their estimated or maximum credits, and the exact combined budget. Wait for the user to confirm that amount in chat.

After confirmation, use the same credential and API base to create one shared run with `start_skill_run`, or `skillry run start --name "Media task" --skill bs-loom-style-og --budget-points <confirmed-total> --run-id <uuid>`. API-key clients can instead POST `id`, `name`, `skill_slug`, and `budget_points` to `/api/relay/runs`. Set `SKILLRY_RUN_ID` to that registered UUID when running bundled scripts, or pass `--run-id` on CLI media commands. Record one request ID per step and use it to recover interrupted jobs. Report settled credits from the job or run status, including any settlement at the approved ceiling when usage evidence is unavailable.

## Generation provider (ask first)

Before generating any new images, present these 3 options upfront and confirm the user's choice:

1. **Skillry API Key (Default)**: Use Skillry (`--provider skillry`, default when omitted) with `SKILLRY_API_KEY`, a logged-in `skillry` CLI session, or Skillry MCP tools (`upload_image_reference`, `quote_media`, `start_skill_run`, `generate_media`, `media_status`, `download_media`).
2. **Codex Built-in Image Generation (Recommended in Codex)**: When running inside a Codex client (`CODEX_THREAD_ID`, `CODEX_SESSION_ID`, or native `image_gen` tool detected), use Codex's built-in `image_gen` tool directly with this Skill's exact prompt, aspect ratio, and reference rules instead of an API key.
3. **Custom FAL API Key (`FAL_KEY`)**: Generate directly through FAL using `--provider fal` and the user's own `FAL_KEY`.
## Use this Skill when

- The user invokes `/bs-loom-style-og`.
- A website, launch, article, product, event, or social share needs a distinct
  Open Graph image.
- A team wants several cards to share one repeatable art direction.
- A reference is supplied for high-level visual analysis and the user owns it
  or is authorized to use it.

Do not use this Skill to reproduce a protected logo, mascot, campaign asset,
recognizable person, proprietary interface, or trademarked product design.

## Inputs

Required:

- Brand or project name.
- One short headline.
- Product, audience, or page context.

Optional:

- Brand colors and an authorized logo.
- A desired emotional tone.
- User-owned reference images.
- A required safe area for a specific social platform.

## Workflow

1. **Define the message.** Reduce the card to one brand name, one short
   headline, and one visual idea. Remove supporting copy that cannot survive a
   small social preview.
2. **Set the composition.** Follow `references/visual-system.md` for the
   hierarchy, negative space, image-to-type balance, and edge behavior. Create
   a new arrangement for the current subject.
3. **Choose the palette and material.** Translate the supplied brand into the
   style tags without copying a source palette mechanically: split-layout, product-screenshot, circular-presenter, cream-neutral.
4. **Replace identity.** Remove every source name, logo, person, character,
   interface, slogan, URL, watermark, and trademarked object. Rebuild the
   subject and supporting artwork from scratch.
5. **Set the type.** Quote the requested brand and headline exactly. Keep the
   headline short, readable, and inside a safe central area. Do not invent
   claims, awards, customer names, prices, or metrics.
6. **Set the icons.** Use simple inline Lucide geometry when the card needs a
   generic interface symbol. Follow `references/icon-library.md`; never use
   emoji, dingbats, icon fonts, or a brand mark as decoration.
7. **Set the imagery.** Create original people, devices, diagrams, objects, or
   artwork that serve the new message. Preserve clear silhouettes, useful
   contrast, and enough room for the exact text.
8. **Write the prompt.** Describe only visible facts: layout, scale, palette,
   material, lighting, typography placement, subject, and avoid rules. Do not
   name the reference brand or ask for a replica.
9. **Generate once.** Use the user-selected provider from the options above: Skillry API Key (`scripts/generate.mjs`, default), Codex built-in `image_gen` (if in Codex), or custom `FAL_KEY` (`--provider fal`). A new FAL request is paid; save its task record and never submit an
   automatic replacement after a failure or an unsatisfying result.
10. **Inspect the pixels.** Check all text character by character, then review
    identity removal, originality, contrast, safe areas, accidental logos,
    watermarks, and exact 16:9 dimensions.
11. **Revise narrowly.** Name one visible defect and propose one precise prompt
    change. Wait for explicit approval before a second paid generation.

## Image generation helper

The helper defaults to Skillry (`--provider skillry`, using `SKILLRY_API_KEY` or logged-in `skillry` CLI) and supports `--provider fal` (`FAL_KEY`). Create a
UTF-8 prompt file, then run:

```bash
node scripts/generate.mjs \
  --prompt-file /absolute/path/og-card.txt \
  --output /absolute/path/og-card.webp \
  --task /absolute/path/og-card.fal-task.json \
  --size landscape_16_9 \
  --quality high
```

For an authorized reference, repeat `--reference` with a local PNG, JPEG, or
WebP path. Run the exact same command to resume the same saved request. The
helper will not submit a replacement while its task record exists.

## Output contract

- One original 16:9 Open Graph image per approved generation request.
- WebP for catalog and ordinary web delivery.
- Exact requested brand and headline text, with no extra copy.
- The final prompt or concise prompt summary.
- A short visible-result review, plus the saved task path for FAL runs.

## Non-negotiable constraints

- Create a new composition and new artwork for the current subject.
- Do not reproduce a source identity, logo, mascot, campaign, person,
  proprietary interface, or protected product design.
- Do not use emoji, dingbats, Unicode arrows, or icon fonts as icons.
- Do not invent claims, testimonials, metrics, partnerships, or awards.
- Do not hide defective text with a crop.
- Do not automatically retry or replace a paid provider task.

Before delivery, run `scripts/validate-output.mjs` with `--require-format
webp --require-16-9`. Visual review remains mandatory because a text scanner
cannot read every glyph baked into a bitmap.

---

## More from Skillry

This skill is part of the open-source free skills collection from [Skillry](https://skillry.dev).

- Get a Skillry API key for one-click media generation or explore the full catalog at [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
