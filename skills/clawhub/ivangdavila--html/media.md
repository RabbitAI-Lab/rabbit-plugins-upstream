# Media — Images, Video, Audio, Embeds

Everything that arrives over the network and lands in a box. The markup decides the layout stability, the download size, and whether it plays at all.

**Contents:** [Every Image](#every-image) · [Formats](#formats) · [Responsive Images](#responsive-images) · [`picture`](#picture) · [Inline SVG](#inline-svg) · [Video](#video) · [Audio](#audio) · [Captions and Tracks](#captions-and-tracks) · [Iframes](#iframes) · [Third-Party Embeds](#third-party-embeds) · [Canvas and Fallbacks](#canvas-and-fallbacks) · [Media Review](#media-review)

## Every Image

```html
<img src="/hero.avif" alt="…" width="1600" height="900"
     loading="eager" fetchpriority="high" decoding="async">
```

| Attribute | Rule |
|---|---|
| `alt` | Always present; content decided by the image's job (`accessibility.md`) |
| `width` / `height` | Always, as unitless intrinsic values. The browser derives `aspect-ratio: 1600 / 900` before the bytes arrive; CSS can still resize it. Only the ratio has to be right (SKILL.md Rule 3) |
| `loading` | `eager` (default) for anything in the first viewport, `lazy` for everything else. Lazy-loading the LCP image measurably delays it and hides it from the preload scanner |
| `fetchpriority` | `high` on the LCP image, `low` on below-fold decorative images. Chromium and Safari support it; Firefox since 132 — harmless where unsupported |
| `decoding="async"` | Lets the browser decode off the main thread; the default (`auto`) is usually equivalent, but explicit `async` helps on long lists |
| `srcset` / `sizes` | Whenever the rendered width varies (`responsive images` below) |
| `referrerpolicy` | For hotlinked third-party images that reject requests carrying your referrer |

A CSS `background-image` cannot be lazy-loaded by the browser, cannot carry `alt`, and is invisible to the preload scanner. Use `<img>` for content images and reserve backgrounds for decoration.

## Formats

| Format | Use for | Notes |
|---|---|---|
| AVIF | Photos, hero images | Best compression; slower to encode, and quality settings are not comparable to JPEG's numbers |
| WebP | Photos and graphics, universal fallback | ~25–35% smaller than JPEG at equivalent quality; supported everywhere current |
| JPEG | The last-resort fallback | Progressive encoding for large images |
| PNG | Screenshots, sharp edges, transparency | Lossless; enormous for photographs |
| SVG | Icons, logos, diagrams | Scales to any DPI; sanitize any SVG you did not author (`security.md`) |
| GIF | Nothing | An MP4 or WebM of the same animation is typically 5–20× smaller. Use `<video autoplay muted loop playsinline>` |

## Responsive Images

Two independent problems, two mechanisms:

**Same image, different sizes → `srcset` with `w` descriptors + `sizes`.**

```html
<img src="/photo-800.jpg" alt="…" width="1600" height="900"
     srcset="/photo-400.jpg 400w, /photo-800.jpg 800w, /photo-1600.jpg 1600w"
     sizes="(min-width: 60rem) 50vw, 100vw">
```

- `sizes` tells the browser how wide the image will render **before CSS is applied** — the whole point is that the choice happens in the preload scanner. A wrong `sizes` is worse than none: `sizes="100vw"` on an image that renders at 400px downloads four times the bytes it needs.
- `w` descriptors are the image's real pixel widths. The browser multiplies by the device pixel ratio itself; do not pre-multiply.
- Three to four steps is plenty. Doubling widths (400/800/1600) covers 1× and 2× screens with no gaps.
- `sizes="auto"` with `loading="lazy"` lets the browser use the actual layout size — Chromium-only for now, and it only works on lazy images.
- Fixed-size images (an avatar at 48px) use `x` descriptors instead: `srcset="/a.png 1x, /a@2x.png 2x"` and no `sizes`.

## `picture`

For **format fallback** and **art direction** — a different crop, not a different size:

```html
<picture>
  <source type="image/avif" srcset="/hero.avif">
  <source type="image/webp" srcset="/hero.webp">
  <img src="/hero.jpg" alt="…" width="1600" height="900">
</picture>
```

- The browser takes the **first matching `<source>`** and never re-evaluates. Order most-preferred first; a JPEG source before an AVIF one means the AVIF is never used.
- `media` on a `<source>` does art direction: a square crop under 40rem, a wide crop above.
- The `<img>` is mandatory: it carries `alt`, `width`, `height`, `loading` and the final fallback. Attributes on `<source>` do not substitute for it.
- Never use `<picture>` for plain resolution switching — that is `srcset` alone, and it lets the browser make a better choice.

## Inline SVG

- Decorative icon: `<svg aria-hidden="true" focusable="false">` beside real text.
- Meaningful graphic: `role="img"` plus `<title>` as the first child, and `aria-labelledby` pointing at it for older AT.
- `focusable="false"` matters on legacy Edge/IE-derived engines where SVGs entered the tab order.
- Inline SVG is styleable by CSS and needs no request; `<img src="*.svg">` is cacheable and isolated but cannot inherit `currentColor`. Choose by whether the icon changes color with its context.
- SVG from an untrusted source is executable markup — it can carry `<script>` and event handlers (`security.md`). Detailed authoring is the `svg` skill.

## Video

```html
<video controls width="1280" height="720" poster="/poster.jpg"
       preload="metadata" playsinline>
  <source src="/clip.webm" type="video/webm">
  <source src="/clip.mp4" type="video/mp4">
  <track kind="captions" src="/clip.en.vtt" srclang="en" label="English" default>
  <p>Your browser cannot play this video. <a href="/clip.mp4">Download it</a>.</p>
</video>
```

| Attribute | Rule |
|---|---|
| `controls` | Unless you build a complete keyboard-accessible replacement — which means play/pause, seek, volume, captions toggle, and fullscreen, all reachable by keyboard |
| `width`/`height` or `poster` dimensions | Same layout-shift rule as images |
| `preload` | `metadata` is the right default: duration and dimensions without the payload. `auto` on several videos per page can outweigh every other asset combined |
| `playsinline` | Required or iOS takes over the screen in fullscreen on play |
| Autoplay | Only ever `autoplay muted loop playsinline` — browsers block unmuted autoplay. Anything over 5s needs a pause control (WCAG 2.2.2) |
| `poster` | Otherwise the element is blank until the first frame decodes |
| Fallback content | Inside the element, after the sources — shown only when the element is unsupported, not when the file 404s |

MP4/H.264 is the universal fallback; WebM/VP9 or AV1 first for smaller files. Order the sources best-first, same as `<picture>`.

## Audio

`<audio controls preload="metadata">` with the same source-fallback pattern. Provide a transcript for anything spoken — it is the WCAG requirement (1.2.1) and it is also the only version that is searchable and skimmable.

## Captions and Tracks

| `kind` | Content |
|---|---|
| `captions` | Dialogue **plus** relevant non-speech sound, for users who cannot hear the audio |
| `subtitles` | Translation of dialogue, for users who cannot understand the language |
| `descriptions` | Narration of visual information for users who cannot see it |
| `chapters` | Navigation points |
| `metadata` | Script-only, never displayed |

`default` on one track only. WebVTT files must be served with `text/vtt` and are subject to CORS when cross-origin. Auto-generated captions are a draft: WCAG 1.2.2 expects accuracy, and names, jargon and numbers are exactly what auto-captioning gets wrong.

## Iframes

```html
<iframe src="https://example.com/widget" title="Booking widget"
        width="600" height="400" loading="lazy"
        sandbox="allow-scripts allow-forms"
        allow="geolocation 'none'" referrerpolicy="strict-origin-when-cross-origin"></iframe>
```

- **`title` is mandatory** — it is the frame's accessible name, and a frame list of "iframe, iframe, iframe" is unnavigable.
- `sandbox` with no value removes everything: scripts, forms, popups, top-level navigation, same-origin identity. Add back one token at a time: `allow-scripts`, `allow-forms`, `allow-popups`, `allow-downloads`, `allow-same-origin`, `allow-top-navigation-by-user-activation`.
- **`allow-scripts` plus `allow-same-origin` on same-origin content defeats the sandbox** — the framed document can reach its parent and remove the attribute. Host sandboxed content on a different origin.
- `allow` is Permissions Policy: camera, microphone, geolocation, fullscreen, autoplay. Deny by omission; the default for most powerful features in a cross-origin frame is already off.
- `loading="lazy"` on below-fold embeds; a single third-party embed frequently costs more than the entire host page.
- A blank frame is usually the *other* side refusing: `X-Frame-Options: DENY` or a CSP `frame-ancestors` that excludes you. Neither is fixable from your markup.
- `srcdoc` renders inline HTML in the frame — useful for previewing untrusted content behind a sandbox (`security.md`).

## Third-Party Embeds

| Embed | Markup cost |
|---|---|
| Video platform player | 500 KB–1 MB of JS and several connections. A poster image plus a click-to-load `<iframe>` removes it from the initial load entirely |
| Map | Same pattern; a static map image linking to the interactive one is often enough |
| Social post | Loads a script that rewrites your DOM and sets cookies — a quoted `<blockquote>` with a link is a legitimate substitute |
| Comment widget | Lazy-load below the fold; it is never the LCP element |
| Analytics / tag manager | Not visual, but blocking if inline and un-deferred (`performance.md`) |

Before proposing an embed, name the origin it contacts, the capabilities it requests, and whether a facade would do. Consent and tracking implications are a `security.md` and legal matter, not a markup default.

## Canvas and Fallbacks

`<canvas>` content is invisible to assistive tech. Fallback content between the tags is only shown when canvas is unsupported — not when the drawing is meaningless without sight. For anything conveying information, render an accessible DOM equivalent (a table, a list) alongside or behind it, and keep interactive canvas elements mirrored as real focusable controls.

**When an image policy is settled for a site** — formats, breakpoint widths, the CDN's URL shape, the LCP element per template — record it in `## Pages` of `~/Clawic/data/html/memory.md` against the template it applies to, or as `artifacts/images-<site>.md` when it is a page-long recipe (`memory-template.md`). **When an embed or a codec behaves differently on one client** — a browser that ignores `sizes`, a webview that blocks autoplay, a CMS that strips `loading` — that is a row in `## Quirks` with the surface and the date.
