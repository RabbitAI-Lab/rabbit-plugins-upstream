## Description:

CompanyCam integrates with the CompanyCam API through Maton-managed OAuth so agents can list and manage contractor photo documentation resources such as projects, photos, users, tags, groups, documents, webhooks, and company information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate CompanyCam accounts from an agent, starting with read/list calls and requiring approval for account authorization, writes, uploads, deletes, webhook management, and automation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on CompanyCam account data through an authorized connection.

Mitigation: Confirm trust in Maton as the gateway, connect only the intended CompanyCam account, choose the narrowest available scopes, and specify the connection when more than one account is available.

Risk: Create, update, delete, upload, user/group management, and webhook operations can change account state or expose business data.

Mitigation: Default to read/list calls, verify identifiers and current state, and require explicit user approval for the target, payload, and expected effect before each write.

Risk: Webhook and trigger destinations create persistent automatic delivery of event data.

Mitigation: Approve the exact destination URL, controller, event list, data fields, schedule, and cleanup plan before enabling; keep destinations on Maton-controlled URLs unless the user names and approves a third-party host.

Risk: Hosted functions run under the deploying Maton account and can reach that account's authorized connections.

Mitigation: Deploy only user-authored or user-reviewed handlers, use DENY_ALL network policy unless specific hosts are approved, review the account's connections first, and delete functions when the task is complete.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key in the process environment.

Mitigation: Use raw HTTP only when the CLI cannot be installed, never print or persist the key, pass it only to api.maton.ai, and rotate it if it appears in logs, files, commands, or pasted output.

## Reference(s):

- [CompanyCam skill page](https://clawhub.ai/byungkyu/skills/companycam)
- [Maton homepage](https://maton.ai)
- [CompanyCam API Documentation](https://docs.companycam.com)
- [CompanyCam API Reference](https://docs.companycam.com/reference)
- [CompanyCam Getting Started](https://docs.companycam.com/docs/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated CompanyCam API calls, Maton CLI commands, raw HTTPS fallback commands, hosted-function code, trigger configuration, and approval checklists.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
