## Description:

Open security scanner for agentic infrastructure, including agents, MCP, packages, blast radius, runtime, package CVEs, container images, provenance, filesystems, and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check packages for vulnerabilities, scan containers and filesystems, verify package provenance, map blast radius, plan remediation, and generate SBOMs for agentic infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full discovery can read local AI agent, MCP, IDE, and Snowflake configuration files while building an inventory and assessing blast radius.

Mitigation: Use narrower package, image, provenance, filesystem, or SBOM checks when full discovery is not needed, and review the listed file-read scope and redaction behavior before scanning shared or sensitive machines.

Risk: Broad activation wording may trigger local discovery in situations where the user only wanted a targeted safety answer.

Mitigation: Invoke full scans only for explicit security scanning tasks, prefer targeted commands for package or CVE questions, and ask before scanning paths outside the user's home directory.

## Reference(s):

- [Agent BOM project](https://github.com/msaad00/agent-bom)
- [Agent BOM PyPI package](https://pypi.org/project/agent-bom/)
- [Agent BOM OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Credential redaction implementation](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)
- [OSV vulnerability database API](https://api.osv.dev/v1)
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0)
- [EPSS API](https://api.first.org/data/v1/epss)
- [GitHub Security Advisories API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown, JSON, SARIF, CycloneDX/SPDX SBOM, HTML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce vulnerability findings, blast-radius analysis, remediation priorities, inventory data, provenance checks, CI gate results, and SBOM files.]

## Skill Version(s):

0.101.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
