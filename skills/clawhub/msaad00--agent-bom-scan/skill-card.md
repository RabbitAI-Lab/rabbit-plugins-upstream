## Description:

Open security scanner for agentic infrastructure - agents, MCP, packages, blast radius, runtime, and trust for package CVEs (OSV, NVD, EPSS, KEV), container images, provenance, filesystems, and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and agent operators use this skill to check packages, MCP servers, container images, filesystems, and SBOMs for vulnerabilities, provenance, blast radius, and remediation guidance before installing or operating agentic infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner can inspect a broad set of local agent and MCP configuration paths under the user's home directory.

Mitigation: Review the discovery paths with `agent-bom where`, prefer narrow checks such as a specific package or image when possible, and avoid broad scans in sensitive environments.

Risk: Configuration scans may encounter sensitive internal endpoints or environment-derived values even though credential-like values are redacted.

Mitigation: Review the redaction behavior before scanning and do not share scan output until it has been checked for environment-specific details.

Risk: The tool sends public package names and CVE IDs to external vulnerability databases for enrichment.

Mitigation: Use the skill where those lookups are acceptable, and avoid scanning package inventories whose names should not leave the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Credential redaction implementation](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)
- [OSV vulnerability database API](https://api.osv.dev/v1)
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0)
- [EPSS API](https://api.first.org/data/v1/epss)
- [GitHub Security Advisories API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON, SARIF, CycloneDX, SPDX, or HTML report outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend scanner commands and report formats; review generated findings and broad local discovery paths before execution.]

## Skill Version(s):

0.102.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
