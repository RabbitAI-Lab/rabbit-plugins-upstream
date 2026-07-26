# HTML Email

A separate dialect with its own engine, its own century, and its own rules. Almost nothing from the rest of this skill applies. Governed by `email_client_floor`.

**Contents:** [The Two Builds](#the-two-builds) · [The Skeleton](#the-skeleton) · [What Works Where](#what-works-where) · [Outlook Desktop](#outlook-desktop) · [Gmail](#gmail) · [Apple Mail and iOS](#apple-mail-and-ios) · [Images](#images) · [Buttons](#buttons) · [Dark Mode](#dark-mode) · [Accessibility in Email](#accessibility-in-email) · [Preheader and Subject](#preheader-and-subject) · [Size Limits](#size-limits) · [Testing](#testing)

## The Two Builds

| `email_client_floor` | Layout | Cost |
|---|---|---|
| `outlook-desktop` (default) | Nested tables, inline styles, fixed 600px, VML for background images and buttons | Works everywhere, including Outlook 2007–2019 on Windows |
| `modern` | Single-column with `<div>`s, `<style>` in the head, some flex | Breaks in Outlook desktop and in a few corporate clients; acceptable only when the audience is known |

Ask nothing; read `email_client_floor` and build accordingly. If the user says their audience is consumer mobile, that is a declaration — record `email_client_floor: modern` in `config.yaml`.

## The Skeleton

```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <meta name="supported-color-schemes" content="light dark">
  <title>Order confirmed</title>
  <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
</head>
<body style="margin:0;padding:0;background:#f4f4f4;">
  <div style="display:none;max-height:0;overflow:hidden;">Preheader text here.&#8203;&#8203;&#8203;</div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr><td align="center">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:100%;">
        <tr><td style="padding:24px;font-family:Arial,sans-serif;font-size:16px;line-height:24px;color:#222;">
          Content
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
```

- `role="presentation"` on every layout table, so screen readers do not announce rows and columns.
- `cellpadding="0" cellspacing="0" border="0"` on every table — the attributes, not the CSS: Outlook reads the attributes.
- 600px is the convention that fits the Outlook reading pane; 640 is the practical ceiling.
- Padding lives on `<td>`, never as a margin. Margins are unreliable across clients; `<td style="padding:…">` is not.
- The `PixelsPerInch` block fixes image scaling on high-DPI Windows displays.

## What Works Where

| Feature | Reality |
|---|---|
| `<style>` in `<head>` | Supported by most clients including Gmail webmail; stripped by some (older Gmail app with a non-Gmail account, some corporate filters). Always inline the critical styles and use `<style>` only for enhancements and media queries |
| External CSS, `@import` | Never |
| Flexbox, grid, `position` | Not in Outlook desktop; unreliable elsewhere |
| Media queries | Widely supported; **not** in the Gmail app when the account is a non-Gmail address — hence a mobile-first single column that needs no query |
| Web fonts | Apple Mail and some others; always a full font stack fallback |
| `background-image` on a `<td>` | Ignored by Outlook desktop without VML |
| Rounded corners, shadows | Ignored by Outlook desktop; degrade to square, do not depend on them |
| SVG | Blocked in most clients |
| Forms, scripts, video | Stripped everywhere; link out instead |
| `<div>` layout | Fine for a single column; Outlook still needs a table wrapper for width and background |

## Outlook Desktop

Outlook 2007–2019 on Windows renders with the **Word** engine. Practical rules:

- Wrap fixed-width content in a `<!--[if mso]>` conditional table when the outer layout is a div.
- `mso-` properties are the only way to control Word behaviors: `mso-line-height-rule:exactly` next to every `line-height`, `mso-hide:all` to hide an element, `mso-padding-alt` where padding is ignored.
- Word inserts a page break roughly every 22 inches (~1,800px) of content and can leave a visible line; keep emails shorter, or split into separate tables.
- Background images need a VML `<v:rect>` fallback inside a conditional comment.
- Animated GIFs show only the **first frame** — put the message in frame one.
- `max-width` is ignored; give tables a `width` attribute as well as a CSS width.

## Gmail

- Clips messages larger than **102 KB**; everything past the cut is behind a "[Message clipped] View entire message" link, and tracking pixels below the cut never fire. Inline styles are the main cause of hitting it — deduplicate and drop comments.
- Strips `<style>` blocks when the message exceeds that limit, and ignores CSS it cannot parse — a single invalid declaration can void the whole block.
- Rewrites class names in some contexts; prefer attribute-free inline styling for anything critical.
- Aggressive dark-mode color inversion on some platforms (see below).

## Apple Mail and iOS

- The most capable renderer: web fonts, media queries, most modern CSS.
- Auto-links dates, addresses and phone numbers, restyling them blue. Suppress with `<meta name="format-detection" content="telephone=no,date=no,address=no">` and an explicit color on the wrapping element, or with the `x-apple-data-detectors` selectors in your `<style>`.
- Respects `prefers-color-scheme` properly, which makes it the place to test dark mode first.

## Images

- **Blocked by default in Outlook desktop and in many corporate clients.** The email must be comprehensible with every image off: real text for headlines, `alt` on every image, and a background color behind logos so alt text is legible.
- Always set `width` and `height` attributes plus `style="display:block;"` — the display rule removes the mystery gap under images in Outlook.
- Serve at 2× and constrain with `width` for retina.
- Never place critical information — price, date, code — inside an image only.
- Host images on a stable public URL; embedded (CID) attachments raise spam scores and behave inconsistently.

## Buttons

Bulletproof pattern, no images:

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0">
  <tr><td align="center" bgcolor="#0a5" style="border-radius:4px;">
    <a href="https://example.com/order/4821"
       style="display:inline-block;padding:14px 28px;font-family:Arial,sans-serif;
              font-size:16px;color:#ffffff;text-decoration:none;border-radius:4px;">
      View your order
    </a>
  </td></tr>
</table>
```

- The background is on the `<td>` (`bgcolor` attribute for Outlook), the padding on the `<a>` — that way the whole area is clickable in clients that support it, and the color still shows where the padding is ignored.
- Minimum 44×44 px of tap target.
- Link text says what happens; "Click here" is unreadable in a link list and unhelpful in a screen reader.

## Dark Mode

Three client behaviors, in increasing hostility: respects `prefers-color-scheme` (Apple Mail, Outlook.com); partially inverts (some Gmail platforms); fully inverts everything (Outlook Windows dark mode).

- `<meta name="color-scheme">` and `supported-color-schemes` opt into the first tier.
- Design for inversion: avoid pure white backgrounds behind dark logos, use transparent PNGs with a mid-tone stroke, and never rely on a dark logo on a light background surviving.
- Test a dark-mode screenshot before shipping; there is no CSS that guarantees the third tier.

## Accessibility in Email

- `lang` on `<html>`, and a real `<title>` — some clients announce it.
- `role="presentation"` on every layout table (mandatory, and the reason email tables are not an accessibility failure).
- Real text over image text; `alt` on every image, `alt=""` on spacers.
- Logical reading order in the source — the DOM order is the reading order regardless of the visual arrangement.
- Contrast 4.5:1 as everywhere else; body copy at 14–16px minimum, and never below 12px.
- One `<h1>`-equivalent heading structure; clients strip much of it, but the ones that keep it benefit.

## Preheader and Subject

- The preheader is the preview text after the subject in the inbox. Hidden div at the very top, 40–100 characters, and it must not repeat the subject.
- Pad the hidden div with zero-width spaces (`&#8203;`, as in the skeleton above) or alternating `&zwnj;&nbsp;` pairs, so the client does not pull the first visible body copy into the preview.
- Subject line practical ceiling ~40 characters on mobile before truncation.

## Size Limits

| Limit | Value |
|---|---|
| Gmail clipping | ~102 KB of HTML |
| Practical total email weight | Under 100 KB HTML; images are separate but still count against load time |
| Outlook page break | ~1,800 px of content height |
| Safe body width | 600 px |
| Minimum tap target | 44×44 px |

## Testing

Screenshot testing across clients is the only method that works; the rendering differences are not derivable. The floor set: Outlook Windows (current and one older), Gmail webmail, Gmail app on Android, Apple Mail on macOS and iOS, and one webmail (Outlook.com or Yahoo). Re-test after any client's major update — that cadence belongs in `## Due`.

**When an email template renders correctly across the client set**, save it to `~/Clawic/data/html/artifacts/email-<name>.md` with the client list and date it was verified on, and add its `## Boxes` line in the same turn (`memory-template.md`). It is the only reliable starting point for the next campaign. **Every client-specific behavior discovered** — a stripped `<style>`, an inversion, a `mso-` property that was required — is a row in `## Quirks` of `memory.md` with the client and version: the same Outlook bug otherwise gets rediscovered every year.
