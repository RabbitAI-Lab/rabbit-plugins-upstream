## Description:

把 Amazon 商品特性连接到评论验证的用户利益，提出有证据支持的 Listing 表达建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon operators and ecommerce teams use this skill to turn product details and collected review evidence into benefit-focused Listing wording suggestions. It is scoped to evidence mapping for Listing benefits, not ad bidding, unsupported product claims, or automatic Amazon page publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release presents a narrow Listing-benefit purpose while enabling broader ARI account workflows that can spend credits or change account-related settings.

Mitigation: Install only when broad ARI account operation is intended, review the skill before deployment, and keep credit-spending actions behind explicit user confirmation unless the user has intentionally configured auto-confirm.

Risk: Credit-spending operations may run under account auto-confirm rules.

Mitigation: Use quote-only flows for price checks, turn auto-confirm off when every charge should be approved, and report credits used and remaining balance after paid actions.

Risk: Custom ARI endpoint settings can redirect requests that include the API key.

Mitigation: Avoid custom ARI_BASE_URL settings unless the endpoint is fully trusted and intentionally enabled by the user.

Risk: Monitoring, schedule, competitor, and export actions can affect ongoing collection behavior or local data handling.

Mitigation: Review schedule, watch, competitor, and export targets before approval, and export only to intended local destinations.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [Feature Benefit Operation Workflow](artifact/references/operation-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/feature-benefit)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise conversational text, with shell commands only for setup, confirmation, or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should identify the data range, review evidence, trends, credit use when applicable, and limitations when sample size or coverage is insufficient.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
