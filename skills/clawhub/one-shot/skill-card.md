## Description:

This skill helps agents use dLazy image editing to replace the model, background, or both in an existing ecommerce model or mannequin photo while preserving the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams and agents use this skill to turn a single finished product photo into market-specific model and background variants. It is suited for model replacement, background replacement, mannequin-to-human conversion, and multi-audience catalog image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product photos and prompts are sent to dLazy's hosted service, and generated outputs may be hosted on files.dlazy.com.

Mitigation: Review the data being uploaded before use, avoid sensitive or unauthorized images, and use the service only when hosted processing is acceptable.

Risk: Changing model demographics or presentation can create unlawful, discriminatory, or misleading ecommerce imagery.

Mitigation: Use the skill only with rights to the source material, check that edits are lawful and non-discriminatory, and do not present generated models as real endorsements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/one-shot)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted image URLs and optionally save generated image files through the dLazy CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
