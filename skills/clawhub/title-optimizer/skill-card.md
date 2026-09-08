## Description:

基于 Amazon 商品详情与评论证据，诊断标题信息缺口并提出优化建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to review product detail and review evidence for an ASIN, then receive title optimization recommendations with supporting rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access ARI account data, consume credits, export reports or reviews, and change monitoring or confirmation settings beyond title-only advice.

Mitigation: Install it only for intended ARI operations workflows, keep auto-confirm limits conservative, and verify costs before enabling recurring monitoring or paid analyses.

Risk: Generated title recommendations can be incorrect, incomplete, or misleading if product fields, review samples, or time windows are limited.

Mitigation: Review the data scope and supporting review evidence before applying recommendations to an Amazon listing.

Risk: Custom ARI endpoint settings can redirect API-key-bearing requests if configured incorrectly.

Mitigation: Use the official ARI endpoint unless the operator controls the HTTPS endpoint and intentionally enables the custom-base allow flag.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/title-optimizer)
- [Amazon 标题优化建议 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text responses with optional shell commands and API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations may consume credits and must follow server quote, confirmation, and auto-confirm rules.]

## Skill Version(s):

1.4.8 (source: frontmatter, CHANGELOG, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
