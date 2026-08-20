## Description:

This skill helps agents evaluate China-focused government, public-institution, and state-owned-enterprise procurement bids by analyzing bid fit, restrictive signals, buyer history, likely competitors, price benchmarks, disqualification risks, and compliance considerations using ZhiLiao BiaoXun procurement data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement teams, bidding advisors, and agents use this skill to decide whether to pursue a specific public procurement bid, how to price it, and which competitors or compliance issues require attention. It is designed for concrete project-level bid evaluation rather than general procurement search.

### Deployment Geography for Use:

Global, with China-focused procurement data and workflows.

## Known Risks and Mitigations:

Risk: The skill uses a third-party procurement data service and may consume paid or trial credits.

Mitigation: Review expected query cost before analysis and stop for user approval before exceeding the documented budget.

Risk: The skill can store an API key in local configuration and uses ZLBX_API_KEY when available.

Mitigation: Prefer a preconfigured environment variable or local config file and never expose API keys in chat or generated reports.

Risk: Optional trial registration uses platform, CPU architecture, and a hashed MAC address for device-based trial de-duplication.

Mitigation: Run registration only after explicit user consent, and skip registration entirely when an API key is already configured.

Risk: Generated HTML reports may include signed sk links that grant access to source records.

Mitigation: Review reports before sharing and treat signed source-record links as sensitive access links.

Risk: Bid recommendations may be incomplete or misleading if procurement data is missing, stale, or not applicable to the user's situation.

Mitigation: Require traceable data support, call out data gaps, and treat the report as decision support rather than a final business decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bid-decision)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API quick reference](artifact/references/api-quick.md)
- [Bid decision workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown procurement decision report, optional self-contained HTML report file, and supporting operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full reports typically use 12-25 data queries; quick analysis uses about 5-8 data queries.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
