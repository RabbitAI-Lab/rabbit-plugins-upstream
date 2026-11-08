## Description:

Builds, deploys, and manages n8n workflows through the REST API, including webhook flows, scheduled tasks, AI agents, data syncs, conditional logic, and error handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deyogaid](https://clawhub.ai/user/deyogaid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation builders use this skill to design n8n workflow JSON and manage workflows through an n8n instance. It supports webhook, scheduled, AI, database, and service integration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default instructions activate live automations without clearly requiring authorization for their ongoing effects.

Mitigation: Before activating each workflow, require authorization and review its triggers, connected accounts, recipients, and data changes.

Risk: Workflow data may be sent to connected services, including OpenAI, Google Sheets, or Slack.

Mitigation: Review which chat or lead information reaches each service, and use a test n8n instance, a narrowly scoped API key, and HTTPS for remote connections.

## Reference(s):

- [n8n Workflow Patterns](artifact/references/workflow-patterns.md)
- [n8n Workflow JSON Schema Reference](artifact/references/workflow-schema.md)

## Skill Output:

**Output Type(s):** [Configuration, JSON, Shell commands, Guidance]

**Output Format:** [Markdown instructions with n8n workflow JSON and Bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow JSON can be submitted to an n8n instance using the supplied API commands.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
