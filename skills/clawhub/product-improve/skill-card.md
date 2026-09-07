## Description:

Turns Amazon review complaints into prioritized product improvement actions for product, packaging, listing, monitoring, and customer-response workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to analyze ARI-collected review data, identify recurring complaints and trends, compare competitors, and convert evidence into product iteration and operations actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let the agent operate ARI account workflows that may consume credits or change monitoring, competitor, export, workbench status, or auto-confirm settings.

Mitigation: Install only when ARI account integration is intended, set a strict confirmation preference when needed, and review paid or state-changing actions before approval.

Risk: Price checks or VOC/analyze flows may execute under account auto-confirm rules if the user does not explicitly limit execution.

Mitigation: Use "only quote, do not execute" for price checks and require explicit confirmation before commands that can charge credits when auto-confirm is not desired.

Risk: A custom ARI endpoint could receive API-key authenticated requests if environment overrides are enabled.

Mitigation: Do not enable ARI_BASE_URL or ARI_ALLOW_CUSTOM_BASE unless the endpoint is trusted and uses HTTPS.

Risk: Retrying after an interrupted paid workflow can duplicate work or charges if the server already completed the task.

Mitigation: Check existing reports or workflow status before retrying interrupted paid operations.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [ARI User Guide](使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-improve)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and reports, optional JSON or CSV exports, and shell commands for setup, checks, collection, analysis, monitoring, and export.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, report IDs, sample ranges, credit usage, account balance information, local export paths, and confirmation prompts for paid actions.]

## Skill Version(s):

1.4.7 (source: release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
