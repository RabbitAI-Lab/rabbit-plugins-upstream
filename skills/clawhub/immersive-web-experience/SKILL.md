---
name: immersive-web-experience
description: Conceive, build, or review cinematic and spatial web experiences organized as connected scenes, using GSAP as the default motion layer and Three.js/WebGL only when real 3D or shader rendering materially improves the concept. Use for immersive landing pages, portfolios, launches, editorials, interactive stories, and experiential product sites; not for routine dashboards or animation-only tweaks.
---

# Immersive Web Experience

Treat the interface as a directed experience, not a stack of sections. Define narrative, space, continuity, motion grammar, interaction, accessibility, and performance before choosing effects.

## Non-negotiable gates

1. Inspect the project and constraints with [workflows/01-project-analysis.md](workflows/01-project-analysis.md).
2. Write an **Experience Concept** with [workflows/03-experience-concept.md](workflows/03-experience-concept.md) before implementing production motion. A lightweight prototype is allowed only to resolve a named uncertainty.
3. Complete the relevant build workflows.
4. Finish with the **Immersion Review** in [workflows/09-immersion-review.md](workflows/09-immersion-review.md). Do not call the experience complete while any critical review item fails.

If the request is only exploratory, stop after the requested concept, direction, or prototype. Do not expand scope into a full build.

## Core operating model

- Replace page-section thinking with scenes, beats, transitions, persistent objects, and a spatial/narrative arc.
- Make motion explain hierarchy, continuity, causality, or spatial relationships. Remove motion that only decorates.
- Prefer native layout, CSS, and GSAP (`gsap`, `ScrollTrigger`, `Flip`, `SplitText`) for DOM-led experiences.
- Add Three.js/WebGL only when the concept requires a true camera, geometry, particles, shaders, post-processing, or continuous 3D transformation that would be brittle or fake in the DOM.
- Establish a coherent motion language before individual animations.
- Design reduced-motion, keyboard, focus, touch, resize, and low-power behavior as first-class variants.
- Measure frame stability, scripting cost, memory, asset weight, and layout shifts on representative devices.

Never default to generic SaaS composition, repeated cards, interchangeable purple/blue gradients, or `section -> fade-in -> section -> fade-in`. Do not imitate references literally; extract principles and create a direction specific to the content and brand.

## Route the task

Read only what the task needs, plus all files explicitly required by the selected workflow.

- Concept and art direction: [experience-design.md](references/experience-design.md), [visual-direction.md](references/visual-direction.md), [immersion-levels.md](references/immersion-levels.md).
- Scene planning and transitions: [scene-architecture.md](references/scene-architecture.md), [transition-design.md](references/transition-design.md), [scroll-storytelling.md](references/scroll-storytelling.md), then [patterns/index.md](patterns/index.md).
- Motion implementation: [motion-language.md](references/motion-language.md), [gsap-engineering.md](references/gsap-engineering.md), [typography-motion.md](references/typography-motion.md).
- Spatial or 3D work: [camera-depth.md](references/camera-depth.md) and, only if justified, [webgl-integration.md](references/webgl-integration.md).
- Review and hardening: [performance.md](references/performance.md), [accessibility.md](references/accessibility.md), [anti-patterns.md](references/anti-patterns.md).

## Required deliverables

Scale detail to the request, but keep these artifacts explicit:

- Experience Concept: premise, intended feeling, audience action, spatial metaphor, signature mechanic, narrative arc, immersion level, technology rationale, and fallback.
- Scene Map: scene purpose, entry state, beats, exit state, persistent objects, input mapping, and transition contract.
- Motion System: timing families, easing families, choreography rules, depth/layer model, text behavior, and reduced-motion translation.
- Implementation Notes: ownership and cleanup, responsive behavior, performance budget, accessibility strategy, and WebGL lifecycle if used.
- Immersion Review: scored findings, critical failures, evidence, and concrete fixes.

## Implementation discipline

- Build one representative vertical slice before multiplying scenes.
- Keep DOM semantics and readable content intact; animation state must not become the sole source of truth.
- Use GSAP contexts or equivalent scoped ownership, revert on teardown, kill listeners/triggers, and rebuild deliberately at responsive boundaries.
- Avoid competing scroll systems. If smooth scrolling exists, integrate and test it rather than silently adding another.
- Animate transforms and opacity by default; justify layout-triggering animation.
- Preserve continuity through shared objects, matched geometry, light, color, sound only when requested, or camera logic.
- Never hide essential content indefinitely behind JavaScript or scroll position.

## GSAP specialist reuse

If a `gsap-motion` skill is available, use this skill to define experience, scene contracts, and motion intent, then delegate low-level GSAP construction and debugging to `gsap-motion`. This skill remains responsible for coherence, technology choice, accessibility, performance, and the final Immersion Review. If `gsap-motion` is absent, implement directly from [gsap-engineering.md](references/gsap-engineering.md).

## Completion standard

The result should feel like one connected world: each movement has a reason, scenes transform into one another, interaction remains legible, and the experience degrades gracefully. A technically impressive effect that weakens comprehension, control, accessibility, or performance is a failed choice.
