## Description:

Track, aggregate, and report OpenClaw token usage and costs across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect local OpenClaw and Codex session logs, summarize token usage by date, model, session, or cron job, and estimate model costs for budget monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local usage reports can expose sensitive workflow metadata such as session filenames, model names, usage patterns, and cron job labels.

Mitigation: Run the skill locally, restrict access to generated reports and JSON exports, and review outputs before sharing them outside the intended audience.

Risk: The optional pricing updater performs outbound requests to OpenRouter and rewrites bundled pricing and registry files.

Mitigation: Use the updater only when outbound pricing lookup is acceptable, and review generated pricing changes before relying on them.

Risk: Cost outputs are estimates and may differ from provider billing.

Mitigation: Treat cost reports as planning aids and reconcile important budget decisions against provider invoices or official billing dashboards.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/space-cadet/skills/token-usage)
- [Project Homepage](https://github.com/space-cadet/openclaw-token-usage)
- [OpenRouter Models API](https://openrouter.ai/api/v1/models)
- [Kimi Pricing Documentation](https://platform.kimi.com/docs/pricing/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or plain text reports with optional JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include daily, weekly, all-time, model-level, session-level, cron-job, and estimated-cost breakdowns.]

## Skill Version(s):

2.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
