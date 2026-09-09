## Description:

Analyzes competitors from a bidding and procurement perspective, using Zhiliaobiaoxun tender data to produce single-company intelligence reports, two-company comparisons, and monitoring-oriented summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sales teams, and bid teams use this skill to assess a named company's tender history, competitive overlap, customer relationships, and public risk signals before bidding, partnering, or monitoring market competitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts zhiliaobiaoxun.com services and may consume paid API credits.

Mitigation: Review the stated credit estimate before use and monitor the account tied to ZLBX_API_KEY.

Risk: If no API key is configured, the skill may ask to auto-register a trial account using a stable hashed device identifier.

Mitigation: Prefer a manually configured ZLBX_API_KEY when avoiding auto-registration, and grant registration consent only on trusted machines.

Risk: The skill can persist API credentials locally and write HTML reports containing company intelligence.

Mitigation: Use controlled file permissions, avoid shared machines, and remove local reports or credentials when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/competitor-intel-analysis)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API quick reference](artifact/references/api-quick.md)
- [Workflow guide](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, optional self-contained HTML reports, and concise follow-up guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based trial registration; may write HTML reports under ~/zlbx-company-intel-files/.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
