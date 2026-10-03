## Description:

Helps analyze agent context graphs, correlate runtime audit logs with CVE findings, and query vulnerability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to examine agent context graphs, correlate user-provided runtime audit logs with vulnerability findings, and review vulnerability analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external package from an untrusted source may expose the environment to unwanted code.

Mitigation: Confirm that you trust the agent-bom package source before installing it.

Risk: Runtime audit logs may contain sensitive operational information.

Mitigation: Provide only audit log files you intend to analyze, and avoid sharing credential values.

Risk: Optional analytics storage or Kubernetes access may involve sensitive data or cluster context.

Mitigation: Configure ClickHouse or kubectl only when you trust the selected storage or cluster context.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown text with findings and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the available scan findings and user-provided audit logs.]

## Skill Version(s):

0.107.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
