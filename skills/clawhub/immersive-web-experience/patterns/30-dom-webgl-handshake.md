# DOM–WebGL Handshake

Synchronize accessible DOM content and controls with objects in a continuous WebGL world.

**Use when:** real 3D is justified but text, navigation, and interaction should remain semantic DOM.

**Build:** choose one source of scene state; project stable 3D anchors to screen coordinates or drive both layers from shared normalized parameters; define occlusion, pointer ownership, resize, camera, and z-order; pause/dispose rendering correctly.

**Continuity:** DOM labels/actions and rendered objects share identity and timing.

**Avoid:** per-frame layout thrashing, fragile pixel matching, duplicated interaction targets, and canvas-only content. Reduced motion can freeze representative 3D poses while DOM scenes remain fully usable.
