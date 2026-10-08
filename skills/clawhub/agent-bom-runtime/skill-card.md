## Description:

Helps agents analyze context graphs, correlate user-provided runtime audit logs with CVE findings, and query vulnerability trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to assess agent runtime context, correlate provided audit logs with vulnerability findings, and examine security trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external agent-bom package introduces a dependency on its publisher.

Mitigation: Confirm you trust the package source before installing it.

Risk: User-provided audit logs may contain sensitive runtime-security information.

Mitigation: Provide only intended audit logs and avoid exposing credential values.

Risk: Optional ClickHouse analytics can persist sensitive runtime-security data.

Mitigation: Enable it only deliberately and configure storage access and credentials explicitly.

## Reference(s):

- [Project homepage](https://github.com/msaad00/agent-bom)
- [Python package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context graphs, runtime-to-CVE correlations, and vulnerability trend summaries depend on supplied scan and audit data.]

## Skill Version(s):

0.108.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
