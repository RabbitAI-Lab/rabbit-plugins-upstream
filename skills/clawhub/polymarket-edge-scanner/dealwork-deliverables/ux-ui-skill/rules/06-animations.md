# Rule 6 — Animations

Use the project's animation wrappers from `src/components/animate` instead of raw `framer-motion`.

## Available wrappers

- `MotionContainer` — staggered children animations
- `MotionViewport` — animate when scrolling into view
- `MotionLazy` — app-level wrapper with reduced-motion support
- `m` — exported framer-motion component

## Preset variants

- `varFade()` — fade in (directions: `in`, `inUp`, `inDown`, `inLeft`, `inRight`)
- `varZoom()` — zoom in/out
- `varFlip()` — flip animations
- `varScale()` — scale animations
- `varSlide()` — slide animations
- `varBounce()` — bounce animations

## Example

```tsx
import { MotionViewport, varFade } from 'src/components/animate';

<MotionViewport variants={varFade().inUp}>
  <Card>...</Card>
</MotionViewport>
```

Always respect `prefers-reduced-motion` by using `MotionLazy` at the app root and the wrappers above for individual animations.
