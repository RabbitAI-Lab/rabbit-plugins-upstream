## Description:

一张商品图裂变成整套素材。商品图 + 卖点 → 多角度多场景成套图，够铺满一屏。当用户说「裂变套图」「一张变一屏」「凑够详情页」「出一套图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营者和设计人员可根据一张商品图及商品卖点，制作同一商品的多角度、多场景套图，用于商品主图和详情页素材。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to an external image service, and the scan found no disclosure about that transfer.

Mitigation: Avoid sending confidential material and review the selected provider's data handling terms before use.

Risk: Some bundled components were only partially inspected, so their behavior remains unevaluated.

Mitigation: Review the skill and its bundled components before use, and limit execution to trusted environments.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/fission-pattern)

## Skill Output:

**Output Type(s):** [Image files, Prompt text, Shell commands]

**Output Format:** [Generated raster images (JPEG by default), with prompt text and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A variable-length set of product images; generation uses a configured external image service.]

## Skill Version(s):

1.0.32 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
