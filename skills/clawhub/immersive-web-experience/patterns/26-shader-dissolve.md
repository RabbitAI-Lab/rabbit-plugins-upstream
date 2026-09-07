# Shader Dissolve

Use a controlled threshold/noise field to transform rendered media or geometry.

**Use when:** disappearance, erosion, growth, or material change is a narrative event and the edge quality matters.

**Build:** drive one progress uniform from a scene timeline; tune threshold softness; control noise scale and direction; preserve subject recognition; cap resolution and supply poster/crossfade fallback.

**Continuity:** silhouette, color, or particles should bridge the midpoint.

**Avoid:** dissolving every scene, noisy unreadable edges, or a shader for what opacity can accomplish. Reduced motion uses a brief dissolve or immediate state switch.
