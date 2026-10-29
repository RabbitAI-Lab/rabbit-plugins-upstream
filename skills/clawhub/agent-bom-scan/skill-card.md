## Description:

Check specified packages, repositories, container images, SBOMs, or CVEs for vulnerabilities, with local MCP client discovery only when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to review specified software packages, repositories, container images, SBOMs, and vulnerability advisories. It provides scoped findings, remediation guidance, and requested SBOM or scan report outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability lookups send package identifiers, versions, and advisory IDs to providers, which may expose private package details.

Mitigation: Use offline mode unless sharing those identifiers is authorized, and report any resulting coverage gaps.

Risk: Scanning a repository or container image contacts the specified host, and this review of skill instructions is not a full audit of the external package.

Mitigation: Scan only explicitly authorized targets and review findings in the context of the target and scan coverage.

## Reference(s):

- [Agent BOM project](https://github.com/koda-ai-studio/agent-bom)
- [Agent BOM on PyPI](https://pypi.org/project/agent-bom/)
- [Agent BOM Security Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [Text, JSON, Markdown, SARIF, HTML, CycloneDX, or SPDX, depending on the requested report or SBOM]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and generated files are scoped to the authorized target; offline scans may have incomplete advisory coverage.]

## Skill Version(s):

0.111.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
