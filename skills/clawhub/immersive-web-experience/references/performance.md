# Performance

Set a budget from the audience and target devices before polish. Record assumptions instead of inventing universal numbers.

## Measure

Inspect frame time and long tasks during the heaviest passage; startup and route transition cost; JavaScript and asset transfer; decoded image/texture memory; layout shifts; number of active triggers/listeners; and idle CPU/GPU use.

## Priorities

1. Reduce work and assets.
2. Animate compositor-friendly properties.
3. Avoid forced synchronous layout and per-frame DOM querying.
4. Cap canvas resolution and rendering complexity.
5. Pause offscreen, background-tab, and completed work.
6. Load later-scene assets just before they are needed without causing visible gaps.

Compress images/video, size media correctly, subset fonts, avoid duplicate libraries, and reserve dimensions. In WebGL, compress textures, minimize overdraw, reuse geometry/materials, and reduce draw calls where evidence shows a bottleneck.

Do not accept average FPS alone. Inspect worst passages, dropped frames during input, thermal behavior, and repeated navigation. Performance is part of the art direction: simplify the effect while preserving its perceptual purpose.
