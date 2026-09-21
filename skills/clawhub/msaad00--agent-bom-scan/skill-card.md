## Description:

Open security scanner for agentic infrastructure covering agents, MCP, packages, blast radius, runtime, package CVEs, container images, provenance, filesystems, and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check package and container vulnerabilities, verify package provenance, scan filesystems or SBOMs, and prioritize remediation for agent and MCP environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default discovery scans can read sensitive agent, MCP, developer, and cloud configuration files from the user's home directory.

Mitigation: Prefer targeted package checks, image scans, or explicit SBOM scans; run broad discovery only after reviewing the disclosed file-read paths.

Risk: Local configuration contents may be inspected during discovery scans.

Mitigation: Review credential redaction behavior before scanning and avoid broad discovery in environments with sensitive local configuration unless the operator accepts that exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [Credential redaction source](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, code snippets, JSON examples, and recommendations for scanner outputs such as SARIF, JSON, CycloneDX, or SPDX.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide CLI and MCP-server use; generated scan artifacts depend on the explicit agent-bom command and output path selected by the user.]

## Skill Version(s):

0.105.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
