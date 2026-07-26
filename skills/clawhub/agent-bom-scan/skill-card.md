## Description: <br>
Open security scanner for agentic infrastructure, including agents, MCP, packages, blast radius, runtime, trust for package CVEs, container images, provenance, filesystems, and SBOMs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security engineers use this skill to check packages, scan containers or filesystems, verify provenance, generate SBOMs, and prioritize remediation for agentic infrastructure risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags this as suspicious because broad or vague scan prompts may inventory local AI-agent and service configuration files in the user's home directory. <br>
Mitigation: Prefer explicit scan targets such as a named package, container image, SBOM, or directory, and use narrow or no-discovery modes when broad local configuration discovery is not intended. <br>
Risk: The scanner may read local agent configuration paths and user-provided SBOM files as part of its inventory workflow. <br>
Mitigation: Review the intended scope before installation or execution, and ask before scanning paths outside the user's home directory. <br>
Risk: Package names and CVE IDs may be sent to vulnerability databases for lookup and enrichment. <br>
Mitigation: Use the skill only when those public identifiers can be shared with OSV, NVD, EPSS, or GitHub Advisories, and avoid submitting secrets or private configuration contents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-scan) <br>
- [agent-bom source](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom) <br>
- [Credential redaction source](https://github.com/msaad00/agent-bom/blob/main/src/agent_bom/security.py) <br>
- [OSV vulnerability database](https://api.osv.dev/v1) <br>
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0) <br>
- [EPSS API](https://api.first.org/data/v1/epss) <br>
- [GitHub Security Advisories API](https://api.github.com/advisories) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Concise recommendations and scan guidance, with JSON, SARIF, HTML, CycloneDX, SPDX, or Markdown outputs when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can guide local scans of package, image, filesystem, provenance, SBOM, and agent configuration evidence.] <br>

## Skill Version(s): <br>
0.98.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
