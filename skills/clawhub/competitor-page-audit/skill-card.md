## Description:

审查主 ASIN 与已授权竞品商品页的字段完整度、表达一致性和评论证据，输出对照问题清单；仅用于页面审查，不用于实时价格、销量、库存、广告、订单或真实退货率判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and their agents use this skill to run an ARI-backed page_compare/page audit that compares a main ASIN with authorized competitor product pages for listing-field completeness, wording consistency, and review-evidence alignment before producing an issues list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is presented as a competitor page audit, but the security evidence says the bundled ARI CLI can also manage monitoring, export reports or reviews, and modify ARI-side state under the same API key.

Mitigation: Install only when that broader ARI review-operations access is intended, run only user-requested workflows, and require clear user confirmation before state-changing actions.

Risk: Paid ARI collection and analysis actions can spend account credits.

Mitigation: Use quote, profile, status, or report lookup commands before paid execution, and run paid commands only after explicit confirmation with the expected requestId or command arguments.

Risk: ARI API keys could be exposed if requests are redirected to an untrusted custom endpoint.

Mitigation: Use the official ARI endpoint by default, keep keys in local user configuration or ARI_API_KEY, and allow custom ARI_BASE_URL or ARI_WEB_URL only for a trusted environment with ARI_ALLOW_CUSTOM_BASE=1.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-page-audit)
- [README](README.md)
- [User guide](使用说明.md)
- [Operation workflow](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text reports with CLI command guidance; exports may produce Markdown, HTML, or CSV files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid ARI actions.]

## Skill Version(s):

1.4.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
