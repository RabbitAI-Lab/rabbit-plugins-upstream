## Description:

CompanyCam API integration with managed OAuth for managing CompanyCam projects, photos, users, tags, groups, documents, checklists, labels, collaborators, webhooks, and company information through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, contractors, and operations teams use this skill to let an agent inspect and manage CompanyCam resources for contractor photo documentation. It supports account-scoped CompanyCam API access through Maton, with explicit confirmation expected before writes, uploads, deletions, user or group changes, connection creation, and webhook operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent make account-changing CompanyCam API calls, including writes, deletes, uploads, and user or group changes.

Mitigation: Confirm the exact CompanyCam account, Maton connection, resource identifiers, request payload, and intended effect before approving any account-changing operation.

Risk: Webhook creation or updates can send CompanyCam project, photo, document, or label event data to an external URL.

Mitigation: Confirm the destination URL, selected scopes, and business intent before creating, updating, or enabling a webhook.

Risk: Maton or provider credentials could be exposed if printed, logged, persisted, or passed on command lines.

Mitigation: Use OAuth and the platform credential store where possible, avoid printing or persisting credentials, and use the documented stdin-based raw HTTP fallback only when the CLI cannot be installed.

Risk: CompanyCam API responses and webhook payloads may contain untrusted text that could be mistaken for instructions.

Mitigation: Treat fetched CompanyCam content as data, validate it before reuse, and do not execute or follow instructions embedded in returned records or payloads.

## Reference(s):

- [ClawHub CompanyCam skill](https://clawhub.ai/byungkyu/skills/companycam)
- [Maton homepage](https://maton.ai)
- [CompanyCam API Documentation](https://docs.companycam.com)
- [CompanyCam API Reference](https://docs.companycam.com/reference)
- [CompanyCam Getting Started](https://docs.companycam.com/docs/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user confirmation before connection creation or account-changing operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
