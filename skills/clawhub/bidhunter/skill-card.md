## Description:

BidHunter helps agents monitor tender notices, compare opportunities against user-defined qualification rules, generate bid-readiness reports, and optionally summarize tender documents, suggest bid strategy, and scan statutory bid-rejection risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and bid teams use this skill to monitor public and enterprise tender sources, triage opportunities against their own qualifications, and prepare concise reports, calendars, and compliance checks before bid submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement document text, API keys, or generated reports may be sent to configurable external services.

Mitigation: Review configuration before use, keep AI disabled unless external processing through the configured MiniMax-compatible endpoint is acceptable, and use only HTTPS endpoints you control.

Risk: Webhook, push, and browser-based rule-editor workflows can expose reports or local controls if used on untrusted systems.

Mitigation: Isolate webhook and browser-session use, run the local rule editor only briefly on a trusted machine, and review push destinations before enabling notifications.

Risk: Tender-source adapters can fail or return incomplete data, which may lead to missed opportunities.

Mitigation: Check source adapter status, validate configured sources, and treat generated reports as triage outputs that require human review.

## Reference(s):

- [BidHunter ClawHub Release Page](https://clawhub.ai/419597334-sudo/skills/bidhunter)
- [Field Standard](references/field_standard.md)
- [Filter Rules](references/filter_rules.md)
- [Platform Support and Configuration](references/platforms.md)
- [Setup Guide](references/setup-guide.md)
- [Skill Dependencies](skill-dependencies.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and text reports, HTML reports, JSON or JSONL records, local configuration files, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local reports, calendars, configuration, local telemetry, and pushed notifications depending on user configuration.]

## Skill Version(s):

2.6.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
