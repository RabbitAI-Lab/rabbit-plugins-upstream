## Description:

Builds, redesigns, and critiques presentation-grade .pptx slide decks using planning, design, rendering, linting, and critic-review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, educators, and business users use this skill to plan, generate, redesign, and review slide decks while preserving source fidelity, matching audience needs, and producing editable PowerPoint deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags broad local execution and file-write authority for rendering decks and creating reusable build artifacts.

Mitigation: Run the skill in a trusted workspace, review generated Python or shell commands before execution, and inspect output folders before sharing deliverables.

Risk: The skill can contact hosted image or version services and may prompt for updates.

Mitigation: Review update prompts before accepting them, keep a single version for a deck build, and avoid generated-image paths for sensitive material unless the session and API data flow are acceptable.

Risk: Optional style-preference persistence can retain user taste signals beyond a single deck.

Mitigation: Use persistence only with explicit user consent and avoid storing confidential project, client, or source-material details in preference records.

Risk: Generated or sourced visual assets can introduce licensing, factuality, or privacy issues in final slides.

Mitigation: Use trusted source material, record image origins and licenses, reject watermarked or unidentified assets, and verify sensitive imagery is de-identified before delivery.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dong845/skills/slide-maker)
- [Project Details Link](https://github.com/addsumtech/slides_maker)
- [Design Principles](references/design-principles.md)
- [Review Rubrics](references/review-rubrics.md)
- [Deck Setup](references/deck-setup.md)
- [Image Generation](references/image-generation.md)
- [Runtime Routing](references/runtime-routing.md)
- [Codex Runtime](references/codex-runtime.md)
- [Hand-off and Iteration](references/handoff-and-iteration.md)
- [Troubleshooting FAQ](references/troubleshooting-faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus generated Python, PPTX, asset, render, lint, and review artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local deck folders, reusable build scripts, rendered previews, quality-gate outputs, and optional style-preference records.]

## Skill Version(s):

4.6.0 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
