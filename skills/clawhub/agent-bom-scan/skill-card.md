## Description:

Check a specified package/version, repository, container image, SBOM, or CVE for vulnerability and supply-chain security information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check specified packages, repositories, container images, SBOMs, or CVEs for vulnerability and supply-chain information. It can also generate SBOMs and scoped reports or remediation guidance for a requested target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and could not resolve several path-like references.

Mitigation: Review flagged configuration-path references and external service URLs before installing, and proceed only if they fit your needs.

Risk: Online vulnerability lookups send package identifiers, versions, and advisory IDs to providers; image and repository scans contact the requested registry or host.

Mitigation: Confirm permission before querying private package identifiers, or use offline mode and report its coverage gaps.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Security Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [Credential redaction implementation reference](https://github.com/koda-ai-studio/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [Analysis, Files, Guidance, Shell commands]

**Output Format:** [Text analysis and remediation guidance; optional JSON, SARIF, Markdown, HTML, CycloneDX, or SPDX reports and SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Format and contents depend on the requested target and report type; report files are written to requested output paths.]

## Skill Version(s):

0.114.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
