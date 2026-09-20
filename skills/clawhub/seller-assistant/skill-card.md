## Description:

亚马逊运营助手用 ARI 评论数据帮助 Amazon 卖家采集自家与竞品评论、查看评分和趋势、生成 VOC 或深度洞察报告，并把评论证据转化为运营、Listing、监控和差评处理建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operations teams use this skill to turn collected review data into product diagnostics, VOC reports, keyword and Listing guidance, competitor comparisons, alert triage, and monitoring decisions. It is aimed at conversational use: users provide an ASIN, site, and business question while the agent chooses the appropriate ARI command flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits when paid workflows run under explicit confirmation or server-side auto-confirm rules.

Mitigation: Set autoconfirm off when strict approval is required, use quote-only flows for pricing, and require explicit review before running paid analysis, collection, leaderboard, or advise actions.

Risk: Monitoring and competitor bindings can create future collection costs after the initial interaction.

Mitigation: Review schedule, competitors, and watch changes before enabling them, and prefer manual or paused monitoring when ongoing costs are not intended.

Risk: The skill uses an ARI API key and can change account-facing settings such as auto-confirm behavior.

Mitigation: Use browser setup or local configuration instead of sharing keys in chat, keep keys out of reports and examples, and review any autoconfirm setting changes.

Risk: Business conclusions may be incomplete if review samples, variant coverage, or time windows are limited.

Mitigation: Require outputs to state data range, sample size, site, collection window, and uncertainty before treating recommendations as operational decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/seller-assistant)
- [README](artifact/README.md)
- [使用说明](artifact/使用说明.md)
- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Products](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational guidance, Markdown reports, JSON command responses, shell command examples, exported CSV, and exported Markdown or HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may invoke ARI credit-consuming workflows when user authorization or server-side auto-confirm rules apply.]

## Skill Version(s):

1.4.13 (source: release evidence, SKILL.md frontmatter, CHANGELOG, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
