# Image-Sequence Scrub

Map progress through pre-rendered frames to create an authored transformation or camera move.

**Use when:** photoreal product transformation or controlled footage cannot be recreated efficiently in DOM/3D and every frame matters.

**Build:** size and compress frames, preload a small initial window, draw to a responsive canvas, clamp frame indices, and preserve a poster until ready. Consider video with seeking when it is more efficient; test actual devices.

**Continuity:** the subject remains stable while the rendered state evolves.

**Avoid:** hundreds of oversized frames, blank loading stages, or using a sequence for a simple scale/fade. Reduced motion uses a representative poster or selected keyframes.
