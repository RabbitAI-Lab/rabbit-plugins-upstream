## Description:

Looks up MCP server security metadata and helps assess marketplace packages, server fleets, skill files, and source code for trust and security risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to check MCP servers before installation, assess server inventories and skill files, and request code security scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the required Python package introduces third-party code into the operator's environment.

Mitigation: Verify that you trust the agent-bom package source before installing it.

Risk: Optional Snyk enrichment may send scan data to a third-party service.

Mitigation: Enable SNYK_TOKEN only when third-party enrichment is intended; bundled registry lookups require no credentials or network access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage (listed in skill metadata; not verified import provenance)](https://github.com/msaad00/agent-bom)
- [agent-bom package on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Security assessment guidance, Shell commands]

**Output Format:** [Markdown and text with scan results and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry lookups use bundled data; optional code scans may use Semgrep and Snyk enrichment.]

## Skill Version(s):

0.108.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
