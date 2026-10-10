## Description:

Creates images from a text description and optionally edits a reference image to change the model, pose, or outfit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and e-commerce teams use this skill to draft scene images from descriptions or revise a reference image's model, pose, or clothing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to the selected cloud image provider.

Mitigation: Do not supply sensitive local files, private URLs, credentials, or internal network resources as inputs; review the selected provider before use.

Risk: Image generation can incur unexpected charges or use an unintended provider.

Mitigation: Use dry-run or explicitly select the provider when cost or destination matters.

Risk: Generated images could be mistaken for authentic portraits or product photography.

Mitigation: Do not generate specific real-person portraits or misrepresent generated product images as real photos or customer experiences.

## Reference(s):

- [Creative Scene on ClawHub](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPG/PNG images and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference-image edits and optional local image saves.]

## Skill Version(s):

1.0.19 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
