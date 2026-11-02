## Description:

AI runtime security monitoring — context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to analyze agent runtime context, correlate supplied audit logs with CVE findings, and query vulnerability trends and runtime events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit logs may contain raw secrets.

Mitigation: Use only logs intended for analysis and remove raw secrets before use.

Risk: Optional ClickHouse analytics can store audit data persistently.

Mitigation: Configure ClickHouse only when needed and use appropriately scoped credentials.

Risk: The installed agent-bom package code was not inspected in this release review.

Mitigation: Pin the package version and review the package code before installation.

## Reference(s):

- [agent-bom project homepage](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Concise analysis and query results in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize context graphs, runtime audit and CVE correlations, vulnerability trends, and runtime events from available data.]

## Skill Version(s):

0.112.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
