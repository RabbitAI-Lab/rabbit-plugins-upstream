## Description:

当用户需要归纳商品评价中的优缺点、购买顾虑和改进建议时使用。支持各平台提供的评价文本或表格，也可通过小红书商品链接或sku_id在线分析评价。输出带原话依据、评价条数与范围说明的主题表；已有资料可直接分析。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

用户可提供商品评价文本或表格，或在授权在线访问时提供小红书商品链接或 sku_id。该技能归纳评价主题、原话证据、样本范围与局限，并给出有依据的改进建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI is fetched from the mutable @latest package tag and could change or be compromised in a way that exposes configured credentials.

Mitigation: Review the package release before online use, prefer a reviewed pinned version where supported, and use a credential with only the access needed; use supplied review files when online access is not needed.

Risk: The security analysis was partial because three local references could not be resolved.

Mitigation: Review the unresolved references and complete the security scan before relying on it as a full assessment.

## Reference(s):

- [ClawHub release](https://clawhub.ai/devinchen2014/skills/ecommerce-review-insights)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown report with a sample summary, themed review table, short cited excerpts, limitations, and prioritized recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the analyzed sample size and scope; preserves review row numbers or IDs where available; distinguishes observed sample mentions from population-wide rates.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
