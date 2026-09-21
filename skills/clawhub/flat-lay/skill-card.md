## Description:

服装平铺图一键上身试穿。服装平铺图 + 姿势参考图 → 模特上身商拍图，款式、颜色、织法、版型保持不变。当用户说「平铺图转模特图」「衣服上身」「虚拟试穿」「AI 试衣」「让模特穿上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, creative teams, and agent-assisted catalog workflows use this skill to turn garment flat-lay or on-body source images plus pose references into on-model product photography. It supports single-garment and full-look try-on workflows while preserving garment color, material, cut, and visible details as much as the generation model allows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, model, and reference images may be sent to the selected image-generation provider.

Mitigation: Use the documented dry-run or doctor mode first, choose an approved provider, and only submit images suitable for that provider's data handling terms.

Risk: API keys are required for cloud generation providers and could be misused if overbroad or exposed.

Mitigation: Keep provider keys scoped, revocable, and stored through the documented CLI or environment variable mechanisms rather than embedding them in prompts or outputs.

Risk: Virtual try-on output can misrepresent a person's endorsement or alter garment, body, hand, face, or background details.

Mitigation: Follow the skill's restriction against forged commercial endorsements and review generated images for color, texture, print placement, anatomy, and background changes before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [provider-cli.md](references/provider-cli.md)
- [model-flags.md](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy product site](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with CLI commands and saved image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are typically JPEG images saved to a project path; dry-run and doctor modes support preflight checks.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
