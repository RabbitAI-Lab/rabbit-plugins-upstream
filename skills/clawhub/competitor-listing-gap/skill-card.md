## Description:

对照主 ASIN 与已授权竞品的商品页字段、图片和评论证据，识别 Listing 表达差距与可验证改进项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and marketplace operators use this skill to compare a primary ASIN with an authorized competitor and produce evidence-based Listing gap analysis and improvement actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires ARI account access and can read Amazon product and review data tied to that account.

Mitigation: Install and use it only when that access is acceptable, keep the ARI API key out of chat transcripts and reports, and revoke or rotate the key if access is no longer needed.

Risk: Some analysis flows can spend ARI credits under account auto-confirm rules.

Mitigation: Set auto-confirm to always ask when per-run approval is required, use quote steps before paid runs, and proceed only after the user has explicitly approved the cost.

Risk: The package includes broader monitoring, export, report, and paid-analysis flows beyond the narrow Listing gap task.

Mitigation: Keep normal use scoped to the fixed page_compare/listing_gap workflow and avoid schedules, watches, exports, or broader reports unless the user explicitly requests them.

Risk: Incomplete samples or unsupported metrics could lead to misleading marketplace decisions.

Mitigation: State the data range and sample limits, compare only metrics available for both products, and do not infer real-time price, sales, inventory, orders, advertising, profit, or true return rates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-listing-gap)
- [Operation workflow reference](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [User guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise natural-language summaries, with occasional shell command snippets or JSON status from the ARI CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations may consume ARI account credits under the account's confirmation settings.]

## Skill Version(s):

1.4.7 (source: frontmatter, artifact/_meta.json, evidence.json release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
