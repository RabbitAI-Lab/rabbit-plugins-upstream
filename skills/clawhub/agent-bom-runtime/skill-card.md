## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to analyze agent runtime context graphs, correlate user-provided audit logs with CVE findings, and query vulnerability analytics during runtime security monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented install command may pull a newer or different external Python package than the reviewed release.

Mitigation: Pin installation to version 0.104.0 and use a trusted package index before deployment.

Risk: Runtime audit logs and optional ClickHouse connection details can contain operationally sensitive information.

Mitigation: Provide only audit logs and ClickHouse details intended for processing, and avoid displaying or inferring credential values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and tool invocation examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include context graph analysis, runtime audit correlation, and vulnerability analytics query guidance.]

## Skill Version(s):

0.104.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
