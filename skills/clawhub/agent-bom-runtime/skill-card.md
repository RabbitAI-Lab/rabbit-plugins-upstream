## Description:

Analyzes agent context graphs, correlates runtime audit logs with CVE findings, and queries vulnerability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to examine agent context graphs, correlate provided runtime audit logs with CVE findings, and review vulnerability analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided runtime audit logs may contain sensitive operational details.

Mitigation: Provide only intended audit logs, exclude raw credential values, and review access to any stored analytics.

Risk: Optional ClickHouse storage persists vulnerability analytics outside the local session.

Mitigation: Configure ClickHouse only when needed and apply appropriate access and retention controls.

Risk: The external package requires a separate supply-chain review in strict environments.

Mitigation: Review the PyPI package and linked project independently before installation.

## Reference(s):

- [Agent-BOM project (linked in skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [Agent-BOM on PyPI](https://pypi.org/project/agent-bom/)
- [Agent-BOM OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context graph findings, audit-log/CVE correlations, and vulnerability analytics summaries.]

## Skill Version(s):

0.108.4 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
