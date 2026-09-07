# Transition Design

Treat a transition as a bridge with three phases: release the current scene, transform shared properties, establish the next scene. It should preserve context while redirecting attention.

## Selection criteria

Choose by semantic relationship:

- same object, new context: FLIP, object continuity, morph, or camera reframe;
- entering detail: zoom, portal, aperture, or crop expansion;
- adjacent chapters: horizontal world, directional wipe, or spatial navigation;
- conceptual transformation: mask, material shift, typography handoff, or controlled dissolve;
- hard narrative break: cut, flash, blackout, or silence—used intentionally and rarely.

## Transition contract

Specify the outgoing anchor, incoming anchor, continuity property, occlusion strategy, duration/progress, interruption behavior, and reduced-motion equivalent.

## Interruption

Decide what happens when the visitor reverses scroll, resizes, changes route, or repeats input mid-transition. Scrubbed transitions must be reversible. Triggered transitions should be idempotent or safely cancel/restart.

Do not use a transition merely because it is visually impressive. If it obscures navigation or delays content without adding meaning, remove it.
