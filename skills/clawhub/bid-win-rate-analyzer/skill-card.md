## Description:

Analyzes a specific tender opportunity using Zhiliaobiaoxun bid history to estimate win probability, supplier preference signals, competitor strength, bid pricing context, and bid/no-bid risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and bidding teams use this skill to decide whether to pursue a specific tender, identify likely competitors, estimate pricing posture, and produce a concise bid decision report. The skill is intended for public bid-data analysis and requires users to verify conclusions against the underlying source records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically register an account and collect a device identifier when no API key is configured.

Mitigation: Prefer supplying ZLBX_API_KEY through a secure mechanism, and decline auto-registration when device fingerprinting is not acceptable.

Risk: The skill stores credentials in a local configuration file.

Mitigation: Protect local credential files, avoid sharing their contents, and rotate the API key if it may have been exposed.

Risk: Generated reports can preserve signed access links and business-sensitive bid analysis.

Mitigation: Treat HTML reports and signed links as sensitive files and share them only with intended recipients.

Risk: Bid-win analysis may be incomplete, stale, or misleading if public bid data is missing or delayed.

Mitigation: Review cited records, inspect stated data gaps, and use the report as decision support rather than as a final commercial recommendation.

Risk: Analysis about real companies and public agencies can create reputational risk if inferences are stated as facts.

Mitigation: Keep factual records separate from inferred signals, use neutral language, and avoid unsupported accusations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-win-rate-analyzer)
- [API quick reference](references/api-quick.md)
- [Workflow guide](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [HTML report renderer](scripts/render_report.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include data citations, source-data caveats, cost estimates, and a disclaimer; the skill uses ZLBX_API_KEY for authenticated bid-data access.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
