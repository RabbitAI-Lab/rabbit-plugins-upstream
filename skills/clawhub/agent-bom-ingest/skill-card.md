## Description: <br>
Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors for local findings, graph, policy, provenance, and auditor-ready exports without giving agent-bom direct cloud credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, security engineers, platform operators, and auditors use this skill when they already have canonical inventory JSON and need local validation, scanning, graphing, policy checks, provenance review, or export guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads operator-selected inventory JSON that may contain sensitive asset or package details. <br>
Mitigation: Run it only on inventory files intended for analysis, validate the schema before trusting the inventory, and choose export paths appropriate for the data sensitivity. <br>
Risk: Optional control-plane push can send inventory data to a configured remote endpoint and uses an API token. <br>
Mitigation: Use optional push only with an operator-owned AGENT_BOM_PUSH_URL, keep AGENT_BOM_API_KEY in environment variables, and do not print tokens or URL credentials. <br>
Risk: Optional vulnerability enrichment may contact external OSV or GitHub Advisory APIs. <br>
Mitigation: Use network enrichment only where external security-intelligence lookups are allowed by policy. <br>


## Reference(s): <br>
- [agent-bom source](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI project](https://pypi.org/project/agent-bom/) <br>
- [OSV vulnerability API](https://api.osv.dev/v1) <br>
- [GitHub Advisory Database API](https://api.github.com/advisories) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and export-format recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX outputs produced by agent-bom.] <br>

## Skill Version(s): <br>
0.98.3 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
