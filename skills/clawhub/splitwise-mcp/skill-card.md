## Description: <br>
Access and manage Splitwise expenses, groups, friends, balances, notifications, categories, and currencies through a registered MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to Splitwise so it can answer questions about shared expenses and perform account-affecting expense or group actions through the Splitwise API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify Splitwise account data, including creating, editing, deleting expenses and changing group membership. <br>
Mitigation: Use explicit confirmations before account-changing actions, review previews carefully, and verify group, user, and expense identifiers before execution. <br>
Risk: The Splitwise API key authorizes account access and is attached to requests made by the MCP server. <br>
Mitigation: Keep SPLITWISE_API_KEY private in the MCP environment or local .env file, avoid exposing it in logs or shared configs, and rotate it if exposed. <br>
Risk: Custom split updates replace the full users array, and deleted expenses are soft-deleted with restoration handled in the Splitwise web app. <br>
Mitigation: Review the complete split before updates and confirm delete actions only after checking the target expense. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/chrischall/skills/splitwise-mcp) <br>
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp) <br>
- [Splitwise API app registration](https://secure.splitwise.com/apps/register) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Configuration, Guidance] <br>
**Output Format:** [Natural-language guidance with MCP tool calls and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and modify Splitwise account data when the configured server executes tool calls.] <br>

## Skill Version(s): <br>
2.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
