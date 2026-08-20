## Description:

AI runtime security monitoring for context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to inspect agent runtime behavior, correlate audit logs with vulnerability findings, and query vulnerability posture trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit logs may contain secrets or sensitive operational data.

Mitigation: Use only intended audit logs and avoid passing files that contain raw secrets or data that should not be analyzed.

Risk: Optional ClickHouse storage can persist runtime analytics beyond the active session.

Mitigation: Configure ClickHouse only when persistent analytics are desired, and use operator-approved connection settings.

Risk: The skill installs and relies on an external third-party package.

Mitigation: Review the agent-bom package and source repository before installation in sensitive environments.

## Reference(s):

- [Source repository](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline commands and structured security analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided audit log paths, scan results already in memory, optional kubectl context, and optional ClickHouse analytics configuration.]

## Skill Version(s):

0.101.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
