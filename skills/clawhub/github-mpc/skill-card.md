## Description: <br>
Verifies and configures required MCP servers, especially Atlassian and GitHub, to enable Product Guide Writer integrations and guide setup when missing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsvetelin-kulinski](https://clawhub.ai/user/tsvetelin-kulinski) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and documentation workflow users use this skill to check whether required Product Guide Writer MCP integrations are available, authenticate Atlassian and GitHub access, and follow setup guidance when a server is missing or misconfigured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tokens or service credentials may be exposed during MCP setup. <br>
Mitigation: Use least-privilege or fine-grained tokens where possible and avoid pasting secrets into chat or committed files. <br>
Risk: MCP packages, server names, or remote endpoints may be misconfigured before use. <br>
Mitigation: Verify MCP package names, server identifiers, endpoints, and workspace access before enabling the integrations. <br>
Risk: Optional Figma or Elasticsearch integrations can expand the systems available to the agent. <br>
Mitigation: Enable optional integrations only when needed and grant scoped access for the specific workflow. <br>


## Reference(s): <br>
- [Atlassian remote MCP endpoint](https://mcp.atlassian.com/v1/mcp) <br>
- [GitHub personal access tokens](https://github.com/settings/tokens) <br>
- [GT Confluence space](https://trading212.atlassian.net/wiki/spaces/gt) <br>
- [ClawHub skill page](https://clawhub.ai/tsvetelin-kulinski/skills/github-mpc) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code snippets, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with checklists, JSON configuration snippets, tool-call examples, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Focuses on MCP availability checks, authentication validation, and setup troubleshooting for named Product Guide Writer integrations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
