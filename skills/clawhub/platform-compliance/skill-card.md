## Description:

上架前平台合规校验与自动修复。待上架图 → Amazon / TikTok Shop / Temu / Shopee / 淘宝 各平台的通过或驳回风险报告，可一键修成合规图。当用户说「会不会被驳回」「合规检查」「白底不达标」「主图规格」「传上去被拒」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商卖家和运营人员可用此技能按目标平台检查商品图片规格，查看通过或驳回风险，并对可修复的尺寸、背景和文件规格问题生成修正版。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unreadable images may pass as successful when the skill's exit status is used to gate compliance in CI.

Mitigation: Avoid relying on its exit status as a CI gate until the reported read-error behavior is addressed.

Risk: The security scan was partial, so some behavior remains unassessed.

Mitigation: Review the partially inspected files and remaining components before relying on the skill.

## Reference(s):

- [Platform Compliance on ClawHub](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Image files, Guidance]

**Output Format:** [Text or JSON compliance reports, plus corrected image files when automatic repair is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-image and batch checks; repaired images are saved as separate files.]

## Skill Version(s):

1.0.31 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
