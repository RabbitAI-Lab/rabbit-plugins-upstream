## Description:

归纳商品评价中的优缺点、购买顾虑和改进建议，并以原话依据、样本条数和范围说明呈现结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

商品运营人员可用此技能分析已有评价文本或表格，也可在线读取小红书商品评价，以了解实际出现的主题、购买顾虑和改进方向。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online queries use a SocialDataX API key and may consume paid credits.

Mitigation: Use online queries only when needed, keep the API key in its environment variable, and monitor credit usage. Supplied review text can be analyzed offline.

Risk: The command examples use a CLI package that can access local files and secrets available to its process.

Mitigation: Prefer a reviewed, pinned CLI version and limit its access to unrelated files and secrets.

## Reference(s):

- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summary with a review-theme table, cited review excerpts, sample counts, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sample scope and data limitations when available; findings are grounded in supplied or retrieved reviews.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
