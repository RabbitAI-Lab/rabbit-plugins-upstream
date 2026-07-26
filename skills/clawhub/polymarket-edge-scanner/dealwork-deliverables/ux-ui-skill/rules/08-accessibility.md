# Rule 8 — Accessibility

## Required practices

- Every form input needs a visible `label` or `aria-label`.
- Icon-only buttons must have an `aria-label`.
- Use `FormHelperText` / helper text for validation messages.
- Maintain logical heading order (`h1` → `h2` → `h3`).
- Use `prefers-reduced-motion` via `MotionLazy` and animation wrappers.
- Ensure color contrast by sticking to the theme palette.
- Use MUI components which ship with built-in accessibility patterns.

## Avoid

- `onClick` on non-interactive elements (`div`, `span`) without `role` and keyboard handlers.
- Custom selects or checkboxes when MUI components already exist.
- Color-only status indicators; pair color with text or icons.
