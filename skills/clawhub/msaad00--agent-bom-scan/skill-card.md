## Description:

Open security scanner for agentic infrastructure: agents, MCP, packages, blast radius, runtime, trust for package CVEs, container images, provenance, filesystems, and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to check packages, scan containers and filesystems, verify package provenance, generate SBOMs, and prioritize vulnerability remediation for agentic infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner can broadly inventory local agent and tool configuration files that may reveal private infrastructure details or sensitive context.

Mitigation: Review discovery paths with `agent-bom where`, avoid broad scans unless a full inventory is intended, and run scans in a restricted environment when local configs may be sensitive.

Risk: Unpinned package execution paths may run code that differs from the reviewed release.

Mitigation: Pin the reviewed version 0.104.0 or use the reviewed container image tag before deploying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [PyPI project](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Redaction logic](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)
- [OSV API](https://api.osv.dev/v1)
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0)
- [FIRST EPSS API](https://api.first.org/data/v1/epss)
- [GitHub Security Advisories API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands, JSON examples, and scanner output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce SARIF, JSON, HTML, Markdown, CycloneDX, or SPDX outputs through the underlying scanner.]

## Skill Version(s):

0.104.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
