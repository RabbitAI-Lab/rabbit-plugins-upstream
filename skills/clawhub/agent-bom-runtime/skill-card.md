## Description:

AI runtime security monitoring — context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries. Use when the user mentions runtime monitoring, context graphs, lateral movement analysis, audit log correlation, or vulnerability analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use the skill to analyze runtime audit logs, correlate events with CVE findings, inspect context graphs for lateral movement, and query vulnerability trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided runtime audit logs may contain raw secrets or other sensitive data.

Mitigation: Provide only logs intended for analysis and remove raw secrets first.

Risk: Optional analytics storage sends data to a configured ClickHouse destination.

Mitigation: Enable ClickHouse only for a destination you control.

Risk: The reviewed artifact contains instructions only; the installed agent-bom package was not independently audited here.

Mitigation: Review the package through your normal software trust process before installing it.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text]

**Output Format:** [Runtime audit correlation findings, context graph analysis, and vulnerability analytics results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the supplied scan results, audit log, or analytics query.]

## Skill Version(s):

0.113.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
