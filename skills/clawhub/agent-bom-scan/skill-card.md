## Description: <br>
agent-bom scan checks agentic infrastructure, MCP servers, packages, container images, filesystems, SBOMs, and package provenance for security and vulnerability risk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and agent platform operators use this skill to check packages, scan container images and filesystems, inspect MCP or agent configurations, generate SBOMs, and prioritize vulnerability remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read many local AI-agent, MCP, Snowflake, and AI-tool configuration paths during discovery. <br>
Mitigation: Review the configured discovery paths before installation or full scans, and prefer targeted package, image, filesystem, or SBOM checks when a broad local inventory is not needed. <br>
Risk: The activation language is broad enough that an agent could invoke the skill for general safety or verification requests. <br>
Mitigation: Use the skill only for explicit security scans and keep autonomous invocation restricted so the user confirms scan scope before local configuration discovery. <br>
Risk: Scan lookups can contact public vulnerability databases with public package names and CVE IDs. <br>
Mitigation: Avoid scanning sensitive private package identifiers unless sharing those identifiers with the configured vulnerability services is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan) <br>
- [Project homepage](https://github.com/msaad00/agent-bom) <br>
- [PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>
- [Credential redaction source reference](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py) <br>
- [OSV vulnerability database API](https://api.osv.dev/v1) <br>
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0) <br>
- [EPSS API](https://api.first.org/data/v1/epss) <br>
- [GitHub Security Advisories API](https://api.github.com/advisories) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with optional JSON, SARIF, CycloneDX, SPDX, HTML, and shell command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce vulnerability findings, inventory data, blast-radius analysis, remediation plans, SBOMs, scan diffs, and CI gate results.] <br>

## Skill Version(s): <br>
0.98.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
