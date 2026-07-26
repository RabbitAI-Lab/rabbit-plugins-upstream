## Description: <br>
Manage n8n workflows from OpenClaw via the n8n REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dilomcfly](https://clawhub.ai/user/dilomcfly) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations teams use this skill to inspect, create, activate, deactivate, trigger, and debug n8n workflows in n8n Cloud or self-hosted instances. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-suggested n8n API commands can create, change, delete, activate, deactivate, or trigger workflows. <br>
Mitigation: Use a test or non-production n8n instance first, require explicit confirmation before mutating or triggering workflows, and export or back up workflows before making changes. <br>
Risk: The skill relies on an n8n API key that may provide broad workflow access. <br>
Mitigation: Use the least-privilege key available, keep the key scoped to the intended environment, and rotate it if it is exposed. <br>


## Reference(s): <br>
- [n8n REST API Endpoint Reference](references/api-endpoints.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and REST API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl commands that use N8N_API_URL and N8N_API_KEY to call n8n REST API endpoints.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
