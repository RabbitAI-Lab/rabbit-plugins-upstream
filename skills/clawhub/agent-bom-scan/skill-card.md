## Description:

Check vulnerabilities in a specified package/version, repository, container image, or SBOM, or inspect a specified CVE; discover local MCP clients only when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check named dependencies, repositories, container images, SBOMs, or CVEs and to generate software inventories. Scans should stay within explicitly authorized targets, with local MCP-client discovery used only when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability lookups transmit package identifiers, versions, and advisory IDs to external providers; private identifiers may be sensitive.

Mitigation: Confirm permission before querying private identifiers, or use offline mode and report the resulting coverage gaps.

Risk: Security scanner coverage was partial, so some referenced paths or items could not be resolved and the available evidence is incomplete.

Mitigation: Treat the clean verdict as limited evidence and review the authorized scan scope and unresolved coverage before relying on results.

Risk: Local MCP-client discovery can involve configuration paths that contain sensitive settings.

Mitigation: Discover local MCP clients only when the user explicitly requests it, read only authorized sources, and never print raw credentials.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [Security Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, SARIF, HTML, CycloneDX/SPDX SBOMs, Shell commands]

**Output Format:** [Text or files in JSON, Markdown, SARIF, HTML, CycloneDX, or SPDX formats, depending on the requested task]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the supplied target and available vulnerability data; offline scans may have incomplete advisory coverage.]

## Skill Version(s):

0.115.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
