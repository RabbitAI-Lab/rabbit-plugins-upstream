# Three.js and WebGL Integration

## Decision rule

Use WebGL only when at least one central requirement needs true perspective/occlusion, mesh deformation, particles at scale, shaders, post-processing, lighting/material response, or a navigable 3D scene. A simple parallax composition, masked video, image distortion, or 2.5D depth often belongs in DOM/CSS/GSAP.

Estimate the cost of the 3D choice: bundle and asset weight, shader complexity, texture memory, battery, accessibility, fallback, lifecycle, and team maintainability. If the same concept survives without WebGL, prefer the simpler implementation.

## Architecture

Use one renderer/canvas per continuous world when possible. Separate scene state from render objects. Drive a small set of normalized parameters from GSAP rather than scattering scroll reads through the render loop.

Define pixel-ratio caps, resize behavior, texture formats/sizes, color space, camera near/far planes, visibility pausing, context-loss handling, and resource disposal. Dispose geometries, materials, textures, render targets, controls, and listeners.

## Composition with DOM

Choose which layer owns text, interaction, and accessibility; usually DOM should. Synchronize camera/object anchors with DOM only when the relationship is stable across breakpoints. Use occlusion and pointer events deliberately.

## Fallback

Provide a poster, video, static composition, or DOM alternative for reduced motion, unsupported contexts, data-saving conditions, and constrained devices. Fallback must carry the same message and action.
