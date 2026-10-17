## Description:

Helps analyze agent context graphs, correlate runtime audit logs with CVE findings, and query vulnerability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to examine agent context graphs, relate user-provided runtime audit logs to CVE findings, and review vulnerability trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime audit logs can expose sensitive operational context.

Mitigation: Review and redact logs before providing them for analysis or sharing results.

Risk: Optional ClickHouse or Kubernetes integration may access infrastructure beyond local analysis.

Mitigation: Configure ClickHouse or kubectl only when those integrations are intentionally needed.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom package on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard for agent-bom](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of context graphs, audit correlations, and vulnerability analytics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses scan results and user-provided audit logs; optional analytics storage requires an intentionally configured ClickHouse connection.]

## Skill Version(s):

0.109.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
