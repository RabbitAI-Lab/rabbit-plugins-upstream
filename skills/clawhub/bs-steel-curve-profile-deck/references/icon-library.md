# Inline SVG icons

Preserve [third-party-notices.md](third-party-notices.md) when redistributing these icon forms; the notice includes Lucide and Feather-derived geometry.

Use the Lucide convention (ISC): 24-unit viewBox, no fill, currentColor stroke, rounded caps and joins, stroke width 1.7. Use icons beside visible labels in service cards, role cards, quality callouts, contact pills, and final actions. Decorative chevron stacks (`.decor.chev`) are plain stroked SVG paths, not icons. Never use emoji, glyph arrows, or icon fonts.

```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M5 12h14m-6-6 6 6-6 6"/>
</svg>
```

| Meaning | Paths |
| --- | --- |
| Network | `<rect x="3" y="3" width="6" height="6" rx="1"/><rect x="15" y="15" width="6" height="6" rx="1"/><path d="M6 9v9h9M9 6h9v9"/>` |
| Chart | `<path d="M3 3v18h18M7 15v-4M12 15V7M17 15v-7"/>` |
| Shield | `<path d="M12 22s8-4 8-11V5l-8-3-8 3v6c0 7 8 11 8 11Z"/><path d="m8 12 3 3 5-6"/>` |
| People | `<circle cx="9" cy="8" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 5a3 3 0 0 1 0 6M21 21v-3a6 6 0 0 0-3-5"/>` |
| Calendar | `<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 11h18"/>` |
| Arrow | `<path d="M5 12h14m-6-6 6 6-6 6"/>` |
| Clipboard | `<rect x="5" y="4" width="14" height="18" rx="2"/><rect x="9" y="2" width="6" height="4" rx="1"/><path d="M9 12h6M9 16h6"/>` |
| Mail | `<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>` |
| Map pin | `<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/>` |
| Bell | `<path d="M3 15h18M5 15a7 7 0 0 1 14 0M12 4v2M10 20h4"/>` |

Real AI integration marks may use LobeHub monochrome `fill="currentColor"` geometry, with an adjacent visible product label and appropriate license notice. Use them only for a real integration; never as decoration or a fictional organization logo. The sample has no integration marks.
