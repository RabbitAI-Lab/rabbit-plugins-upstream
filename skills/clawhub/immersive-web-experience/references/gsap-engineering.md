# GSAP Engineering

## Tool choice

- `gsap`: timelines, orchestration, transforms, state transitions.
- `ScrollTrigger`: scroll progress, pinning, trigger lifecycle, batch only when conceptually appropriate.
- `Flip`: layout/state continuity for the same semantic object.
- `SplitText`: typographic segmentation where licensing/runtime availability permits; otherwise use an accessible alternative.

Register only used plugins in the client environment. Confirm framework SSR/client boundaries and installed versions before coding.

## Timeline architecture

Give each scene an owned timeline and expose semantic labels or progress. Compose scene transitions at a higher level instead of one global unmaintainable timeline. Use functions for values that depend on current measurements.

Scope selectors, create animations after elements exist, and revert/kill them on unmount. Clean up ScrollTriggers, observers, requestAnimationFrame loops, media listeners, and split text. Use responsive contexts or explicit breakpoint reconstruction.

## Rendering

Prefer `x/y`, scale, rotation, and opacity. Use `will-change` only during active expensive motion. Batch reads before writes, avoid layout queries inside update loops, and use `quickSetter`/`quickTo` for frequent pointer-driven values when appropriate.

## Scroll integration

Use one scroll authority. When a third-party smooth scroller is already present, connect updates and proxies according to its documented integration and refresh measurements after layout changes.

## Quality checks

Test initial render, reverse, rapid input, navigation away/back, resize, font/media load, hidden tabs, multiple mounts, reduced motion, and low-end devices. Development hot reload must not duplicate triggers.
