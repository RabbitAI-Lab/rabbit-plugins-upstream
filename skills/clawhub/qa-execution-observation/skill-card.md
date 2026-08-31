## Description:

Helps QA practitioners observe functional behavior, API responses, logs, UI rendering, data consistency, and performance during test execution, then record anomalies and follow-up questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA testers and test engineers use this skill during test execution to monitor multiple signal streams, compare actual behavior with expected results, and produce observation records that identify anomalies and follow-up questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Log, monitoring, and database checks could expose secrets, personal data, or production data.

Mitigation: Use approved test or sanitized environments, prefer read-only database access, and redact sensitive values from copied logs and reports.

Risk: External monitoring or screenshot tools may capture sensitive application state when used during QA observation.

Mitigation: Run the skill only in controlled QA workflows and confirm that any external tools are approved for the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-execution-observation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown observation reports with tables, checklists, anomaly lists, and environment issue notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Observation records should include unique OBS IDs, related test case IDs, observed results, anomalies, environment issues, and coverage caveats.]

## Skill Version(s):

1.7.5 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
