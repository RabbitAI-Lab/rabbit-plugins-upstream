# Route Scene Bridge

Carry a selected object or composition across navigation so routes feel like connected places.

**Use when:** list-to-detail, chapter-to-chapter, or object-focused navigation benefits from continuity.

**Build:** preserve semantic navigation/history; capture outgoing geometry/state; coordinate route readiness with transition; use the platform View Transitions API, GSAP Flip, or a temporary proxy based on project support; set timeout/failure recovery and restore focus appropriately.

**Continuity:** selected object, title, crop, or color becomes the next route's anchor.

**Avoid:** delaying navigation for ornamental motion, breaking deep links, or leaving overlays after errors. Reduced motion navigates immediately with correct focus.
