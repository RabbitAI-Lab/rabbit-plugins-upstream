## Description:

Check vulnerabilities in a specified package/version, repository, container image, or SBOM, or inspect a specified CVE. Discover local MCP clients only when the user explicitly requests that discovery. Ask for the target when a request such as "verify" or "is this safe" does not identify one.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check specified packages, repositories, container images, SBOMs, and CVEs for vulnerabilities, and to generate SBOMs or obtain remediation and compliance guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability lookups send package identifiers, versions, and advisory IDs to providers; repository and image scans also contact the requested host.

Mitigation: Confirm permission before querying private package identifiers. Use offline mode when disclosure is not authorized, and report resulting coverage gaps.

Risk: Local client configuration discovery can expose sensitive configuration values.

Mitigation: Discover clients only when explicitly requested, read only authorized sources, never print raw credentials, and do not use discovered cloud credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [Vulnerability findings and guidance; requested reports or SBOMs in JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coverage depends on the specified target and whether online vulnerability lookups are enabled.]

## Skill Version(s):

0.113.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
