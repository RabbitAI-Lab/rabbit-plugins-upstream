## Description:

投前 AI 图真实性质检。待检图 → 风险等级 + 8 项逐条判定 + 可直接追加到 prompt 的修正句，可自动重跑直到达标。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员和创作者可在投放或上架前检查 AI 生成的商品图片，查看风险等级、8 项检查结果和投放建议，并取得可用于重跑生成的 prompt 修正句。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports a suspicious purpose mismatch with medium confidence, and the analysis is incomplete.

Mitigation: Review the skill's behavior and its reports before relying on recommendations for a publishing or advertising decision; do not treat the assessment as proof that the skill is safe.

Risk: Images and prompts may be handled externally, and unreadable images may still produce a successful exit status.

Mitigation: Avoid submitting sensitive images or prompts unless the provider's data handling is acceptable, and check that each image was actually readable and assessed before accepting a result.

## Reference(s):

- [Provider CLI guide](artifact/references/provider-cli.md)
- [Model flags](artifact/references/model-flags.md)
- [Platform specifications](artifact/references/platform-specs.md)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/detect-task)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Prompt text]

**Output Format:** [Chinese Markdown report with a risk level, eight itemized checks, a deployment recommendation, and optional English prompt correction sentences]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One report per submitted image; the skill describes an optional rerun loop.]

## Skill Version(s):

1.0.36 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
