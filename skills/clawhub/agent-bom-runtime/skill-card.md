## Description:

Analyzes agent context graphs, correlates runtime audit logs with CVE findings, and queries vulnerability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to investigate agent context graphs, correlate supplied runtime audit logs with CVE findings, and review vulnerability trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted package could expose the user's environment.

Mitigation: Confirm you trust the listed PyPI package and project homepage before installing.

Risk: Runtime audit logs and analytics may contain sensitive operational details.

Mitigation: Use only intended audit logs and operator-configured ClickHouse endpoints; do not share credential values.

## Reference(s):

- [agent-bom project homepage (listed by publisher; source provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [agent-bom OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [Text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available scan findings, supplied audit logs, and optionally configured analytics storage.]

## Skill Version(s):

0.107.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
