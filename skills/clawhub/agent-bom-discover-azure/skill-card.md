## Description: <br>
Discover Azure-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived Azure credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and cloud security engineers use this skill to inventory Azure OpenAI, Container Apps, AKS, Functions, ML, and related agentic Azure infrastructure as canonical agent-bom inventory. It supports discovery-first workflows that can optionally scan the resulting local inventory when the operator asks for findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads Azure identity configuration and token-cache files when using the operator's existing Azure credential chain. <br>
Mitigation: Use a read-only Azure account or scoped service principal, avoid environments where Azure token-cache access is not acceptable, and do not paste or print secrets. <br>
Risk: Inventory output can describe Azure resources and service metadata. <br>
Mitigation: Write inventory only to an operator-selected path and review the local JSON before sharing or scanning it. <br>


## Reference(s): <br>
- [agent-bom homepage](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-azure) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON inventory guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operator-reviewed commands and guidance for writing canonical local inventory JSON and optional agent-bom scan findings.] <br>

## Skill Version(s): <br>
0.98.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
