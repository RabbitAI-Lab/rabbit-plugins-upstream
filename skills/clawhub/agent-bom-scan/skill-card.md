## Description:

Checks vulnerabilities in specified packages, repositories, container images, and SBOMs, and looks up named advisories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to assess vulnerabilities in explicitly identified software or SBOMs, inspect advisories, and prepare scoped scan findings or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups may disclose package identifiers and versions to advisory providers.

Mitigation: Confirm permission before checking private identifiers, or use offline mode and note its coverage gaps.

Risk: Local MCP-client or home-directory discovery may inspect sensitive configuration.

Mitigation: Scan explicit targets without discovery; request local-client discovery only when expressly authorized.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown; JSON, SARIF, or CycloneDX/SPDX for requested reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scoped to an authorized target; offline advisory coverage may be incomplete.]

## Skill Version(s):

0.108.3 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
