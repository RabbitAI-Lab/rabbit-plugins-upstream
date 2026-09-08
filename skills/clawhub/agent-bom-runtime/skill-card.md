## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to analyze agent runtime context, correlate user-provided audit logs with CVE findings, and query vulnerability trends or posture history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided audit logs may contain sensitive operational details such as credential environment variable names.

Mitigation: Review audit logs before use, avoid including raw credential values, and share only the minimum data needed for the analysis.

Risk: Optional ClickHouse or kubectl use can expose analytics data or cluster context if configured unintentionally.

Mitigation: Configure optional ClickHouse and kubectl access deliberately, using least-privilege credentials and operator-approved endpoints.

## Reference(s):

- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and structured analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided JSONL audit logs, in-memory scan results, optional kubectl context, and optional ClickHouse analytics storage.]

## Skill Version(s):

0.103.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
