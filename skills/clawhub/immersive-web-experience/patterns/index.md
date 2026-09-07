# Pattern Library

Select patterns from scene meaning and continuity needs, not novelty. Combine a small compatible set; do not attempt to use the whole catalog.

| # | Pattern | Best for | Default stack |
|---|---|---|---|
| 01 | [Pinned stage](01-pinned-stage.md) | transforming one composition through beats | GSAP + ScrollTrigger |
| 02 | [Sticky handoff](02-sticky-handoff.md) | transferring attention between adjacent scenes | CSS sticky + GSAP |
| 03 | [Horizontal world](03-horizontal-world.md) | genuinely lateral chapters or journeys | GSAP + ScrollTrigger |
| 04 | [Zoom passage](04-zoom-passage.md) | entering detail or changing scale | GSAP; Three.js if true 3D |
| 05 | [Portal aperture](05-portal-aperture.md) | threshold into a new world | GSAP masks; optional WebGL |
| 06 | [Morph transition](06-morph-transition.md) | semantic shape transformation | GSAP/SVG; WebGL for mesh |
| 07 | [Object continuity](07-object-continuity.md) | one object across scenes | GSAP |
| 08 | [FLIP relay](08-flip-relay.md) | same DOM identity across layouts | GSAP Flip |
| 09 | [Layered parallax](09-layered-parallax.md) | restrained 2.5D depth | GSAP + CSS perspective |
| 10 | [Scroll camera](10-scroll-camera.md) | deliberate spatial traversal | GSAP + Three.js when real 3D |
| 11 | [Spatial navigation](11-spatial-navigation.md) | non-linear places or chapters | GSAP; optional Three.js |
| 12 | [Foreground wipe](12-foreground-wipe.md) | motivated occlusion | GSAP/CSS |
| 13 | [Background migration](13-background-migration.md) | world continuity behind content | GSAP/CSS |
| 14 | [Mask reveal](14-mask-reveal.md) | directed image/text exposure | GSAP/CSS/SVG |
| 15 | [Clip-path iris](15-clip-path-iris.md) | focused aperture reveal | GSAP/CSS |
| 16 | [Typography relay](16-typography-relay.md) | phrase/object carrying meaning | GSAP + Flip/SplitText |
| 17 | [Kinetic text field](17-kinetic-text-field.md) | display type as environment | GSAP/SplitText |
| 18 | [Image-sequence scrub](18-image-sequence-scrub.md) | authored frame-by-frame transformation | Canvas + ScrollTrigger |
| 19 | [Scroll assembly](19-scroll-assembly.md) | explaining parts or construction | GSAP + ScrollTrigger |
| 20 | [Layered occlusion](20-layered-occlusion.md) | depth through crossings | GSAP/CSS |
| 21 | [Scale tunnel](21-scale-tunnel.md) | repeated frames as spatial passage | GSAP; optional Three.js |
| 22 | [Gallery conveyor](22-gallery-conveyor.md) | continuous visual catalog | GSAP/Draggable optional |
| 23 | [Sticky stack transform](23-sticky-stack-transform.md) | cumulative state/history | CSS sticky + GSAP |
| 24 | [Light and color passage](24-light-color-passage.md) | atmospheric chapter change | GSAP/CSS; WebGL for lighting |
| 25 | [Texture displacement](25-texture-displacement.md) | material image transition | WebGL/shader, justified |
| 26 | [Shader dissolve](26-shader-dissolve.md) | organic transformation of rendered media | WebGL/shader, justified |
| 27 | [Particle convergence](27-particle-convergence.md) | many units forming meaning | Three.js/WebGL |
| 28 | [Route scene bridge](28-route-scene-bridge.md) | continuity across navigation | GSAP + View Transitions/Flip |
| 29 | [Pointer lens](29-pointer-lens.md) | optional exploration/reveal | GSAP/CSS; shader if needed |
| 30 | [DOM–WebGL handshake](30-dom-webgl-handshake.md) | aligning accessible UI with a 3D world | GSAP + Three.js |

For each selected pattern, record its narrative job, owner, fallback, interruption behavior, and budget. Read [GSAP engineering](../references/gsap-engineering.md), and read [WebGL integration](../references/webgl-integration.md) for patterns marked WebGL.
