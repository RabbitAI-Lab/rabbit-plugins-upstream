## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to analyze agent context graphs, correlate runtime audit logs with CVE findings, and query vulnerability trends and runtime events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because a referenced runtime component was not available for review, so some behavior may not have been assessed.

Mitigation: Review the referenced runtime component before relying on its behavior.

Risk: Runtime audit data may include credential environment variable names.

Mitigation: Do not include raw credential values in audit data; configure optional analytics credentials explicitly and do not display or infer them.

## Reference(s):

- [ClawHub release](https://clawhub.ai/msaad00/skills/agent-bom-runtime)
- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Structured text with context graph, audit correlation, and vulnerability analytics results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are based on in-memory scan results and any user-provided JSONL audit log data.]

## Skill Version(s):

0.114.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
