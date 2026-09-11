## Description:

Generates an AI-assisted weekly operations report for one subscribed Amazon ASIN, summarizing product changes, review signals, and prioritized follow-up actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and marketplace operators use this skill to turn subscribed ASIN product data, review signals, and snapshots into a weekly operations brief with action priorities. It is intended for confirmed, account-authorized ARI workflows rather than free watch digests or store-level order and inventory reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses ARI account access and stores a local ARI API key.

Mitigation: Authorize only through the ARI browser flow or approved key setup, do not paste keys into chat or reports, and remove access if the skill is no longer trusted.

Risk: The skill can initiate paid analysis, monitoring changes, exports, and account-level confirmation settings.

Mitigation: Set autoconfirm to ask every time when per-run approval is required, review quoted credits and balances before confirmed paid runs, and check schedule, watch, and export targets before approving changes.

Risk: A custom ARI endpoint could redirect account-key requests away from the official service.

Mitigation: Avoid custom ARI_BASE_URL or ARI_WEB_URL values unless the endpoint is controlled and intentionally allowed; clear unexpected environment overrides before use.

Risk: Interrupted paid operations may already have charged credits and produced an archived report.

Mitigation: Check the relevant report or operation status before retrying any confirmed paid operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/weekly-operator)
- [ARI CLI and API reference](references/reference.md)
- [Amazon 单 ASIN 运营周报 专属运营工作流](references/operation-workflow.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise conversational guidance, with shell commands only for setup, advanced usage, or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are grounded in ARI-returned product, review, report, billing, and monitoring data; the skill should state data windows, sample limits, report URLs, and credits used when available.]

## Skill Version(s):

1.4.8 (source: server release metadata, skill frontmatter, _meta.json, skill-defaults.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
