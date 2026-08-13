## Description:

Offline dashboard for WorkBuddy local usage analytics, focused on token consumption, local credit estimates, thinking efficiency, model distribution, cost-performance, date-range filtering, error monitoring, and usage-spike inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy users and teams use this skill to generate a local usage dashboard from their own WorkBuddy history for cost monitoring, model comparison, error review, and usage auditing. It is scoped to WorkBuddy local/account usage data and is not a generic dashboard builder for arbitrary products or datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated dashboard and data files can expose local WorkBuddy usage history, including session titles, model usage, token counts, errors, and credit estimates.

Mitigation: Keep generated usage-status.json, usage-status.js, and HTML dashboard files private unless the user intentionally shares those usage details.

Risk: Local credit values are estimates when no WorkBuddy usage export is supplied, which can mislead cost analysis.

Mitigation: Use token totals as the primary metric and provide --credit-xlsx when exact exported credit values are needed for a date window.

Risk: Skipped or corrupted trace records can make a report incomplete.

Mitigation: Review the extractor's data-integrity warnings and dashboard warning banner before treating the report as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [README.md](artifact/README.md)
- [DATA-GUIDE.md](artifact/DATA-GUIDE.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Code, Shell commands, Guidance]

**Output Format:** [Self-contained HTML dashboard, usage-status.json, usage-status.js, and concise agent handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python 3 and reads WorkBuddy data from the configured local home path.]

## Skill Version(s):

1.2.1 (source: frontmatter, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
