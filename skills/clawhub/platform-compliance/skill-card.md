## Description:

上架前平台合规校验与自动修复。待上架图 → Amazon / TikTok Shop / Temu / Shopee / 淘宝 各平台的通过或驳回风险报告，可一键修成合规图。当用户说「会不会被驳回」「合规检查」「白底不达标」「主图规格」「传上去被拒」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商卖家和运营人员可用此技能检查商品图片是否符合目标平台的可机检上架规格，并在需要时自动修复白底、主体占比、分辨率或文件体积问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 检查与生成流程可能调用外部图像服务并传送输入图像或提示词。

Mitigation: 仅使用符合你数据处理要求的服务；不要提交敏感图像或提示词，除非你接受其处理方式。

Risk: 安全扫描指出工具权限范围不清晰，且仅完整扫描了部分组件。

Mitigation: 启用前核查实际授予的工具和权限，并先用非敏感输入验证运行行为。

## Reference(s):

- [平台图片规格（可机检子集）](references/platform-specs.md)
- [后端调用参考](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands, Files]

**Output Format:** [合规检查文本报告；按请求可生成修复后的图片文件]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [支持单张或批量图片，并可指定平台及自定义规则。]

## Skill Version(s):

1.0.33 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
