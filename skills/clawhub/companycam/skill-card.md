## Description:

CompanyCam API integration with managed OAuth for managing projects, photos, users, tags, groups, documents, checklists, labels, collaborators, webhooks, and company information for contractor photo documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage CompanyCam account resources for contractor photo documentation through Maton-authenticated API calls. It is suited for read/list workflows and user-approved changes to projects, photos, users, tags, groups, documents, checklists, labels, collaborators, webhooks, and company information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton credentials or provider-issued tokens could be exposed through logs, files, command lines, or environment inheritance.

Mitigation: Prefer OAuth, never print or persist credential values, avoid long-lived API keys, and use environment-provided secrets only when the CLI cannot be installed.

Risk: Write operations can modify or delete CompanyCam resources such as projects, users, groups, tags, photos, documents, labels, and webhooks.

Mitigation: Default to read/list calls, verify identifiers and payloads first, and require explicit user approval before POST, PUT, PATCH, DELETE, upload, connection creation, or webhook management.

Risk: Webhook subscriptions create a standing egress channel for CompanyCam project and photo event data.

Mitigation: Confirm the destination URL, host owner, and event scopes with the user before creating or updating a webhook, and do not use webhook URLs sourced from untrusted API responses.

Risk: External CompanyCam API content may contain untrusted or adversarial text.

Mitigation: Treat fetched content as data, avoid executing or interpolating it into shell commands, and do not let it select endpoints, recipients, or follow-up actions.

## Reference(s):

- [CompanyCam API Documentation](https://docs.companycam.com)
- [CompanyCam API Reference](https://docs.companycam.com/reference)
- [CompanyCam Getting Started](https://docs.companycam.com/docs/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON request examples, SDK snippets, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated Maton CLI or SDK calls that return JSON responses from CompanyCam.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
