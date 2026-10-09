## Description:

Helps create e-commerce photo variations by changing a model, background, or both while aiming to preserve the pictured product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce merchants and creative teams use this skill to make variations of existing apparel model or mannequin photos for different audiences and settings without intentionally changing the product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted photos and prompts are sent to the selected cloud image provider.

Mitigation: Use dry-run first, choose the provider deliberately, and do not submit private local images or prompts you are unwilling to share.

Risk: Demographic targeting or watermark removal may be inappropriate without permission or a compliant purpose.

Mitigation: Avoid these uses unless you have consent, rights, and a compliant business purpose.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider and CLI reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and shell commands; edited product photos saved as image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated photos for product fidelity, hands, and lighting before use.]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
