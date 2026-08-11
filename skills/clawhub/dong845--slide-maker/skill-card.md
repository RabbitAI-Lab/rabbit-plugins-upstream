## Description:

Builds, redesigns, and critiques presentation-grade PowerPoint slide decks with structured planning, design gates, rendering checks, and critic review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, educators, and business users use this skill to turn source material, existing decks, or rough ideas into presentation-ready .pptx decks and to review or redesign slides for a target audience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run local Python and rendering tools while creating deck artifacts on the user's machine.

Mitigation: Install only when the source is trusted, review generated commands before execution, and scan the skill before deployment.

Risk: The skill can fetch web assets for icons, images, and verification workflows.

Mitigation: Review network-dependent steps, prefer license-clear or user-provided assets, and keep image licenses and credits visible in the delivery record.

Risk: Supplied style.py or section_*.py files are executable code, not ordinary slide content.

Mitigation: Treat these files as code: inspect them before running and avoid executing files from untrusted decks or templates.

Risk: Self-update and persistent template or taste registry behavior can affect future deck builds.

Mitigation: Decline or defer self-updates unless the source is trusted and local changes are understood; keep registry writes user-visible and reversible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dong845/skills/slide-maker)
- [Design Principles](references/design-principles.md)
- [Content Plan Specification](references/content-plan-spec.md)
- [Review Rubrics](references/review-rubrics.md)
- [File Inventory](references/file-inventory.md)
- [User Taste Registry](references/user-taste.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with Python build code, shell commands, JSON review records, and generated .pptx, PDF, PNG, or HTML deck artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create deck folders under Downloads, render slides, fetch web assets, and maintain an optional slide-preference or template registry.]

## Skill Version(s):

4.8.0 (source: target metadata, server release, artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
