# Inline SVG icon and marker library

Icons clarify small labels; large original marker people establish the illustration style. Do not use emoji, Unicode dingbats, icon fonts, or glyph arrows. Use SVG elements with accessible text labels when an icon carries meaning.

## Standard shell

These simple path shapes follow the Lucide icon convention. Lucide is ISC licensed. Use a 24-unit viewBox, `stroke="currentColor"`, round caps and joins, and stroke width 2. For large marker illustrations, increase the stroke proportion while keeping text and controls readable.

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
     width="24" height="24" fill="none" stroke="currentColor"
     stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
     aria-hidden="true">
  <!-- Place one of the path sets below here. -->
</svg>
```

| Meaning | Paths to place inside the shell | Suitable placement |
| --- | --- | --- |
| Light bulb | `<path d="M9 18h6m-5 3h4M8.1 14.1a6 6 0 1 1 7.8 0c-.9.7-1.5 1.7-1.5 2.9H9.6c0-1.2-.6-2.2-1.5-2.9Z"/>` | Idea or workshop activity label. |
| Tool | `<path d="M14.7 6.3a5 5 0 0 0-6.4 6.4l-5 5a2 2 0 0 0 2.8 2.8l5-5a5 5 0 0 0 6.4-6.4L14 12l-2-2 2.7-3.7Z"/>` | Resources or hands-on activity. |
| Flag | `<path d="M4 22V3m0 1c4-3 8 3 12 0v10c-4 3-8-3-12 0"/>` | Milestone heading with a visible label. |
| Calendar | `<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 11h18"/>` | Dates or scheduled session. |
| Direction | `<path d="M5 12h14m-6-6 6 6-6 6"/>` | A final invitation beside explanatory text. |

Keep the shell's fill and stroke settings consistent. Give an informative icon an accessible name via `<title>` if no adjacent text labels it. Mark purely decorative art `aria-hidden="true"` and `data-edit="off"`.

## Original marker people

Create fresh path geometry rather than tracing a reference. Use a loosely oval head with one deliberate opening, small filled eye dots, an unfilled torso outline, and one or two active arms. Let slight asymmetry and varying curve tension suggest a pen drawn by hand. Hands may be simple irregular ink blobs. A shared tool, paper, or lamp can carry the accent color.

Use one to four characters in one coherent composition and change poses across slides. Faces remain abstract; do not adapt the identity of a photographed person. Avoid replicating a reference's exact head, arm position, group arrangement, or object. Keep all illustration paths in a `.decor` container so decoration stays separate from meaningful text.

## Real integration marks

If a future user deck genuinely discusses an AI integration, a LobeHub monochrome `fill="currentColor"` mark may be used with its visible product label. Keep the official monochrome geometry and license notice, never recolor the mark, and never use it as decorative art or a fictional organization's logo. The included example has no integration strip and needs no provider logos.

The included icon geometry carries the license notices in [third-party-notices.md](third-party-notices.md); preserve them with redistributed copies.
