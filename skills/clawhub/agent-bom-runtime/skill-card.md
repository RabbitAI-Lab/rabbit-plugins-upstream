## Description:

AI runtime security monitoring — context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries. Use when the user mentions runtime monitoring, context graphs, lateral movement analysis, audit log correlation, or vulnerability analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to analyze agent context graphs and lateral movement, correlate user-provided runtime audit logs with CVE findings, and query vulnerability trends and runtime events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is incomplete because a referenced runtime file was not included, so its behavior could not be fully assessed.

Mitigation: Review the complete release artifact, including the missing referenced file, before relying on the assessment.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Structured analysis and query results in text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.115.5 (source: artifact frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
