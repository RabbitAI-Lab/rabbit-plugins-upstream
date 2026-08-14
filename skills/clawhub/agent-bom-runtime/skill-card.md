## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to inspect agent runtime behavior, build context graphs, correlate user-provided audit logs with CVE findings, and query vulnerability analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external agent-bom package source.

Mitigation: Confirm the package source and version are trusted before installation.

Risk: User-provided runtime audit logs may contain sensitive operational details, including credential environment variable names.

Mitigation: Treat audit logs as sensitive input, avoid sharing raw logs, and redact sensitive identifiers before including findings in reports.

## Reference(s):

- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with tool invocation examples and concise analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference runtime audit files supplied by the user; does not require credentials.]

## Skill Version(s):

0.100.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
