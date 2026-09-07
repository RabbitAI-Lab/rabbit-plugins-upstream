# FLIP Relay

Use GSAP Flip to move the same semantic element between real layouts.

**Use when:** an item becomes a hero, thumbnail becomes detail, label changes container, or responsive layout should remain natural.

**Build:** capture state, make the real DOM/layout change, then animate from the captured state. Preserve focus and reading order; decide whether absolute positioning is temporarily safe; clean inline styles after completion.

**Continuity:** DOM identity and geometry provide the bridge.

**Avoid:** FLIP across unrelated nodes without an accessibility plan, unstable image dimensions, or frequent layout flips during scroll. Reduced motion applies the layout state immediately.
