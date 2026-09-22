## Description:

已有模特图换模特、换背景，一张模特图生成多人群多场景版本，同时保持商品本身不变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce marketers, operators, and creative production teams use this skill to turn one existing model or mannequin product photo into market-specific catalog variants by changing the model, background, or both while keeping the garment unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model likenesses, prompts, and referenced image URLs are sent to the selected AI provider.

Mitigation: Use approved provider accounts, avoid sensitive or unlicensed inputs, and confirm consent for model likenesses and product imagery before generation.

Risk: Generated model or background variants can be misused for deceptive likeness, endorsement, or demographic-targeting claims.

Mitigation: Do not use the skill for specific-person face swaps or fake endorsements, and review demographic-targeting requests for consent and compliance before publishing assets.

Risk: Generated outputs can drift from the source garment or introduce visual defects such as changed product details, misaligned fit, hand artifacts, or mismatched lighting.

Mitigation: Review outputs before publication, checking product color, cut, logos, folds, fit, hands, and lighting; regenerate or adjust prompts when details drift.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)
- [provider-cli.md](references/provider-cli.md)
- [model-flags.md](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline bash commands; generated assets are saved as image files through the selected AI provider.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompts plus one or more image inputs; supports provider selection, dry runs, batch generation, and local save paths.]

## Skill Version(s):

1.0.11 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
