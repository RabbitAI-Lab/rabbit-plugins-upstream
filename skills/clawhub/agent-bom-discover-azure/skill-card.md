## Description: <br>
Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and cloud security engineers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, Azure ML, and related agentic infrastructure as canonical agent-bom JSON. The workflow supports local discovery and optional scan reporting without handing agent-bom long-lived Azure credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Azure discovery can expose subscription and service metadata if the generated inventory is shared without review. <br>
Mitigation: Use a least-privilege read-only Azure identity, inventory only approved subscriptions, and review generated inventory before sharing it. <br>
Risk: Pasted client secrets, access tokens, or connection strings could be captured in an agent transcript or local output. <br>
Mitigation: Use the operator's existing Azure identity chain and do not paste or print credential values. <br>
Risk: Using credentials with broader permissions than required increases blast radius if the operator environment is compromised. <br>
Mitigation: Prefer read-only Azure credentials from Azure CLI, workload identity, managed identity, or short-lived service principal flows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure) <br>
- [agent-bom source repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON inventory or findings files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operator-selected local inventory JSON and, when requested, local agent-bom scan findings JSON.] <br>

## Skill Version(s): <br>
0.98.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
