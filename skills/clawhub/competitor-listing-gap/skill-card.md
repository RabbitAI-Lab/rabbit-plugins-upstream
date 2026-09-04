## Description:

Compares a primary Amazon ASIN with authorized competitor product-page fields, images, and review evidence to identify Listing expression gaps and verifiable improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to run ARI's fixed page_compare/listing_gap workflow for comparing a target ASIN against authorized competitors and turning product-page and review evidence into Listing improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broader ARI account, monitoring, export, and paid-operation authority than a narrow listing-gap comparison may imply.

Mitigation: Install and use it only with an ARI account where that authority is acceptable, and review account, export, monitoring, competitor, and paid-operation access before use.

Risk: Paid or auto-confirmed ARI operations can consume credits under ARI rules.

Mitigation: Verify quote, balance, auto-confirmation status, ASIN, site, and requestId before permitting paid operations or accepting auto-confirmed results.

Risk: The skill can save an ARI API key locally and export reports or reviews to local files.

Mitigation: Use trusted environments, avoid exposing API keys in reports or examples, and handle exported Markdown, HTML, and CSV files as account or product data.

Risk: Monitoring and competitor-setting changes can alter ongoing collection behavior and future costs.

Mitigation: Confirm the target ASIN, competitor relationship, schedule, and cost before creating, resuming, deleting, or changing monitoring settings.

## Reference(s):

- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [Amazon 竞品 Listing 差距 专属运营工作流](artifact/references/operation-workflow.md)
- [ARI API Key Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-listing-gap)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown narrative with ARI CLI command proposals, report links, and optional local Markdown, HTML, or CSV exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may access ARI account, product, review, monitoring, and report data.]

## Skill Version(s):

1.4.5 (source: SKILL.md frontmatter, _meta.json, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
