## Description:

n8n Builder helps agents design, create, deploy, activate, verify, and manage n8n workflow automations through workflow JSON and the n8n REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kassimisai](https://clawhub.ai/user/kassimisai)

### License/Terms of Use:


## Use Case:

Developers and automation builders use this skill to create, deploy, and manage n8n workflows for webhook flows, scheduled jobs, AI agents, database syncs, conditional logic, error handling, and real estate automation patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, activate, execute, and delete workflows on a live n8n instance.

Mitigation: Require explicit approval before running API commands that change workflow state or execute automations.

Risk: The n8n API key grants broad access to workflow and credential metadata.

Mitigation: Use a narrowly scoped API key where possible and keep N8N_API_KEY out of logs, prompts, and generated files.

Risk: Pointing N8N_URL at the wrong instance can affect unintended automations.

Mitigation: Set N8N_URL only to the intended trusted HTTPS n8n instance and confirm it before write, activation, execution, or delete operations.

Risk: Generated workflows may move data between connected services once activated.

Mitigation: Review workflow JSON, credentials, destinations, and error handling before activation.

## Reference(s):

- [n8n Workflow JSON Schema Reference](references/workflow-schema.md)
- [n8n Workflow Patterns](references/workflow-patterns.md)
- [ClawHub skill page](https://clawhub.ai/kassimisai/skills/n8n-builder)
- [Publisher profile](https://clawhub.ai/user/kassimisai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with n8n workflow JSON, shell commands, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce workflow definitions and API commands that act on a configured n8n instance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
