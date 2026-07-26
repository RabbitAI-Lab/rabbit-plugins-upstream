## Description: <br>
Forwards state, action, or historical user requests to a configured n8n_dispatch MCP service and returns the workflow response. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enchantedmotorcycle](https://clawhub.ai/user/enchantedmotorcycle) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to route agent requests to a trusted n8n workflow for state checks, actions, or historical lookups. It is useful when OpenClaw should delegate request handling to an existing n8n_dispatch service and return that service's response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User prompts and request labels are forwarded to the configured n8n_dispatch service, which may expose sensitive data if the endpoint or workflow is not trusted. <br>
Mitigation: Install only with a controlled or trusted n8n_dispatch service, avoid sending secrets or sensitive personal data unless the workflow is approved for it, and prefer HTTPS or a trusted local/private endpoint. <br>
Risk: Action requests may trigger behavior in the downstream n8n workflow based on user-provided input. <br>
Mitigation: Add input validation and confirmation gates in n8n for workflows that perform actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/enchantedmotorcycle/skills/n8n-dispatch) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Command definition](artifact/commands.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Text responses from the configured n8n workflow with Markdown usage examples in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The dispatch command accepts requestType and text, forwards them as JSON to the configured n8n_dispatch MCP service, and prints the returned response.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
