## Description:

Compares recorded display-price snapshots for an authorized Amazon product and competitor ASINs, highlighting relative price position, timestamp, and evidence gaps without claiming real-time pricing, sales, profit, inventory, orders, or automated repricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators use this skill to compare a primary ASIN with authorized competitor product-page snapshots, understand relative price positioning, and see where supporting product-detail or review evidence is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access ARI account data and product, review, and report data through an ARI API key.

Mitigation: Install only when that account access is acceptable, keep the key out of chat and reports, and revoke the stored ARI key if access is no longer needed.

Risk: Paid ARI workflows and auto-confirm rules can consume credits, including after a user asks for analysis rather than only a quote.

Mitigation: Use explicit quote-only requests for cost checks, disable or lower auto-confirm when needed, and require user confirmation before commands that report confirmationRequired.

Risk: Interrupted paid operations may already have completed and consumed credits.

Mitigation: Check existing reports or the original request status before retrying any paid collection or analysis command.

Risk: Monitoring and export features can change persistent ARI settings or write local files.

Mitigation: Confirm watch create, pause, resume, delete, schedule, competitor-binding, and export targets before execution; use read-only commands for inspection.

Risk: Price-positioning conclusions are limited to recorded snapshots and available samples.

Mitigation: State the data window, site, sample limits, and evidence gaps, and avoid claims about real-time prices, sales, profit, inventory, orders, ads, or automatic repricing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-price)
- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [README](README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown analysis and concise operating guidance; CLI commands may return structured JSON, report links, or local export files when invoked.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Outputs are bounded by authorized ARI data, snapshot timing, site, sample size, and the user's confirmation or auto-confirm settings.]

## Skill Version(s):

1.4.7 (source: server release, SKILL.md frontmatter, _meta.json, skill-defaults.json, scripts/ari.py, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
