## Description:

从主 ASIN 与已授权竞品的商品字段、图片和评论证据提炼可验证的差异化方向与待验证问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and product teams use this skill to compare a main ASIN with authorized competitor evidence and generate product differentiation opportunities, validation questions, and report guidance through ARI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access ARI account data and manage reports, monitoring, exports, and billing-related confirmation settings.

Mitigation: Install only if that account access is acceptable, use quote-only mode for price checks, consider turning autoconfirm off, and review schedule, watch, competitor, and export changes before approval.

Risk: Paid operations may execute when ARI auto-confirm rules apply.

Mitigation: Confirm credit costs and account balance before paid work when confirmation is required, and avoid changing long-term confirmation settings unless the user explicitly asks.

Risk: Differentiation recommendations may be based on limited review samples or incomplete product and competitor evidence.

Mitigation: Treat outputs as directional, include data scope and sample limitations, and verify decisions against additional business sources before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/differentiation)
- [Amazon 产品差异化机会 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language guidance and Markdown reports, with occasional inline shell commands for setup or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, data scope, sample warnings, request IDs, and credit usage when returned by ARI.]

## Skill Version(s):

1.4.7 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
