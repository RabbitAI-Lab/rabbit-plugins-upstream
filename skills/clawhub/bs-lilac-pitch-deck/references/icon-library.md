# Inline SVG icon library

Use icons for small functional cues and accent tiles; let the case imagery carry the pictorial story. Icons follow the Lucide convention and use a 24-unit viewBox, currentColor stroke, round caps and joins, and stroke width 1.5. Lucide is ISC licensed. Never use emoji, Unicode dingbats, glyph arrows, or icon fonts.

```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M7 17 17 7M7 7h10v10"/>
</svg>
```

| Meaning | Paths | Placement |
|---|---|---|
| Direction | `<path d="M7 17 17 7M7 7h10v10"/>` | Accent tile beside a closing invitation or a role. |
| Layers | `<path d="m12 3 9 5-9 5-9-5 9-5Zm-9 9 9 5 9-5M3 16l9 5 9-5"/>` | Shared context or collected evidence. |
| Target | `<path d="M12 8a4 4 0 1 0 4 4M12 3a9 9 0 1 0 9 9M12 12l9-9M16 3h5v5"/>` | Objectives and focus. |
| Check | `<path d="m5 12 4 4L19 6"/>` | A completed step with a visible text label. |
| Calendar | `<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 11h18"/>` | Milestones and scheduled reviews. |
| Users | `<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/><circle cx="9" cy="7" r="4"/>` | Team or audience context. |

For a meaningful standalone icon, add an accessible title. Pure decoration has aria-hidden="true" and data-edit="off". Keep geometry separate from editable text so the browser and PowerPoint text boxes remain legible.

## Real integration marks

LobeHub monochrome fill="currentColor" marks are permitted only for a real AI integration, with the official geometry, license notice, and a visible product label. Never recolor them, make them decorative, or use them as a fictional product logo. The supplied examples do not claim integrations and contain no provider marks.

See [third-party-notices.md](third-party-notices.md) for the complete redistributed Lucide ISC and Feather-derived MIT license text.
