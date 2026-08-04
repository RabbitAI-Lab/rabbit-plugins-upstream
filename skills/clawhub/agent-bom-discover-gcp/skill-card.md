## Description: <br>
Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to inventory Vertex AI, Cloud Run, Cloud Functions, GKE, and other agentic GCP infrastructure into canonical agent-bom inventory JSON. It supports optional local scanning of that inventory when the operator explicitly asks for findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use existing GCP credentials to read project and resource inventory. <br>
Mitigation: Run it only for intended projects with read-only Application Default Credentials, workload identity, or short-lived scoped service account credentials. <br>
Risk: Inventory output may contain cloud resource metadata that should stay under operator control. <br>
Mitigation: Confirm the project, region, and output path before execution, and write inventory only to an operator-selected local path. <br>
Risk: Long-lived service account keys or credential values could be exposed if pasted into chat or printed. <br>
Mitigation: Do not provide service account JSON, OAuth refresh tokens, bearer tokens, or private keys in chat, and do not print credential values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp) <br>
- [agent-bom repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, JSON files] <br>
**Output Format:** [Markdown with inline bash commands and JSON file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operator-selected inventory JSON and optional agent-bom findings JSON; credential-like values are redacted before persistence or export.] <br>

## Skill Version(s): <br>
0.98.3 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
