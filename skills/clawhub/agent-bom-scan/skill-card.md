## Description: <br>
Open security scanner for agentic infrastructure, including agents, MCP servers, package CVEs, container images, provenance checks, filesystems, and SBOMs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and agent operators use this skill to check package and container risk, scan agent and MCP infrastructure, verify package provenance, generate SBOMs, and prioritize remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The discovery workflow can read many local AI tool and MCP configuration files. <br>
Mitigation: Review the discovered paths first and prefer targeted package, image, SBOM, or path scans before running a full scan. <br>
Risk: Broad safety prompts may invoke scanning beyond the user's intended target. <br>
Mitigation: Use explicit commands and require user confirmation before scanning broad locations or paths outside the expected scope. <br>
Risk: Vulnerability lookups send public package names and CVE IDs to external databases. <br>
Mitigation: Use the skill only when those lookups are acceptable and avoid providing private package identifiers unless disclosure is approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan) <br>
- [Project homepage](https://github.com/msaad00/agent-bom) <br>
- [PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>
- [Credential redaction reference](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Concise recommendations, vulnerability findings, remediation plans, SARIF, JSON, Markdown, HTML, and CycloneDX/SPDX SBOMs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include CVE, severity, exploit probability, provenance, blast-radius, and remediation details for the requested scan target.] <br>

## Skill Version(s): <br>
0.98.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
