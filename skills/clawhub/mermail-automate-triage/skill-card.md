## Description: <br>
Create, inspect, update, select, and delete Mermail task triagers and review recent triager runs for mailbox automation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mermail](https://clawhub.ai/user/mermail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure Mermail mailbox task triage automation, inspect recent triager runs, update default triagers, and open triager-linked agent conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent triager configuration changes can affect ongoing mailbox automation. <br>
Mitigation: Review proposed trigger instructions, outputs, integrations, default-status changes, and deletion requests before approval. <br>
Risk: Deleting or replacing triagers without diagnosis can disrupt active triage workflows. <br>
Mitigation: Inspect recent triager runs, require explicit approval for destructive or default-changing actions, and verify the resulting triager list before claiming success. <br>


## Reference(s): <br>
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills) <br>
- [Triage tool map](references/tools.md) <br>
- [Mermail MCP server](https://console.mermail.app/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-automate-triage) <br>
- [Publisher profile](https://clawhub.ai/user/mermail) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, API calls] <br>
**Output Format:** [Markdown guidance with MCP tool calls and configuration summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and access to the Mermail MCP server.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
