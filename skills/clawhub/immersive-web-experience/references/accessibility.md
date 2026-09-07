# Accessibility and Inclusive Motion

## Essential requirements

- Preserve semantic structure, landmarks, headings, reading order, and accessible names.
- Keep all actions keyboard accessible with visible focus and logical focus order.
- Never trap scrolling or focus inside a pinned scene.
- Do not convey essential information only through motion, depth, color, hover, or precise pointer position.
- Provide pause/control for autonomous or lengthy motion when applicable.
- Honor `prefers-reduced-motion` and keep a usable no-animation state.

## Reduced-motion design

Classify motion as essential feedback, orienting, expressive, or ambient. Preserve essential feedback; simplify orienting motion; replace or remove expressive and ambient travel. Disable parallax, rapid zoom, orbit, aggressive scale, and vestibular camera effects. Avoid autoplay motion that cannot be stopped.

## Dynamic scenes

Pinned and visually reordered material must still have sensible DOM order. When scenes change after activation, manage focus only if a real navigation/dialog contract requires it; do not move focus for passive scroll progress. Announce meaningful application state changes, not animation beats.

Test keyboard-only, screen-reader landmarks and names, 200% zoom, text resizing, contrast, coarse pointer, reduced motion, and motion-disabled loading/failure states.
