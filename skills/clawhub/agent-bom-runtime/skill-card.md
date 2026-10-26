## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use the skill to inspect agent context graphs, correlate runtime audit logs with CVE findings, and query vulnerability trends or posture history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime audit data may contain sensitive information.

Mitigation: Supply only intended audit files and remove raw secrets before analysis.

Risk: Optional ClickHouse storage can persist analytics data.

Mitigation: Enable it only with an intentionally selected endpoint and retention policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured security analysis and concise text or Markdown responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis is based on supplied scan results and audit logs.]

## Skill Version(s):

0.110.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
