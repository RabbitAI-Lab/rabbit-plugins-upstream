## Description:

Check vulnerabilities in a specified package/version, repository, container image, or SBOM, or inspect a specified CVE. Discover local MCP clients only when the user explicitly requests that discovery. Ask for the target when a request such as "verify" or "is this safe" does not identify one.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check named packages and versions, scan specified repositories, container images, or SBOMs, investigate advisories, and generate software supply-chain reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability checks send package identifiers, versions, and advisory IDs to external providers; repository or image scans also contact the specified host.

Mitigation: Use offline mode when network lookups are not authorized, and confirm permission before sending private package identifiers.

Risk: The skill can read local agent configuration files when client discovery is requested, and scan coverage may be incomplete when local references cannot be resolved.

Mitigation: Limit scans to the explicitly authorized target; request client discovery only when needed, and report unresolved inputs or offline coverage gaps.

## Reference(s):

- [Agent-BOM project](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown, SBOM files, Shell commands]

**Output Format:** [Findings and guidance in text, JSON, SARIF, HTML, or Markdown; SBOMs in CycloneDX or SPDX formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are scoped to the requested target; offline scans may have incomplete vulnerability coverage.]

## Skill Version(s):

0.115.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
