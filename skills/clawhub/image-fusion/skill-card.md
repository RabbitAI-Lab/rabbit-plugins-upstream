## Description:

多单品融合成一整套 Look。最多 8 张单品图 → 同一模特身上的完整搭配商拍图，每件单品保真。当用户说「多件搭配」「融图」「组一套 look」「搭配图」「几件衣服合成一张」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商团队与商品内容创作者，将最多 8 张单品图组合成同一模特穿着的一套搭配商品图；可指定模特、姿势与场景，并为未提供的服饰补齐搭配。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images may be sent to external image services without a clear privacy disclosure; some components were only partially inspected.

Mitigation: Review provider data handling before use, and avoid identifiable or confidential images unless transfer is approved and consent is in place. Treat behavior in uninspected components as unknown.

## Reference(s):

- [模型参数参考](references/model-flags.md)
- [后端调用参考](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/image-fusion)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance with shell command examples; generated product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Combines up to 8 product images, with optional pose and model references; image output size, resolution, batch count, and save path can be specified.]

## Skill Version(s):

1.0.32 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
