## Description:

商品换背景。白底商品图 → 逼真场景图，光影与投影匹配新环境。当用户说「换背景」「加场景」「白底转场景」「放到桌面上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and product-content creators use this skill to turn white-background product photos into realistic lifestyle scenes while keeping the product visually consistent. It provides scene-selection and image-generation guidance, plus commands for generating and reviewing image variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts are sent to a cloud image provider for processing.

Mitigation: Choose the provider explicitly and submit only images you are permitted to share with it.

Risk: API credentials may be exposed if stored or handled insecurely.

Mitigation: Protect provider API keys and avoid placing secrets in prompts or shared command history.

Risk: Image generation and third-party CLI packages can incur costs or introduce supply-chain risk.

Mitigation: Use --dry-run to check routing and estimated cost, and pin any CLI package you install.

## Reference(s):

- [Model flags](artifact/references/model-flags.md)
- [Provider CLI guide](artifact/references/provider-cli.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/item-change-background)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated product-scene images or image URLs, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The product is intended to remain visually consistent while its background and scene lighting are changed; batch image variants are supported.]

## Skill Version(s):

1.0.25 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
