## Description:

Turns product and model reference photos into on-model images of shoes, bags, and accessories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use this skill to place product photos of shoes, bags, and accessories onto a model reference image for realistic merchandising visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model images, prompts, and related metadata are sent to the selected image-generation provider.

Mitigation: Review the selected provider and its data practices before submitting sensitive or personal images.

Risk: Image generation can consume paid credits.

Mitigation: Use --dry-run to review requests and estimated costs before generating images.

Risk: Real people's images could be misused for impersonation or unauthorized endorsement.

Mitigation: Use model images only with appropriate permission and avoid misleading endorsements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider and CLI reference](references/provider-cli.md)
- [Model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated product images locally; optional JSON reports include saved paths and estimated credits.]

## Skill Version(s):

1.0.23 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
