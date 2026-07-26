## Description: <br>
Kakiyo Skill helps agents manage Kakiyo LinkedIn outreach campaigns, prospects, AI agents, analytics, workspaces, webhooks, and do-not-contact lists through the Kakiyo MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyberboyayush](https://clawhub.ai/user/cyberboyayush) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Kakiyo users and agencies use this skill to configure the Kakiyo MCP server and ask an agent to inspect, create, pause, resume, or update outreach campaigns, prospects, agents, workspaces, webhooks, and do-not-contact entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad control over Kakiyo outreach, prospects, workspaces, do-not-contact entries, and webhook destinations. <br>
Mitigation: Install only for trusted Kakiyo accounts, use a dedicated revocable API key when possible, and review campaign, prospect, workspace, DNC, and webhook changes before execution. <br>
Risk: Resume, delete, remove, and webhook URL actions can restart outreach, remove resources, or change where event data is sent. <br>
Mitigation: Require explicit confirmation for high-impact actions and verify webhook destinations before creating, updating, or deleting them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cyberboyayush/skills/kakiyo) <br>
- [Kakiyo documentation](https://docs.kakiyo.com) <br>
- [Kakiyo MCP server details](https://docs.kakiyo.com/mcp-server) <br>
- [Kakiyo API reference](https://docs.kakiyo.com/api-reference) <br>
- [Kakiyo dashboard](https://app.kakiyo.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mcporter and KAKIYO_API_KEY; commands call the Kakiyo MCP server and commonly request JSON output.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
