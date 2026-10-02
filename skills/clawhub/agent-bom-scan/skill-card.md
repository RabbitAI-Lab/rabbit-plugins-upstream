## Description:

Scans agent infrastructure, dependencies, container images, and SBOMs for vulnerabilities and provides provenance checks and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use the skill to check package and container vulnerabilities, assess their impact on agent infrastructure, verify package provenance, and generate scan reports or SBOMs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full scans and inventory modes may read sensitive agent and service configuration files in the home directory.

Mitigation: Review discovery paths with the where command and prefer targeted package, image, SBOM, CVE, or path checks before full scans.

## Reference(s):

- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Credential redaction source](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Scan reports, SBOMs]

**Output Format:** [Markdown, JSON, SARIF, HTML, CycloneDX, or SPDX as requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide prioritized remediation advice and severity-based CI gate results.]

## Skill Version(s):

0.107.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
