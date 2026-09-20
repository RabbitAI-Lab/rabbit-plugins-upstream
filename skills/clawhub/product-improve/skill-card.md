## Description:

This skill helps Amazon sellers and operators turn review complaints into prioritized product improvement actions, while also supporting ARI review collection, VOC analysis, trend and keyword reports, monitoring, alerts, benchmarking, workbench actions, and report exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product operators, and ecommerce teams use this skill to analyze Amazon review data, identify recurring product issues, prioritize improvements by impact and severity, and generate customer-voice reports, exports, monitoring summaries, and operational guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some VOC and analysis flows can spend ARI credits through service-side auto-confirm behavior without a fresh per-action confirmation.

Mitigation: Users should request quote-only mode or ask for confirmation before every paid action when they want to prevent unexpected credit use.

Risk: The skill requires an ARI API key for authenticated workflows.

Mitigation: Use the browser authorization flow, environment variable, or local hidden-input configuration; do not paste credentials into chat or include keys in reports or examples.

Risk: Interrupted paid operations may already have consumed credits and produced an archived report.

Mitigation: Check existing reports or the original operation status before retrying a paid command.

Risk: Account confirmation preferences, monitoring schedules, exports, and workbench status can affect future costs or stored workflow state.

Mitigation: Require explicit user intent before changing confirmation settings, enabling monitoring, exporting files, or updating workbench status.

Risk: Connecting to a non-official or redirected endpoint could expose credentials or results.

Mitigation: Only use https://ari.funewa.com and stop on endpoint or redirect-blocked errors instead of bypassing connection checks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-improve)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text and Markdown reports with inline shell commands; exported reports may be Markdown, HTML, or CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some analysis and collection workflows may consume ARI credits or change account, monitoring, export, or workbench state.]

## Skill Version(s):

1.4.13 (source: server release evidence, SKILL.md frontmatter, _meta.json, and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
