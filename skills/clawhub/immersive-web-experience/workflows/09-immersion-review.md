# Workflow 09 — Immersion Review (Mandatory Final Gate)

Review the result against the Experience Concept, Scene Map, Motion System, [anti-patterns](../references/anti-patterns.md), [performance](../references/performance.md), and [accessibility](../references/accessibility.md).

Score each dimension 0–3 and cite observable evidence:

- concept specificity;
- narrative/spatial coherence;
- scene purpose and pacing;
- transition continuity;
- motion hierarchy and restraint;
- agency and input legibility;
- visual distinctiveness;
- responsive translation;
- reduced-motion and accessibility completeness;
- runtime performance and lifecycle robustness;
- technology proportionality;
- final action/resolution.

Scale: 0 absent/broken, 1 weak, 2 credible, 3 exceptional and coherent.

## Critical failures

The review fails regardless of score if essential content/action is inaccessible; reduced motion is missing; scrolling/focus can become trapped; severe lifecycle leaks occur; the core path is unusable on target mobile; WebGL lacks a meaningful fallback; or the output collapses into a generic SaaS/cards/gradient/fade-in composition contrary to the concept.

## Completion

List critical failures first, then high-impact improvements. Fix all critical failures and repeat affected checks. Completion requires no critical failure and an average of at least 2 across dimensions, unless the user explicitly requested only a prototype. For a prototype, label unverified dimensions and do not present them as production-ready.
