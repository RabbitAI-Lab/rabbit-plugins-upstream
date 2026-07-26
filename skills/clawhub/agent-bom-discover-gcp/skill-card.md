## Description: <br>
Discovers GCP-hosted AI agent and MCP-relevant assets from operator-approved projects, emits canonical agent-bom inventory JSON, and can scan that inventory when requested. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud engineers, and security reviewers use this skill to inventory Vertex AI, Cloud Run, Cloud Functions, GKE, and related agentic GCP infrastructure with operator-controlled credentials. It helps produce canonical agent-bom inventory and optional scan findings without handing agent-bom long-lived GCP credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Overbroad GCP credentials could expose more project inventory than intended. <br>
Mitigation: Use read-only or short-lived GCP credentials, confirm the selected project, and avoid broad production credentials unless they are necessary for the inventory. <br>
Risk: Inventory output may contain sensitive resource or environment metadata. <br>
Mitigation: Write inventory only to an operator-selected path, review the JSON before sharing it, and rely on the skill's credential redaction behavior for credential-like values. <br>


## Reference(s): <br>
- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, json] <br>
**Output Format:** [Markdown with bash command blocks and JSON file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operator-selected inventory JSON and optional agent-bom scan findings JSON; credentials remain in the operator environment.] <br>

## Skill Version(s): <br>
0.98.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
