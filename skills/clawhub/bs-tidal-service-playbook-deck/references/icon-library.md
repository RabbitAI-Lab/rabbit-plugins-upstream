# Inline SVG icons

Preserve [third-party-notices.md](third-party-notices.md) when redistributing these icon forms; the notice includes Lucide and Feather-derived geometry.

Use the Lucide convention (ISC): 24-unit viewBox, no fill, currentColor stroke, rounded caps and joins, stroke width 1.7. Use icons beside visible labels in habit cards, journey stages, checklists, scenario cards, quality callouts, and final actions. Inside `.icon-badge` and `.stage-ring` the icon inherits the badge colour. Never use emoji, glyph arrows, or icon fonts.

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
| Bell | `<path d="M3 15h18M5 15a7 7 0 0 1 14 0M12 4v2M10 20h4"/>` |
| Check | `<path d="M20 6 9 17l-5-5"/>` |
| Close | `<path d="M18 6 6 18"/><path d="m6 6 12 12"/>` |
| Calendar check | `<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m9 16 2 2 4-4"/>` |
| Luggage | `<path d="M6 20a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2"/><path d="M8 18V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v14"/><path d="M10 20h4"/><circle cx="16" cy="20" r="2"/><circle cx="8" cy="20" r="2"/>` |
| Bed | `<path d="M2 20v-8a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v8"/><path d="M4 10V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><path d="M12 4v6"/><path d="M2 18h20"/>` |
| Log out | `<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><path d="m16 17 5-5-5-5"/><path d="M21 12H9"/>` |
| Mail | `<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>` |
| Message | `<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>` |
| Book | `<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>` |
| Users | `<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>` |

Real AI integration marks may use LobeHub monochrome `fill="currentColor"` geometry, with an adjacent visible product label and appropriate license notice. Use them only for a real integration; never as decoration or a fictional organization logo. The sample has no integration marks.
