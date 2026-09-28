## Description:

Analyzes agent context graphs, correlates runtime audit logs with CVE findings, and queries vulnerability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to examine agent context graphs, correlate user-provided runtime audit logs with CVE findings, and review vulnerability trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted package could expose the local environment.

Mitigation: Confirm you trust the agent-bom package on PyPI and its linked project before installation.

Risk: Runtime audit logs may contain sensitive operational details.

Mitigation: Review logs before sharing or processing them, and avoid exposing credential values.

Risk: Optional persistent analytics storage can retain vulnerability and runtime data.

Mitigation: Configure ClickHouse only when persistent storage is intended.

## Reference(s):

- [Agent-BOM project homepage](https://github.com/msaad00/agent-bom)
- [Agent-BOM package on PyPI](https://pypi.org/project/agent-bom/)
- [Agent-BOM OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings depend on available scan results, user-provided audit logs, and optionally configured analytics storage.]

## Skill Version(s):

0.106.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
