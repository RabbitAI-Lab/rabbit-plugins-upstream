# Workflow 07 — Implementation

Read [GSAP engineering](../references/gsap-engineering.md), [accessibility](../references/accessibility.md), and [WebGL integration](../references/webgl-integration.md) only if the Experience Concept justified WebGL.

1. Preserve the project's architecture and semantics.
2. Implement a vertical slice containing one complete scene and its transitions.
3. Verify lifecycle, reverse behavior, resize, mobile, reduced motion, and representative performance.
4. Establish reusable primitives only after the slice reveals stable patterns.
5. Implement remaining scenes from their contracts.
6. Add loading/failure/fallback states and explicit cleanup.
7. If `gsap-motion` exists, give it the Motion System and scene contracts for low-level GSAP work; review its output against this skill.

Do not add WebGL, a smooth-scroll library, or a custom cursor opportunistically. Keep essential content available before enhancement. Report deviations from the Experience Concept rather than silently changing it.
