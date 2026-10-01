## Description:

Scans agent and MCP environments, packages, container images, filesystems, and SBOMs for vulnerabilities and supply-chain risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to check dependencies, images, and agent or MCP environments for vulnerabilities, assess impact, and plan remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad scans can inventory local agent and service configuration files, including sensitive environments.

Mitigation: Review discovery paths first; prefer explicit package, image, SBOM, or selected-path scans, and avoid full scans on sensitive machines unless local inventory exposure is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [Credential redaction implementation](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [Security findings, Remediation guidance, Shell commands, SBOMs]

**Output Format:** [Text or Markdown guidance; optional JSON, SARIF, HTML, CycloneDX, or SPDX scan output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output format and scan scope depend on the requested operation.]

## Skill Version(s):

0.107.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
