## Description:

Checks specified packages, repositories, container images, and SBOMs for vulnerabilities, or looks up a named CVE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to check explicitly selected software assets for vulnerabilities, review findings, and plan remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning unspecified local files or MCP-client configurations can expose sensitive information.

Mitigation: Scan only explicitly authorized targets; discover local MCP clients only when requested.

Risk: Online vulnerability lookups can disclose private package names and versions to public providers.

Mitigation: Confirm permission before online lookups for private assets, or use offline mode and report its coverage gaps.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [agent-bom security scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, SBOMs]

**Output Format:** [Markdown guidance and findings; optional JSON, SARIF, HTML, or CycloneDX/SPDX reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline scans can have incomplete advisory coverage.]

## Skill Version(s):

0.108.2 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
