## Description:

Queries and analyzes Alibaba Cloud SLS data through Context Models to answer business questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business analysts use the skill to answer questions about SLS log data using verified Context Model definitions and read-only queries, rather than to manage models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad cloud credentials could expose SLS data beyond the intended analysis.

Mitigation: Use least-privilege read-only credentials and restrict access to approved projects and logstores.

Risk: Incomplete or mismatched query results could lead to misleading business conclusions.

Mitigation: Verify query completion, definitions, time ranges, and source coverage before reporting conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sdk-team/skills/alibabacloud-sls-data-agent-qa)
- [Python runtime and credentials](artifact/references/python-runtime.md)
- [Incomplete and inexact query results](artifact/references/sql/incomplete.md)
- [Result presentation](artifact/references/chart-delivery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown answers with queries and optional tables or charts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes data sources, query time windows, and coverage limitations.]

## Skill Version(s):

0.0.1 (source: release metadata, references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
