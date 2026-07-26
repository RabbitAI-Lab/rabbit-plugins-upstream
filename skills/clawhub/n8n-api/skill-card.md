## Description: <br>
Operate n8n via its public REST API from OpenClaw. Use for workflow management, executions, and automation tasks such as listing, creating, publishing, triggering, or troubleshooting. Works with both self-hosted n8n and n8n Cloud. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage n8n workflows, executions, credentials, projects, tags, variables, data tables, users, audits, and webhooks through the n8n public REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live n8n workflows and resources when used with a powerful API key. <br>
Mitigation: Use a dedicated least-privileged API key and explicitly review production-changing actions such as activating, deactivating, retrying, deleting, transferring, changing roles, or triggering production webhooks. <br>
Risk: Experiments against production webhooks or the self-hosted API playground can operate on real data. <br>
Mitigation: Use a test workflow or a separate test instance for experiments before applying changes to production. <br>


## Reference(s): <br>
- [n8n API Endpoint Reference](assets/n8n-api-endpoints.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands, endpoint references, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses N8N_API_BASE_URL and N8N_API_KEY for generated API examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
