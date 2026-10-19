## Description:

Reviews AI-generated e-commerce images before publication and provides an eight-point risk assessment, a placement recommendation, and prompt-ready corrections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and reviewers use the skill to assess generated product images for visual defects and potential listing issues before publication, then decide whether to publish, retouch, or regenerate them. Human review remains necessary before listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to a configured cloud provider.

Mitigation: Review data-sharing requirements and select the provider explicitly; use a dry run before submitting sensitive material.

Risk: The bundled automation can regenerate images, rewrite prompts, rerun tasks, or modify image files beyond a simple inspection.

Mitigation: Avoid the automated run loop and image-fix option unless those changes are intended; review proposed changes and preserve originals.

Risk: Visual judgments and platform-compliance checks can miss defects or flag acceptable images.

Mitigation: Manually review findings and verify current platform requirements before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/detect-task)
- [Example quality-control report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown report; optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk tier, eight pass/fail findings with evidence, publication recommendation, and up to three English prompt corrections when needed. Optional automation can regenerate or modify image files.]

## Skill Version(s):

1.0.24 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
