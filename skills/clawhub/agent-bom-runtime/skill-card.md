## Description:

AI runtime security monitoring — context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to analyze agent context graphs, correlate runtime audit logs with vulnerability findings, and query vulnerability trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided audit logs may contain secrets or credential values.

Mitigation: Remove secrets before supplying logs and include only the intended audit data.

Risk: Optional ClickHouse analytics persist runtime analytics data.

Mitigation: Configure ClickHouse only when persistent analytics are intended.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)
- [Project homepage listed in metadata](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text]

**Output Format:** [Text summaries and query results, including context graph and runtime correlation findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis uses supplied scan results and audit logs; persistent analytics requires optional ClickHouse configuration.]

## Skill Version(s):

0.111.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
