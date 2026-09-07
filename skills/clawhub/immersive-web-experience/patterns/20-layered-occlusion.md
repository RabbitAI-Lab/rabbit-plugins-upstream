# Layered Occlusion

Let elements pass in front of and behind one another to make depth legible.

**Use when:** scene layers already have a coherent spatial order and crossings can guide focus.

**Build:** declare z-order and transition points; use masks or duplicate visual proxies only where needed; keep interactive DOM ownership clear; synchronize scale and speed with implied depth.

**Continuity:** occluding edges and trajectories show spatial relationship.

**Avoid:** accidental clipping, unreadable text behind decoration, excessive duplicated nodes, or z-index escalation. Reduced motion preserves the final layered composition without crossings.
