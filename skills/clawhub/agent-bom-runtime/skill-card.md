## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to inspect AI runtime context graphs, correlate agent audit logs with CVE findings, and query vulnerability trends or posture history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented package install is not pinned to the reviewed version.

Mitigation: Install the reviewed release explicitly, for example `agent-bom==0.104.0`, before relying on this card.

Risk: Runtime audit logs and optional analytics configuration can contain sensitive operational context or credential environment variable names.

Mitigation: Provide only audit logs and optional ClickHouse configuration that are approved for analysis, and do not include raw credential values.

## Reference(s):

- [agent-bom GitHub project](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard report](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline tool-call and shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided audit log paths and optional analytics configuration.]

## Skill Version(s):

0.104.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
