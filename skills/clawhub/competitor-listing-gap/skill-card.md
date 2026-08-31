## Description:

对照主 ASIN 与已授权竞品的商品页字段、图片和评论证据，识别 Listing 表达差距与可验证改进项；仅用于商品页对比，不用于实时价格、销量、库存、广告、订单或真实退货率判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare a primary ASIN against authorized competitor product-page fields, images, and review evidence, then identify Listing wording gaps and verifiable improvement actions. It requires an ARI API key and gates paid analysis behind an explicit quote and confirmation flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged CLI exposes broader ARI account-management, monitoring, export, and paid-operation commands than the narrow Listing gap use case.

Mitigation: Before execution, verify the intended command and keep this skill on the fixed page_compare/listing_gap workflow unless the user explicitly asks for another documented ARI action.

Risk: ARI API keys are account credentials and could be sent to a non-official host if the request base URL is changed carelessly.

Mitigation: Use the documented setup, configuration, or ARI_API_KEY paths; do not include keys in reports or examples, and allow custom ARI_BASE_URL only when ARI_ALLOW_CUSTOM_BASE=1 is intentionally set.

Risk: Paid collection, analysis, leaderboard, and advice commands can consume credits, and retrying interrupted paid operations may duplicate charges.

Mitigation: Require a quote and explicit --confirm before paid work, then check reports or operation status after interruptions before deciding whether to retry.

Risk: Listing comparisons can be misleading when review samples are small, windows differ, or one side lacks comparable data.

Mitigation: Report sample size, site, statistics window, and unavailable fields; treat small samples as directional and avoid inferring unsupported sales, inventory, advertising, order, or real return-rate conclusions.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Amazon Competitor Listing Gap Operation Workflow](references/operation-workflow.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI products](https://ari.funewa.com/zh/products)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-listing-gap)
- [ClawHub publisher profile](https://clawhub.ai/user/funewa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and links to generated ARI reports when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN, site, sample size, report ID, credits used, current balance, and report URL when returned by ARI.]

## Skill Version(s):

1.4.3 (source: server release evidence, SKILL.md frontmatter, _meta.json, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
