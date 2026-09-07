# Morph Transition

Transform one meaningful shape, silhouette, or state into another.

**Use when:** the two forms share semantic identity or demonstrate a real transformation.

**Build:** prefer compatible SVG paths, CSS border-radius/clip geometry, or matched intermediate states. Normalize SVG path topology where needed. Use WebGL only for true mesh/material deformation. Preserve a stable center or identifiable feature.

**Continuity:** shape identity carries the transition.

**Avoid:** morphing unrelated objects merely as spectacle, illegible intermediate forms, or expensive per-frame layout. Reduced motion swaps states while retaining the relationship through position/color.
