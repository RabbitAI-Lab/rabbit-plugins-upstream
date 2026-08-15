## Description:

Open security scanner for agentic infrastructure, including agents, MCP, packages, package CVEs, container images, provenance, filesystems, and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to scan agentic infrastructure, MCP configurations, packages, container images, filesystems, and SBOMs for vulnerabilities, provenance signals, blast radius, and remediation priorities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broadly inspect local agent and MCP configuration files from the user's home directory.

Mitigation: Review the listed discovery paths before enabling the skill and run scans only when local agent or MCP configuration inspection is intended.

Risk: Broad activation phrases could lead an agent to invoke a full scan for vague safety or dependency questions.

Mitigation: Keep autonomous invocation restricted and require explicit scan scope before running full discovery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Credential redaction reference](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured scanner guidance with optional CLI commands and report formats such as JSON, SARIF, CycloneDX, SPDX, and HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide use of local scans, vulnerability lookups, SBOM generation, provenance checks, diffs, and remediation planning.]

## Skill Version(s):

0.100.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
