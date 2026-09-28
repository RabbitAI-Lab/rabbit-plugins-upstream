## Description:

CompanyCam API integration with managed OAuth for managing projects, photos, users, tags, groups, documents, checklists, labels, collaborators, webhooks, and company information for contractor photo documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate CompanyCam resources through Maton-managed OAuth, including read workflows, approved writes, and approved automation for contractor photo documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations, connection creation, hosted functions, trigger destinations, and webhooks can change CompanyCam data or create persistent automation.

Mitigation: Require explicit user approval for each such action after confirming the account, resource IDs, payload, destination URL, forwarded data, and persistence behavior.

Risk: Webhooks and trigger destinations can forward CompanyCam or event data to external URLs until they are removed.

Mitigation: Use only user-provided destinations, prefer Maton-controlled endpoints when appropriate, list existing forwarding before adding more, and remove destinations that are no longer needed.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key in the process environment.

Mitigation: Prefer OAuth through the Maton CLI and OS credential store; if raw HTTP is necessary, send the key only to api.maton.ai and never print, log, commit, or paste it.

Risk: CompanyCam responses and trigger payloads may include customer, job-site, photo, address, user, or payment-related data.

Mitigation: Extract only the fields needed for the user task and avoid dumping full responses into logs, files, prompts, or third-party inspection services.

## Reference(s):

- [CompanyCam API Documentation](https://docs.companycam.com)
- [CompanyCam API Reference](https://docs.companycam.com/reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/companycam)
- [Time Trigger Reference](references/time/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated API calls and automation steps; write operations, connection creation, webhooks, hosted functions, and trigger destinations require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
