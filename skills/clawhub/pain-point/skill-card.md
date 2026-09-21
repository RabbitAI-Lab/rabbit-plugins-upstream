## Description:

提炼 Amazon 评论中的买家痛点、未满足需求、趋势、竞品差异和运营建议，并可通过 ARI 生成报告、导出评论和管理监控。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, operators, and e-commerce analysts use this skill to inspect ARI-collected review data for buyer pain points, unmet needs, low-star causes, trends, competitor comparisons, listing improvements, and product-operations follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI actions may consume credits, including cases where account auto-confirm rules allow a report to run without a separate prompt.

Mitigation: Review billing and confirmation settings before use; use quote-only phrasing for pricing checks and require explicit confirmation for paid actions when appropriate.

Risk: The skill stores an ARI API key locally and uses it to access account data, reviews, reports, and billing-related ARI services.

Mitigation: Use the browser authorization flow or hidden local configuration, keep the key out of chat and reports, and revoke or recreate the key from the ARI account page if needed.

Risk: Monitoring, competitors, watch, and workbench commands can change persistent account state or create recurring collection costs.

Mitigation: Confirm the exact ASIN, watch ID, schedule, and cost before changing monitoring, competitor, watch, or review-status settings.

Risk: Export commands can write report or review files to disk.

Mitigation: Keep exports in an intended working directory and inspect exported files before sharing them.

## Reference(s):

- [Skill README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/pain-point)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Natural-language summaries, Markdown reports, JSON command responses, and optional CSV, Markdown, or HTML export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; some collection, analysis, leaderboard, and advice actions may consume ARI credits.]

## Skill Version(s):

1.4.13 (source: SKILL.md frontmatter, artifact/_meta.json, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
