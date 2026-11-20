## Description:

AI runtime security monitoring — context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries. Use when the user mentions runtime monitoring, context graphs, lateral movement analysis, audit log correlation, or vulnerability analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use the skill to analyze agent runtime context, correlate user-provided audit logs with CVE findings, and query vulnerability trends and runtime events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review could not resolve the referenced proxy-audit.jsonl file, so evidence about that file is incomplete.

Mitigation: Confirm the audit file is available and review its contents before relying on runtime correlation results.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)

## Skill Output:

**Output Type(s):** [Analysis, Text]

**Output Format:** [Text with structured runtime security findings, vulnerability correlations, and analytics query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Works from scan results already in memory and user-provided audit logs; optional ClickHouse configuration enables persistent analytics.]

## Skill Version(s):

0.115.4 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
