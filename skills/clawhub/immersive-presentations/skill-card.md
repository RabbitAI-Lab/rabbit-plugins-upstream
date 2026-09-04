## Description:

Create cinematic, narrative, interactive web presentations from a topic or briefing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cbbathaglini](https://clawhub.ai/user/cbbathaglini)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, educators, and technical communicators use this skill to turn topics, briefs, research, or technical material into cinematic interactive web presentations, scrollytelling experiences, technical explainers, or implementation-ready presentation plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated web presentations may add frontend code, packages, assets, canvas, WebGL, GSAP motion, or external media that need normal project review.

Mitigation: Review generated code, dependencies, assets, and media before use, and run the same frontend security and quality checks used for the target project.

Risk: Motion-heavy scenes can reduce accessibility or cause discomfort if flashing, camera movement, parallax, or continuous animation is overused.

Mitigation: Require reduced-motion behavior, keyboard-accessible controls, visible focus states, readable labels, sufficient contrast, and avoidance of rapid flashing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cbbathaglini/skills/immersive-presentations)
- [README](artifact/README.md)
- [Narrative Architecture](artifact/references/narrative-architecture.md)
- [Scene System](artifact/references/scene-system.md)
- [Motion And GSAP](artifact/references/motion-and-gsap.md)
- [Interaction And Modes](artifact/references/interaction-and-modes.md)
- [Accessibility, Responsive Design, And Performance](artifact/references/accessibility-responsive-performance.md)
- [Diagrams, Data, And Domains](artifact/references/diagrams-data-and-domains.md)
- [Anti-Patterns And Quality Bar](artifact/references/anti-patterns-and-quality-bar.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown plans, implementation-ready specifications, and web project code or files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include presenter and debug controls, accessibility notes, responsive behavior, concrete implementation notes, and optional GSAP delegation guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
