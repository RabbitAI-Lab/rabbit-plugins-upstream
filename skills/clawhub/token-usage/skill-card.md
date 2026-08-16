## Description:

Track, aggregate, and report OpenClaw token usage and costs across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect local OpenClaw and Codex session logs, answer token-usage questions, compare model/session activity, and estimate costs for budgeting or optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local session logs may reveal usage patterns, model names, session IDs, and cron job labels.

Mitigation: Run the reporting commands only in environments where the operator is allowed to read those local OpenClaw/Codex session logs.

Risk: The optional pricing updater contacts OpenRouter and updates bundled local pricing files.

Mitigation: Avoid running the pricing updater unless network access and local pricing-file changes are intended.

Risk: Cost outputs are estimates and may differ from actual billing.

Mitigation: Use generated cost reports for monitoring and comparison, and verify billing decisions against provider invoices or current provider pricing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/token-usage)
- [Project homepage](https://github.com/space-cadet/openclaw-token-usage)
- [OpenRouter models API](https://openrouter.ai/api/v1/models)
- [Kimi pricing documentation](https://platform.kimi.com/docs/pricing/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON reports with shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include daily, weekly, model, session, cron-job, token, cache, and estimated-cost summaries.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
