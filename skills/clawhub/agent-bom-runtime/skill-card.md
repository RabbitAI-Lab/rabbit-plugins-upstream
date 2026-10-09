## Description:

Analyzes agent context graphs, correlates runtime audit logs with CVE findings, and queries vulnerability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to inspect agent context graphs, correlate user-supplied runtime audit logs with CVEs, and review vulnerability trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI introduces package supply-chain risk.

Mitigation: Review the PyPI package and project before installing, as recommended by the release security guidance.

Risk: Optional ClickHouse or kubectl access can expose analytics data or cluster resources.

Mitigation: Configure those connections only when needed and limit access to the intended environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-runtime)
- [Project homepage listed in skill metadata](https://github.com/msaad00/agent-bom)
- [agent-bom package on PyPI](https://pypi.org/project/agent-bom/)
- [Project OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context graph analysis, audit-to-CVE correlation, and vulnerability trend results; no fixed output schema is specified.]

## Skill Version(s):

0.108.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
