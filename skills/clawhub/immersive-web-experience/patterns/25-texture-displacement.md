# Texture Displacement

Distort or displace media as if one material transforms into another.

**Use when:** fluidity, heat, refraction, fabric, terrain, or another material behavior is central to the concept and cannot be expressed by a mask.

**Build:** use a WebGL shader with bounded amplitude, compressed textures, stable UV mapping, and a normalized GSAP-driven parameter. Maintain a DOM image/poster fallback and dispose GPU resources.

**Continuity:** shared image features remain traceable through the distortion.

**Avoid:** adding displacement as a prestige hover, excessive motion near text, and unbounded pixel ratio. Prefer CSS/SVG masks for simple reveals; disable under reduced motion.
