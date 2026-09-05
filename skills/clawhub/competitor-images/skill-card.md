## Description:

对比主 ASIN 与已授权竞品商品页的图片字段、可见信息和评论反馈，整理图片表达缺口与拍摄说明；仅用于图片信息审查，需要 ARI API key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operations teams use this skill to compare a primary ASIN with authorized competitor product-page imagery, visible listing information, and review feedback so they can identify image-expression gaps and shooting notes. It is not intended for ad placement, automated publishing, sales forecasts, inventory, orders, profit, or real return-rate analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised as an Amazon image-gap reviewer, but the security evidence says the artifacts expose broader paid analysis, exports, monitoring, and account-management workflows.

Mitigation: Install only if the broader ARI Amazon review and operations assistant behavior is acceptable, and review billing, autoconfirm, schedule/watch, export, and account-management flows before use.

Risk: The skill uses an ARI API key and can interact with paid ARI operations.

Mitigation: Keep API keys out of reports and examples, review credit costs before confirmed paid actions, and verify server autoconfirm behavior against the user's expectations.

Risk: Changing the ARI service endpoint can redirect key-bearing requests away from the official service.

Mitigation: Keep the API endpoint on the official ARI service unless operating a trusted custom environment intentionally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-images)
- [Skill README](artifact/README.md)
- [Amazon Competitor Image Gap Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with CLI command references and ARI service JSON-derived findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations should be quoted and confirmed according to the skill's billing controls.]

## Skill Version(s):

1.4.5 (source: server release evidence, SKILL.md frontmatter, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
