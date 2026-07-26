## Description: <br>
Manage Vapi voice assistants, calls, phone numbers, tools, and webhooks via Vapi REST API or CLI commands within OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[colygon](https://clawhub.ai/user/colygon) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage Vapi voice-agent resources, inspect account state, and prepare assistant, call, phone-number, tool, and webhook changes through REST API or CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable an agent to manage Vapi account resources and initiate account-changing actions or outbound calls. <br>
Mitigation: Install only for intended Vapi account management, keep VAPI_API_KEY in a secret manager, and approve account-changing actions and outbound calls case by case. <br>
Risk: Phone numbers and webhook URLs can be misconfigured during assistant, call, or event-routing workflows. <br>
Mitigation: Verify phone numbers, assistant IDs, webhook URLs, recording, consent, and compliance constraints before executing changes. <br>
Risk: The optional Vapi CLI installer downloads and runs a remote installation script. <br>
Mitigation: Avoid the remote installer unless the installation path has been independently checked or replaced with a safer official method. <br>
Risk: The artifact references a helper script that was not included in the release evidence. <br>
Mitigation: Confirm the helper script is present and reviewed before relying on REST helper workflows. <br>


## Reference(s): <br>
- [Vapi API Reference](https://api.vapi.ai/api) <br>
- [Vapi Documentation](https://docs.vapi.ai/quickstart/introduction) <br>
- [Vapi CLI](https://github.com/VapiAI/cli) <br>
- [Vapi MCP Setup](https://docs.vapi.ai/cli/mcp) <br>
- [Vapi Example Server for Node.js](https://github.com/VapiAI/example-server-javascript-node) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with inline shell commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference VAPI_API_KEY, VAPI_MODE, Vapi REST endpoints, Vapi CLI commands, and Node helper usage.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
