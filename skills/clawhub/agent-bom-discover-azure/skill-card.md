## Description: <br>
Discovers Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emits canonical agent-bom inventory JSON, and can scan it without giving agent-bom long-lived Azure credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud security engineers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, and related agentic Azure infrastructure as canonical agent-bom inventory. It supports discovery-only collection with an optional local agent-bom scan when the operator asks for findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the operator's existing Azure login context to read cloud metadata. <br>
Mitigation: Run it only against approved subscriptions with read-only Azure roles or short-lived service principal credentials. <br>
Risk: The generated inventory may contain sensitive cloud metadata even when credential-like values are redacted. <br>
Mitigation: Choose the output path deliberately and review the inventory before sharing, scanning, or pushing it elsewhere. <br>
Risk: Credential variables or token material could be exposed if copied into prompts or logs outside the skill workflow. <br>
Mitigation: Do not ask users to paste client secrets, access tokens, or connection strings, and do not print credential values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure) <br>
- [agent-bom repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI project](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with bash command blocks; generated Azure inventory and optional scan findings are JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Discovery writes to an operator-selected path, uses redacted credential material, and defaults to discover-only unless the operator asks for a scan.] <br>

## Skill Version(s): <br>
0.98.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
