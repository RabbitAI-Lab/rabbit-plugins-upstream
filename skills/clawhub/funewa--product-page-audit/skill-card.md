## Description:

Amazon 商品页审查核对单个 Amazon 商品页的标题、要点和图片信息与真实买家评论体验之间的差距。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to audit a single product page against ARI product and review data. It helps identify gaps between listing claims and buyer feedback before making copy, positioning, or product-improvement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill links to an ARI account, stores an ARI API key locally, and sends Amazon product or review data to the ARI service.

Mitigation: Install and use it only when comfortable with that account connection and data flow; never paste the API key into chat or reports.

Risk: Some ARI workflows can spend credits, and account auto-confirm rules may allow small paid actions to run without a fresh prompt.

Mitigation: Use "only quote, do not execute" for pricing-only requests, review credit and balance output before confirming, and set auto-confirm off when every paid action should require approval.

Risk: The release includes paid reports, monitoring, competitor, advertising, and persistent account-setting workflows beyond a narrow page-audit task.

Mitigation: Use the fixed single-page audit workflow unless the user clearly requests another supported action, and verify ASIN, site, request ID, and cost before confirming paid execution.

Risk: Custom ARI endpoint environment variables can change where key-bearing requests are sent when intentionally enabled.

Mitigation: Leave ARI_BASE_URL and ARI_ALLOW_CUSTOM_BASE unset unless using a trusted self-hosted endpoint on purpose.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/product-page-audit)
- [Operation workflow](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with optional shell commands and ARI report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN, site, sample scope, report ID, report URL, credit usage, balance, and confirmation status when returned by ARI.]

## Skill Version(s):

1.4.8 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
