## Description: <br>
Manage Vapi voice assistants, calls, phone numbers, tools, and webhooks via the Vapi REST API or CLI for voice agent operations and integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[colygon](https://clawhub.ai/user/colygon) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage Vapi voice-agent resources, including assistants, calls, phone numbers, tools, and webhooks. It supports read-only inspection and account-changing operations through REST helper commands or the Vapi CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Vapi API keys can grant access to voice-agent resources if exposed. <br>
Mitigation: Store VAPI_API_KEY in a secret manager or trusted environment variable and avoid pasting it into public logs. <br>
Risk: Assistant, phone, webhook, and outbound-call changes can affect live voice-agent operations. <br>
Mitigation: Use read-only list or get operations first and require explicit approval before creating assistants, changing phone or webhook settings, or starting outbound calls. <br>
Risk: The optional curl-to-bash CLI installer executes a remote install script. <br>
Mitigation: Inspect or avoid the installer and prefer the REST helper or a vetted CLI installation path. <br>
Risk: A custom VAPI_BASE_URL can redirect API requests to an unintended destination. <br>
Mitigation: Leave VAPI_BASE_URL unset unless the alternate endpoint is trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/colygon/skills/vapi) <br>
- [Vapi docs introduction](https://docs.vapi.ai/quickstart/introduction) <br>
- [Vapi API reference](https://api.vapi.ai/api) <br>
- [Vapi CLI documentation](https://docs.vapi.ai/cli) <br>
- [Vapi MCP documentation](https://docs.vapi.ai/cli/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses from helper commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires VAPI_API_KEY for API operations; account-changing actions and outbound calls should require explicit user approval.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
