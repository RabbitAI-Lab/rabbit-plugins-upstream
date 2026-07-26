## Description: <br>
Validate and ingest operator-pushed agent-bom inventory JSON to produce local findings, graph, policy, provenance, and auditor-ready exports without direct cloud credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and operators use this skill when they already have canonical inventory JSON from cloud, CMDB, endpoint, or AI-agent collection workflows and need local validation, scanning, graphing, policy checks, provenance review, or exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Inventory-derived security data may leave the local machine when optional push or vulnerability enrichment is enabled. <br>
Mitigation: Verify the operator-provided push URL and enrichment endpoints before enabling those optional actions. <br>
Risk: Untrusted or unintended inventory files could produce misleading local findings. <br>
Mitigation: Run schema validation first and analyze only inventory files the operator intended to provide. <br>
Risk: Inventory and configuration may contain sensitive tokens, URL credentials, private keys, or environment values. <br>
Mitigation: Rely on the skill's redaction guidance and do not display or export raw secrets. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-ingest) <br>
- [agent-bom repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OSV vulnerability API](https://api.osv.dev/v1) <br>
- [GitHub Advisory API](https://api.github.com/advisories) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent-bom CLI to create operator-selected JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX export files.] <br>

## Skill Version(s): <br>
0.98.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
