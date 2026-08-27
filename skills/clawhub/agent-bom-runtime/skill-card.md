## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to inspect AI runtime behavior, build context graphs, correlate user-provided audit logs with CVE findings, and query vulnerability analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking the runtime package from external package sources can introduce supply-chain risk.

Mitigation: Confirm the trusted PyPI or GitHub package source before installation.

Risk: Runtime audit logs and optional analytics storage can contain security-relevant operational details.

Mitigation: Analyze only intended audit logs and treat any configured ClickHouse datastore as sensitive.

Risk: Audit data may include credential environment variable names.

Mitigation: Do not include raw credential values in audit logs or outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)
- [agent-bom GitHub Repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI Package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown with tool call examples and analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May refer to user-provided audit log files and optional ClickHouse analytics storage when configured by the operator.]

## Skill Version(s):

0.102.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
