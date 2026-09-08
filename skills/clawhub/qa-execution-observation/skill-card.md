## Description:

Guides QA testers through execution observation by checking functional behavior, interface responses, logs, UI rendering, data consistency, performance signals, and anomalies during test runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and test teams use this skill to structure test execution observations, capture abnormal signals, and produce observation records for follow-up analysis and bug reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to inspect logs, database state, screenshots, or monitoring data that can contain sensitive test or system information.

Mitigation: Use it only in a controlled test environment with authorization for the systems and data being observed.

Risk: Observation records can contain incorrect or incomplete conclusions if abnormal signals are not reproducible or supporting logs are unavailable.

Mitigation: Record the environment, operation sequence, observed evidence, and follow-up questions so findings can be reviewed before bug reporting or root-cause analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-execution-observation)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown observation records, checklists, anomaly summaries, and execution reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observation IDs, linked test case IDs, observed results, anomalies, environment issues, and follow-up questions.]

## Skill Version(s):

1.7.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
