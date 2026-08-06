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

Risk: The skill analyzes user-provided runtime audit logs that may contain sensitive operational details or credential variable names.

Mitigation: Provide only audit logs intended for analysis and review outputs before sharing them outside the operating environment.

Risk: Optional ClickHouse or kubectl integrations can expand the data sources available to the workflow when enabled.

Mitigation: Configure those integrations only when needed, with least-privilege access and operator-supplied endpoints.

Risk: Server-resolved GitHub import provenance is unavailable for this version.

Mitigation: Review the linked source or package directly if source provenance is required for deployment approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-runtime)
- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard report](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands and concise analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided audit log files and optional kubectl or ClickHouse integrations when configured by the operator.]

## Skill Version(s):

0.99.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
