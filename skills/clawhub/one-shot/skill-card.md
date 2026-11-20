## Description:

已有模特图换模特、换背景。一张模特图 → 多人群多场景版本，商品本身不变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use this skill to create audience and scene variations from an existing model or mannequin product photo while aiming to preserve the garment. It provides prompts and commands for changing the model, background, or both.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source and reference photos may be sent to an external image provider during generation.

Mitigation: Before uploading, confirm you have permission to use the photos and review the selected provider's data handling terms.

Risk: The security review reports incomplete coverage and calls out missing tool scope and an inconsistent example.

Mitigation: Review the commands and provider scope before execution, and inspect generated images before using them in a product listing or campaign.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/one-shot)
- [Image model parameters](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Edited image files (JPEG, PNG, or WebP), with CLI commands and image-editing prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may not preserve every garment detail; inspect the product, alignment, hands, and lighting before use.]

## Skill Version(s):

1.0.33 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
