## Description:

Helps analyze agent context graphs, correlate runtime audit logs with CVE findings, and query vulnerability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to examine agent context graphs, correlate selected runtime audit logs with CVE findings, and review vulnerability trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted package source could expose the operator's environment.

Mitigation: Verify that you trust the agent-bom package source before installation.

Risk: Audit logs or optional analytics storage could expose sensitive credential values.

Mitigation: Analyze only intended audit logs, avoid storing raw credential values, and configure any ClickHouse endpoint deliberately.

## Reference(s):

- [agent-bom project homepage (skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard (skill metadata)](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context graph analysis, audit log and CVE correlations, and vulnerability trend summaries.]

## Skill Version(s):

0.108.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
