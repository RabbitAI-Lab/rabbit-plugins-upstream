## Description: <br>
Use Aident from agent environments to discover, verify, and operate connected integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aident-ai](https://clawhub.ai/user/aident-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to connect AI agents with Aident Loadout so they can discover integrations, check Vault connection state, execute connected app actions, and review audit history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable broad live-app action capability through connected work apps and remote tools. <br>
Mitigation: Connect only needed accounts and scopes, verify Vault status before claiming an integration is connected, and confirm send, post, update, or delete actions before execution. <br>
Risk: The setup path depends on mutable remote setup instructions. <br>
Mitigation: Review the remote setup instructions before letting an agent follow them and refresh only from trusted Aident and ClawHub release surfaces. <br>
Risk: Aident tokens may be stored locally in ~/.aident/credentials.json after authentication. <br>
Mitigation: Protect the credential file, avoid printing tokens or sensitive payloads, and remove the file when access is no longer needed. <br>


## Reference(s): <br>
- [Aident Loadout Reference](references/loadout.md) <br>
- [MCP Client Setup](references/mcp.md) <br>
- [OpenAPI Reference](references/api.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Aident Loadout](https://loadout.aident.ai) <br>
- [Aident Documentation](https://docs.aident.ai) <br>
- [ClawHub Skill Listing](https://clawhub.ai/aident-ai/skills/aident-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to fetch live CLI help and schemas, verify Vault status, and use audit history around external actions.] <br>

## Skill Version(s): <br>
0.4.0 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
