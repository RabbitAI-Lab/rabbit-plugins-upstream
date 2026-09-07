# Scroll-Controlled Camera

Map scroll progress to a designed camera path through a spatial scene.

**Use when:** traversal, inspection, or approach is the central experience and true depth matters.

**Build:** author camera key poses and targets; interpolate a normalized progress parameter via GSAP; keep the render loop independent of raw scroll events; tune near/far planes and target visibility. DOM can simulate simple camera moves with perspective; use Three.js for true geometry/occlusion.

**Continuity:** landmarks and a stable path maintain orientation.

**Avoid:** free-form camera drift, surprise rotation, long passages without readable change, and essential content inside canvas. Reduced motion presents selected viewpoints as discrete scenes.
