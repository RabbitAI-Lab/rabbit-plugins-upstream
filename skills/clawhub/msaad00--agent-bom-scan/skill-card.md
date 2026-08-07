## Description:

Open security scanner for agentic infrastructure, including agents, MCP, packages, blast radius, runtime, trust, package CVEs, container images, provenance, filesystems, and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check packages, scan container images and filesystems, verify package integrity, map CVE blast radius, and generate SBOMs for agentic infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full discovery scans can read many local agent and service configuration files, including files that may describe MCP servers, credentials, and local tool setup.

Mitigation: Prefer explicit package checks, image scans, or user-selected filesystem paths, and review the listed discovery paths before running broad inventory scans.

Risk: Loose activation language such as safety checks and dependency scans can trigger broad inventory behavior when a narrower check would be sufficient.

Mitigation: Ask the agent to use specific commands and targets, such as a named package/version, container image, SBOM file, or selected directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Credential redaction reference](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, JSON, SARIF, CycloneDX, and SPDX examples where requested by the user workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce package vulnerability findings, image and filesystem scan summaries, provenance verification results, blast-radius analysis, remediation guidance, inventories, diffs, and SBOM output.]

## Skill Version(s):

0.99.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
