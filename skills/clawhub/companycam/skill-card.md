## Description:

CompanyCam API integration with managed OAuth for managing projects, photos, users, tags, groups, documents, checklists, labels, collaborators, webhooks, and company information for contractor photo documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and manage CompanyCam account resources for contractor photo documentation. It supports read-first workflows and approved changes to projects, photos, users, groups, tags, documents, checklists, labels, collaborators, webhooks, and company details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account-changing operations can create, update, delete, upload, share, or modify CompanyCam resources.

Mitigation: Confirm the exact account, connection, target resource, payload, and intended effect with the user before allowing any write, delete, membership, sharing, or upload operation.

Risk: Webhook subscriptions can send CompanyCam project and photo event data to external URLs after creation.

Mitigation: Confirm the webhook destination, who controls it, and the event list before creating or updating a webhook.

Risk: The skill depends on Maton as the gateway for CompanyCam access.

Mitigation: Install and use it only when the user is comfortable granting CompanyCam access through Maton and has selected the intended account and connection.

## Reference(s):

- [CompanyCam API Documentation](https://docs.companycam.com)
- [CompanyCam API Reference](https://docs.companycam.com/reference)
- [CompanyCam Getting Started](https://docs.companycam.com/docs/getting-started)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/companycam)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration instructions]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active CompanyCam connection; normal usage goes through the maton CLI.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
