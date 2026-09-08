## Description:

Open security scanner for agentic infrastructure, including agents, MCP, packages, container images, provenance, filesystems, and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check packages, container images, SBOMs, filesystems, and agent or MCP configurations for vulnerabilities, provenance, blast radius, and remediation priorities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A default scan can read many local AI and tooling configuration files.

Mitigation: Review the discovery paths with the provided where command before running a full scan, and prefer explicit package, image, SBOM, filesystem, or provenance commands for narrower checks.

Risk: Broad activation wording could cause a scanner run when the user wanted a narrower safety check.

Mitigation: Use explicit commands for the intended target, such as package, image, SBOM, filesystem, or provenance checks, before escalating to a full discovery scan.

Risk: Vulnerability results can include unknown or pending severity data.

Mitigation: Treat unknown severity as unresolved and preserve CVE IDs in the result so reviewers can follow up instead of assuming the finding is benign.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [agent-bom Source Repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI Package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Credential Redaction Reference](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)
- [OSV Vulnerability Database API](https://api.osv.dev/v1)
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0)
- [FIRST EPSS API](https://api.first.org/data/v1/epss)
- [GitHub Security Advisories API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, SARIF, HTML, CycloneDX, SPDX, and concise text recommendations depending on the selected command and consumer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce allow, warn, or block guidance, CVE findings, provenance checks, SBOMs, scan diffs, inventory output, and remediation plans.]

## Skill Version(s):

0.103.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
