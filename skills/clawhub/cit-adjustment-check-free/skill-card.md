## Description:

企业所得税纳税调整表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 企业所得税纳税调整核对、企业所得税纳税调整表对不上。本免费版只执行 6 项，即 应纳税所得额复算、调增/调减合计 = 各明细项之和复算、合计行逐列复核等。不执行 5 项判定，例如 业务招待费超限额未足额调增提示。详见 SKILL.md 的「这个免费版不包含」一节。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax staff use this skill before annual Chinese enterprise income tax filing to check a provided tax adjustment table for deterministic arithmetic, reconciliation, duplicate-item, blank-placeholder, and negative-amount issues. It reports source-cited findings and withholds conclusions when the input is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the free checker for complete tax advice or a filing-system integration.

Mitigation: Review the free-version limitations before use and treat results as local table checks that still require professional tax review.

Risk: The free version does not perform several tax-law limit checks, including business entertainment, advertising and promotion, charitable donation, negative taxable income, and tax-rate deviation checks.

Mitigation: Use the omitted-check notices to identify checks not performed and review those items separately under applicable tax rules.

Risk: Insufficient or malformed input can prevent a reliable conclusion.

Mitigation: Provide the full enterprise income tax adjustment table with recognizable headers; when the skill reports insufficient input, supply the missing material instead of relying on a no-issue conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cit-adjustment-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON results with source-cited findings, scope metadata, and omitted-check notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided input; material that cannot be parsed yields an insufficient-input result rather than a tax conclusion.]

## Skill Version(s):

1.0.60 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
