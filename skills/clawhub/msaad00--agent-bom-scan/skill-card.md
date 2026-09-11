## Description:

Open security scanner for agentic infrastructure: agents, MCP, packages, blast radius, runtime, package CVEs, container images, provenance, filesystems, and SBOMs.

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

Risk: Broad scans can read local AI-client, MCP, project, and Snowflake configuration files under the user account.

Mitigation: Review the skill before installing, and prefer narrow package, image, filesystem, or SBOM checks unless broad local discovery is required.

Risk: Mutable unpinned install or run commands can execute a build different from the reviewed release.

Mitigation: Prefer pinned commands for version 0.104.0 and verify package provenance before scanning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Source repository](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Redaction implementation](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)
- [OSV API](https://api.osv.dev/v1)
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0)
- [EPSS API](https://api.first.org/data/v1/epss)
- [GitHub Security Advisories API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, plus JSON, SARIF, CycloneDX, SPDX, and HTML outputs from the scanner when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce vulnerability findings, blast-radius analysis, remediation plans, provenance verification results, scan diffs, inventory listings, and SBOMs.]

## Skill Version(s):

0.104.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
