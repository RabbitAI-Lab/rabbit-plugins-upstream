## Description:

Guides QA testers through structured execution observation across functional behavior, API responses, logs, UI rendering, data consistency, performance, and dependency signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA testers and developers use this skill during test execution to record per-run observations, flag abnormal signals, and identify follow-up questions for bug analysis and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to inspect logs, databases, screenshots, monitoring tools, or production-like systems.

Mitigation: Use it only in authorized QA environments and require explicit confirmation before Bash, database, or log-reading actions on production systems or sensitive logs.

Risk: Observation reports may include sensitive test data, logs, UI captures, or environment details.

Mitigation: Redact secrets, credentials, personal data, and internal endpoints before sharing reports.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or structured text observation reports with optional shell commands for authorized log and environment inspection]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include execution reports, observed results, anomaly lists, and environment issue notes.]

## Skill Version(s):

1.6.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
