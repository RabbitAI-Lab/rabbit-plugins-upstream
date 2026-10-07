## Description:

Analyzes agent context graphs, correlates user-provided runtime audit logs with CVE findings, and answers vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to inspect agent context graphs, correlate supplied audit logs with vulnerability findings, and review vulnerability trends and runtime events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied runtime audit logs may expose sensitive operational details.

Mitigation: Review and minimize logs before sharing them; do not disclose credential values.

Risk: Optional analytics storage can retain runtime data.

Mitigation: Configure ClickHouse only when persistent storage is intended and access is appropriately controlled.

Risk: Installing a third-party package requires trusting its distribution source.

Mitigation: Confirm the publisher and review the Agent-BOM package source before installation.

## Reference(s):

- [Agent-BOM project homepage (publisher-supplied)](https://github.com/msaad00/agent-bom)
- [Agent-BOM package on PyPI](https://pypi.org/project/agent-bom/)
- [Agent-BOM OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown with analysis and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context graph insights, audit-log/CVE correlations, and vulnerability trend summaries.]

## Skill Version(s):

0.108.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
