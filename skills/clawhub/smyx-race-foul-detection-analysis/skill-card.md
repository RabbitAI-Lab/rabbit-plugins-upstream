## Description:

Analyzes submitted pet race videos for start timing, finish order, lane assignment, and possible false starts or lane crossings, then returns a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Race referees and event organizers use the skill to review submitted race footage for possible start and lane fouls, finish order, and lane assignment. Its report supports referee review of race fairness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account handling may mix users’ reports, reusable credentials are stored locally, and the export-only option may still run analysis.

Mitigation: Prefer waiting for fixes before using this in shared or sensitive workspaces. Require reliable per-user account separation, protected token storage, separation of API secrets from identity fields, restricted credential destinations, and a working export-only mode.

Risk: Submitted files are uploaded to LifeEmergence’s service, and supplied URLs are forwarded for remote retrieval.

Mitigation: Use only video files and URLs approved for remote processing, and restrict credential destinations as advised by the security guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured race analysis report with detected events and a report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include start times, finish order, lane assignments, and possible foul evidence.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
