## Description:

Conceive, build, or review cinematic and spatial web experiences organized as connected scenes, using GSAP as the default motion layer and Three.js/WebGL only when real 3D or shader rendering materially improves the concept.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cbbathaglini](https://clawhub.ai/user/cbbathaglini)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to plan, implement, or review immersive landing pages, portfolios, launches, editorials, interactive stories, and experiential product sites. It guides scene-based experience concepts, transition design, motion systems, GSAP implementation, optional WebGL decisions, accessibility, performance, and final immersion review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead to user-directed frontend code changes for animation-heavy experiences.

Mitigation: Review proposed code changes, shell commands, and dependency additions before applying them in a project.

Risk: Optional WebGL, shader, or Three.js work can add performance, fallback, and maintainability risk.

Mitigation: Require explicit justification for WebGL, cap rendering cost, provide DOM or static fallbacks, and verify cleanup of GPU resources.

Risk: Pinned scenes, scroll choreography, parallax, and camera movement can impair accessibility or trap interaction when implemented poorly.

Mitigation: Preserve semantic DOM order, keyboard access, visible focus, reduced-motion behavior, and non-trapping scroll/focus paths.

Risk: Motion and media-heavy scenes can degrade frame stability, memory use, and mobile battery life.

Mitigation: Measure heavy passages on representative devices, reduce asset and layout work, pause offscreen rendering, and simplify effects that miss budget.

## Reference(s):

- [Experience Design Principles](references/experience-design.md)
- [Visual Direction](references/visual-direction.md)
- [Immersion Levels](references/immersion-levels.md)
- [Scene Architecture](references/scene-architecture.md)
- [Transition Design](references/transition-design.md)
- [Motion Language](references/motion-language.md)
- [GSAP Engineering](references/gsap-engineering.md)
- [Three.js and WebGL Integration](references/webgl-integration.md)
- [Accessibility and Inclusive Motion](references/accessibility.md)
- [Performance](references/performance.md)
- [Anti-patterns](references/anti-patterns.md)
- [Pattern Library](patterns/index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with possible code edits, shell commands, configuration notes, and structured review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce experience concepts, scene maps, motion systems, implementation notes, and immersion review findings scaled to the user's request.]

## Skill Version(s):

1.0.0 (source: server release evidence, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
