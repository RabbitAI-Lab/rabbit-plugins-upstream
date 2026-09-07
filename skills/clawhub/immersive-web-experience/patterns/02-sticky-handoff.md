# Sticky Handoff

Let an outgoing sticky element remain briefly while the incoming scene meets and assumes its role.

**Use when:** adjacent scenes share a title, object, edge, or visual axis but do not need a fully pinned timeline.

**Build:** use CSS sticky for layout stability; animate the incoming alignment and outgoing release with GSAP. Define a narrow overlap zone and deterministic z-order.

**Continuity:** transfer color, scale, crop, phrase, or position at the overlap.

**Avoid:** multiple sticky ancestors, unclear stacking contexts, or invisible content blocking pointer input. On small screens, allow a simpler normal-flow handoff.
