## Description:

Creates on-model images of shoes, bags, and accessories from product and model reference photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and product marketers use product photos and model references to create realistic images of accessories being worn or carried.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model photos and prompts are sent to the selected cloud image provider.

Mitigation: Confirm the provider with --dry-run or --provider before sending images; avoid private portraits.

Risk: The skill uses image-provider credentials from the environment or local configuration.

Mitigation: Keep credentials private and use only a provider account you trust.

Risk: Generated images could depict people or products without permission or suggest a false endorsement.

Mitigation: Use only images you have rights to modify, obtain model consent, and avoid fabricated endorsements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider and credential guide](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and CLI commands; generated JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multiple product views and batch generation; images require visual review for placement and fidelity.]

## Skill Version(s):

1.0.20 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
