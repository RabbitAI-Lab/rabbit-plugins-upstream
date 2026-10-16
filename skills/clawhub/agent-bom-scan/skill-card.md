## Description:

Checks vulnerabilities in a specified package, repository, container image, or SBOM, and can inspect a named CVE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to assess vulnerabilities in explicitly specified packages, projects, images, and SBOMs, inspect advisories, and plan remediation. Local MCP-client discovery is available only when specifically requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability lookups may disclose package names, versions, advisory IDs, and requested scan targets to external services.

Mitigation: Confirm permission before querying private targets; use offline mode for restricted identifiers and disclose its coverage gaps.

Risk: MCP-client discovery can read local agent configuration files.

Mitigation: Use explicit targets with discovery disabled for ordinary scans; discover local clients only on explicit request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [Python package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance and commands; requested scan reports may be JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report unknown severity and offline advisory-coverage gaps rather than treating them as clean results.]

## Skill Version(s):

0.109.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
