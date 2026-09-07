# Clip-Path Iris

Expand or contract a geometric aperture around a focal point.

**Use when:** focus narrows to a detail or opens from a precise origin.

**Build:** animate `clip-path` with compatible shapes; place the focal anchor explicitly; synchronize scale/position so the revealed scene lands stably. Test paint cost on target devices.

**Continuity:** the focal point remains fixed while context changes.

**Avoid:** extreme high-frequency polygons, large repeated paint areas, and iris movement that obscures controls. Prefer transform-based mask layers when cheaper. Reduced motion uses the end state immediately.
