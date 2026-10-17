## Description:

Guides e-commerce image edits that replace a model, a background, or both while aiming to preserve the original garment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use this skill to prepare prompts and generation commands for product photos featuring different models or settings while keeping the garment consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts are sent to the configured image provider.

Mitigation: Use only images and prompts approved for sharing, select intended input paths, and use dry-run when available.

Risk: Edited photos could suggest a real person's endorsement or target demographic groups without appropriate consent.

Mitigation: Avoid misleading real-person portrayals and review demographic requests for consent and platform compliance.

Risk: Generated images may alter garment details or introduce visual artifacts.

Mitigation: Inspect the product, pose, hands, and lighting before publishing edited images.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy provider](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with image-editing prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A configured image provider may save generated images to user-selected paths; review results for garment fidelity.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
