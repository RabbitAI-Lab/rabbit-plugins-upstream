## Description:

Check vulnerabilities in a specified package/version, repository, container image, or SBOM, or inspect a specified CVE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use the skill to assess specified packages, repositories, container images, and SBOMs for vulnerabilities, investigate advisories, and prepare remediation or compliance guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability lookups send package identifiers, versions, and advisory IDs to providers, which may expose private identifiers.

Mitigation: Confirm authorization before querying private identifiers, or use offline mode and report its coverage gaps.

Risk: Local MCP client discovery can read configuration files that may contain sensitive settings.

Mitigation: Discover clients only when explicitly requested, read only authorized targets, and never print raw credentials.

## Reference(s):

- [Project repository](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, JSON, Markdown, SBOMs]

**Output Format:** [Markdown guidance and scanner outputs such as JSON, SARIF, CycloneDX, or SPDX]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the specified target and requested format; offline scans may have incomplete advisory coverage.]

## Skill Version(s):

0.113.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
