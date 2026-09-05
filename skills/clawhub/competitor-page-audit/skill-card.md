## Description:

审查主 ASIN 与已授权竞品商品页的字段完整度、表达一致性和评论证据，输出对照问题清单，不用于实时价格、销量、库存、广告、订单或真实退货率判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to audit a primary ASIN against authorized competitor pages, checking field completeness, expression consistency, review evidence, and listing improvement opportunities before taking action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes paid analysis, exports, account workflow changes, and recurring monitoring beyond narrow page auditing.

Mitigation: Review paid commands, auto-confirm behavior, schedule/watch features, export paths, and account workflow changes before use; avoid enabling monitoring or autoconfirm unless explicitly intended.

Risk: The skill requires access to an ARI account through an API key.

Mitigation: Use the documented setup flow or ARI_API_KEY environment variable, keep the key out of reports and command examples, and review local API-key storage before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-page-audit)
- [README](artifact/README.md)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI API Reference](artifact/references/reference.md)
- [ARI Web Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise guidance with CLI commands and URLs when returned by ARI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report IDs, report URLs, sample counts, credit use, and balance when returned by ARI; requires an ARI API key.]

## Skill Version(s):

1.4.5 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
