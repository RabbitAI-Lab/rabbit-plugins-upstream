## Description:

This skill helps Amazon operators use ARI product-detail and review evidence to identify user value, usage scenarios, and verifiable product-positioning directions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to turn product-detail and review evidence into concise positioning guidance, including customer value, likely use scenarios, and evidence-backed listing or product strategy discussion points. It is not intended for market sizing, sales forecasting, ad execution, or brand strategy without product and review evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make paid ARI requests and manage account state, including confirmation settings and monitoring workflows.

Mitigation: Use quote-only mode when pricing is needed, keep auto-confirm disabled for per-action approval, and require explicit user confirmation before paid runs or persistent monitoring changes.

Risk: The skill uses an ARI API key and can send authenticated requests to ARI services.

Mitigation: Use the documented setup or local configuration flow, do not share API keys in chat or reports, and do not set custom API base variables unless the host is controlled and trusted.

Risk: Local exports can write report or review data to user-selected paths.

Mitigation: Export only to intended non-sensitive locations and review generated Markdown, HTML, or CSV files before sharing.

Risk: Review-derived positioning guidance can be misleading when samples are small, stale, or incomplete.

Mitigation: Report the data range, sample limits, and evidence basis, and avoid using the skill for unsupported claims such as sales forecasts, ad execution, or market-size estimates.

## Reference(s):

- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [User Guide](使用说明.md)
- [ARI API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Products](https://ari.funewa.com/zh/products)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise guidance, with optional JSON from ARI CLI commands and local Markdown, HTML, or CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may quote, confirm, or run paid ARI operations when the user authorizes them.]

## Skill Version(s):

1.4.8 (source: evidence.release.version, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
