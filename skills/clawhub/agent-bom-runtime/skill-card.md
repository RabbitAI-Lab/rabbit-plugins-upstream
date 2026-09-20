## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to inspect runtime context graphs, correlate agent audit logs with CVE findings, and query vulnerability trends for agent deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party package can introduce supply-chain risk.

Mitigation: Confirm trust in the publisher and package before installation, and review the linked package and scorecard evidence before deployment.

Risk: Runtime audit logs may contain sensitive operational details or credential environment variable names.

Mitigation: Only provide audit logs intended for analysis, avoid raw secret values, and handle the resulting analysis under the same data controls as the source logs.

Risk: Optional ClickHouse use creates persistent analytics and runtime-event storage.

Mitigation: Configure ClickHouse intentionally with appropriate access controls, retention, and storage location before enabling persistence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard report](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.105.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
