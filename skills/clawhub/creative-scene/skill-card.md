## Description:

Generates original scenes from a description or edits a reference image to change a model, pose, or outfit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and ecommerce teams use this skill to make scene images from text and refine a reference image's model, pose, or clothing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to the configured image provider.

Mitigation: Do not include private images, secrets, or internal URLs; confirm the provider before sending inputs.

Risk: Image generation may incur charges.

Mitigation: Use dry-run or confirm expected costs before billable generations.

## Reference(s):

- [Creative Scene on ClawHub](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider setup and output guide](artifact/references/provider-cli.md)
- [Image model parameters](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Text prompts and CLI commands; generated JPEG images when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-only generation and reference-image edits.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
