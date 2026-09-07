## Description:

从 Amazon 低星评论和商品字段中归纳产品质量问题线索、证据和优先级；需要 ARI API key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to inspect low-star reviews and product fields, identify recurring quality issues, and prioritize evidence-backed product improvements. It is not a substitute for quality certification, recall decisions, supplier execution, or verified return-rate analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The quality-issue label may understate broader ARI account capabilities, including paid analysis, persistent schedules, competitor relationships, watches, alerts, and exports.

Mitigation: Review the ARI account permissions and current schedules, competitors, watches, alerts, and exports before and after installation.

Risk: Paid operations may execute under account auto-confirm rules or after explicit confirmation, consuming credits.

Mitigation: Keep auto-confirm off when every paid action should be approved, and verify quoted credits and balances before confirmed paid operations.

Risk: Custom ARI_BASE_URL or ARI_WEB_URL settings could redirect account/API-key traffic away from the official ARI service.

Mitigation: Use the default ARI service unless you control the alternate server, and require ARI_ALLOW_CUSTOM_BASE=1 only for intentional custom deployments.

Risk: Quality reports can be misleading when review samples, collection windows, variant coverage, or competitor data are incomplete.

Mitigation: Treat findings as directional evidence, check the reported data range and sample size, and avoid using the skill as a substitute for certification, recall, supplier, or return-rate decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/quality-issue)
- [ARI CLI and API Reference](references/reference.md)
- [Dedicated Product Quality Workflow](references/operation-workflow.md)
- [ARI User Guide](使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or concise text with optional shell commands and links to ARI reports or exported files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include review evidence, trend interpretation, product quality priorities, report URLs, account status, credit usage, and local export file paths.]

## Skill Version(s):

1.4.7 (source: evidence.json release.version, artifact/SKILL.md frontmatter, artifact/_meta.json, artifact/CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
