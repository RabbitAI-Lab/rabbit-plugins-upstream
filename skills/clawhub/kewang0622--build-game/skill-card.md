## Description:

Generate and iteratively develop polished 3D browser games from natural language. Supports any genre (FPS, RPG, racing, platformer, tower defense, etc.), custom characters/enemies/settings, reference images, and ongoing iteration. Outputs a single playable HTML file using Three.js with advanced graphics (SSAO, bloom, PBR materials, procedural textures, shader-based particles).

This skill is ready for commercial/non-commercial use.

## Publisher:

[kewang0622](https://clawhub.ai/user/kewang0622)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to turn natural-language game ideas or iteration requests into playable single-file Three.js browser games with procedural assets, HUDs, controls, audio, and local serving. It supports ongoing changes to an existing generated game while tracking progress and implementation state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated games may be published to a public here.now URL, exposing embedded assets, prompts, and build metadata.

Mitigation: Publish only when sharing is intended; avoid private images and sensitive prompts unless publication is disabled or explicitly approved.

Risk: The local server helper uses a shared PID file under /tmp, which can affect unrelated same-user processes in shared environments.

Mitigation: Review the running process before stopping or restarting the helper, or use a dedicated local server command for sensitive shared systems.

## Reference(s):

- [3D Game Builder on ClawHub](https://clawhub.ai/kewang0622/skills/build-game)
- [Three.js Engine Patterns](reference/engine-patterns.md)
- [Advanced 3D Graphics Quality Patterns](reference/graphics-quality.md)
- [Procedural Asset Recipes](reference/procedural-assets.md)
- [Complex Game Systems Reference](reference/game-systems.md)
- [GUI / HUD Design Patterns](reference/gui-patterns.md)
- [Procedural Audio Recipes](reference/audio-patterns.md)
- [Three.js module import](https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js)
- [Three.js addons import](https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/)

## Skill Output:

**Output Type(s):** [Code, Files, Markdown, Shell commands, Guidance]

**Output Format:** [Single HTML game file, Markdown progress notes, local and public URLs, and a concise gameplay summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes generated games under /tmp/game-build, serves them on localhost, and may publish the generated files to a public here.now URL.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
