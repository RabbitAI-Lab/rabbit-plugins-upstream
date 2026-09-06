## Description:

采集 Amazon 热销竞品评论，拆解爆款卖点、差评短板与买家真实需求，输出选品验证、竞品调研、Listing 打磨建议以及星级、趋势和关键词图表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, operators, and market researchers use this skill to collect review data for ASINs and turn it into VOC reports, competitor comparisons, negative-review workflows, keyword ideas, exports, and monitoring guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically spend ARI credits under server-controlled auto-confirm rules and can persist account settings.

Mitigation: Review auto-confirm and autoconfirm behavior before installation; set autoconfirm off when every credit-consuming action should require explicit approval.

Risk: The skill requires an ARI API key, stores the key locally, and makes authenticated calls to ari.funewa.com.

Mitigation: Use it only when comfortable granting ARI account access, keep the key out of reports and shared documents, and revoke or recreate the key if exposure is suspected.

Risk: Analysis is based on collected Amazon review samples and can be misleading when sample size or collection windows are limited.

Mitigation: Label small samples and collection windows clearly, avoid treating single reviews as conclusive, and combine outputs with other business evidence before making decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/hot-review)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports, structured JSON responses, CLI commands, and exported CSV, Markdown, or HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may create account-scoped reports, exports, monitoring settings, and credit-consuming analysis results.]

## Skill Version(s):

1.4.5 (source: server release evidence, frontmatter, _meta.json, and CLI version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
