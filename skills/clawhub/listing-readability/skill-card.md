## Description:

检查 Amazon Listing 的结构、术语、重复表达和评论反映的理解障碍，给出可读性建议；仅用于页面可读性诊断，不用于广告投放、翻译质量认证或自动发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to inspect a product ASIN's Listing readability and review-backed buyer comprehension barriers before updating page content. The skill checks product details and available reviews, obtains a quote for paid report generation, and produces an operations report when the user confirms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is broader than a readability checker and can use ARI account integrations for paid review analysis, monitoring, competitor tracking, and account confirmation settings.

Mitigation: Install only when those ARI operations are intended; review account capabilities, confirmation settings, and monitoring changes before enabling or executing them.

Risk: Some ARI operations can spend credits or trigger future collection costs after user confirmation or account auto-confirm rules.

Mitigation: Require quotes before paid actions, keep auto-confirm limits off or low unless deliberately configured, and verify reported credits, balance, and recurring collection costs.

Risk: The skill requires an ARI API key and sends requests to the ARI service.

Mitigation: Use a scoped, revocable ARI API key, do not paste credentials into chat output, and avoid custom ARI endpoints unless the environment override is explicitly intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/listing-readability)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Listing readability workflow](artifact/references/operation-workflow.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with concise operational guidance and occasional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, report identifiers, credit usage, data scope, and account setup guidance when returned by ARI.]

## Skill Version(s):

1.4.8 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
