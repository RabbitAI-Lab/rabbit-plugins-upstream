## Description:

AI runtime security monitoring — context graph analysis, runtime audit log correlation with CVE findings, and vulnerability analytics queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use the skill to build context graphs, correlate user-provided runtime audit logs with CVE findings, and query vulnerability and runtime-event trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided audit logs may contain secret values or credential environment variable names.

Mitigation: Provide only logs intended for analysis and remove secret values first; never display or infer optional analytics credentials.

Risk: Configuring ClickHouse enables persistent analytics storage.

Mitigation: Configure ClickHouse only when persistent storage is intended.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Structured analysis and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include context graph findings, audit-log and CVE correlations, or vulnerability analytics results.]

## Skill Version(s):

0.113.2 (source: artifact frontmatter; server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
