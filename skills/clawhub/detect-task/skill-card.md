## Description:

投前 AI 图真实性质检。待检图 → 风险等级 + 8 项逐条判定 + 可直接追加到 prompt 的修正句，可自动重跑直到达标。当用户说「投前检测」「图片质检」「检查有没有崩」「上架前把关」「这图能不能用」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员可用它审核 AI 生成的商品图，查看风险等级、8 项检查结论和投放建议，并取得可追加到生成提示词中的修正句。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a mismatch between the stated image-checking purpose and some capabilities, and its scan was incomplete (7 of 12 components fully scanned).

Mitigation: Review the skill behavior before relying on it for automated or batch listing decisions, and have a person check each report.

Risk: The security guidance calls out that images may be sent to external services.

Mitigation: Before submitting an image, confirm that sending it to the selected provider is acceptable.

## Reference(s):

- [Provider CLI and data flow](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with a risk level, eight-item assessment, listing recommendation, and prompt corrections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One report per image or image batch; prompt corrections may be in English.]

## Skill Version(s):

1.0.33 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
