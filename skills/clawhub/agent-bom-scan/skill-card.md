## Description:

Scans agent infrastructure, dependencies, container images, and SBOMs for vulnerabilities and package provenance risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to check package and container vulnerabilities, assess agent and MCP dependencies, verify package integrity, and plan remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad discovery scans may inventory sensitive local agent, MCP, and IDE configuration files.

Mitigation: Review discovery paths with the where command and prefer explicit package, image, SBOM, or path targets; run full discovery only when comfortable with its scope.

## Reference(s):

- [Project homepage (publisher-listed)](https://github.com/msaad00/agent-bom)
- [Package on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Credential-redaction implementation (publisher-listed)](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Security findings, Remediation guidance, Shell commands]

**Output Format:** [Markdown or structured JSON/SARIF; CycloneDX/SPDX SBOM when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unknown-severity CVEs remain unresolved.]

## Skill Version(s):

0.106.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
