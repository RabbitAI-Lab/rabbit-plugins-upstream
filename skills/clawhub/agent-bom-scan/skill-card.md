## Description:

Checks vulnerabilities in specified packages, repositories, container images, and SBOMs, and inspects named CVEs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams can assess vulnerabilities and prioritize remediation for explicitly named software assets, inspect advisories, and generate requested scan reports or SBOMs. Local MCP-client discovery is available only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online scans can disclose private package identifiers, versions, advisory IDs, or requested repository and image targets to external services.

Mitigation: Confirm authorization for online lookups; use offline mode for private identifiers and report coverage gaps.

Risk: Optional MCP-client discovery can inspect local configuration files.

Mitigation: Require an explicit discovery request and limit inspection to authorized files; do not expose credentials or configuration contents.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage (skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Files]

**Output Format:** [Text or Markdown findings; requested JSON, SARIF, HTML, or CycloneDX/SPDX reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report unknown severity and gaps in offline advisory coverage.]

## Skill Version(s):

0.108.4 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
