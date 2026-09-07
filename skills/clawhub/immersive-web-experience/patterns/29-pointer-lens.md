# Pointer Lens

Use an optional lens around the pointer to reveal detail, alternate material, metadata, or depth.

**Use when:** exploration is supplemental and the revealed layer rewards inspection.

**Build:** use pointer events and a damped `quickTo`/setter path; clamp the lens inside useful bounds; ensure the underlying content/action remains available; provide touch tap or static alternatives. Use a shader only for genuine optical distortion.

**Continuity:** the lens reveals the same world's hidden layer.

**Avoid:** replacing the cursor, hiding essential information, high-latency tracking, or activating on coarse pointers. Disable for reduced motion when travel or distortion is substantial.
