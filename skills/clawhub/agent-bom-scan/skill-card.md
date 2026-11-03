## Description:

Check vulnerabilities in a specified package/version, repository, container image, or SBOM, or inspect a specified CVE. Discover local MCP clients only when the user explicitly requests that discovery. Ask for the target when a request such as "verify" or "is this safe" does not identify one.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and security engineers use this skill to check a named package, repository, container image, SBOM, or advisory and to produce vulnerability analysis or an SBOM for the requested target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability lookups disclose package identifiers, versions, and advisory IDs to external providers; repository or image scans also contact the requested host.

Mitigation: Confirm permission before sending private identifiers, or use offline mode and report any resulting coverage gaps.

Risk: Explicitly requested client discovery can read local configuration files that may contain sensitive information.

Mitigation: Discover clients only when the user requests that scope; do not expose credentials or upload configuration contents.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [Credential redaction notes](https://github.com/koda-ai-studio/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Vulnerability findings and guidance in text or structured reports; SBOMs in CycloneDX or SPDX, plus example commands and configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the supplied target and advisory coverage; offline scans may have coverage gaps.]

## Skill Version(s):

0.113.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
