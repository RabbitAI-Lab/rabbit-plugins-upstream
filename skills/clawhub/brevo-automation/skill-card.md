## Description: <br>
Automate Brevo (Sendinblue) tasks via Rube MCP (Composio): manage email campaigns, create/edit templates, track senders, and monitor campaign performance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to automate Brevo email marketing workflows through a connected Rube MCP account, including campaign review and updates, template creation or editing, sender lookup, and A/B test configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent using this skill can modify Brevo resources through the connected account. <br>
Mitigation: Use it only with the intended Brevo account, verify the active Rube MCP connection, and review campaign or template changes before execution. <br>
Risk: Template deletion can remove a Brevo asset if the wrong inactive template is selected. <br>
Mitigation: Before deletion, list the exact template, confirm its ID, name, and inactive status, and require explicit user approval. <br>


## Reference(s): <br>
- [Rube MCP endpoint](https://rube.app/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/sohamganatra/skills/brevo-automation) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown with tool names, workflow steps, parameters, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is intended for agents connected to Rube MCP and a verified Brevo account.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
