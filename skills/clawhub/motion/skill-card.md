## Description:

Motion API integration with managed OAuth for managing tasks, projects, workspaces, comments, and recurring tasks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and automation builders use this skill to query and manage Motion tasks, projects, workspaces, comments, and recurring tasks from an agent session. It defaults to read/list operations and requires user confirmation before writes, new connections, hosted functions, triggers, or persistent destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Motion writes, connection changes, or deletions can modify user work data or revoke access.

Mitigation: Default to read/list calls, verify the target account and resource identifiers, and obtain explicit user approval before POST, PUT, PATCH, DELETE, connection creation, or connection deletion.

Risk: Raw HTTP fallback requires a long-lived Maton API key that can leak through logs, shell history, child processes, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is necessary, keep the key in the process environment only, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Hosted functions, triggers, and destinations can become persistent automation or ongoing event forwarding.

Mitigation: Create them only after separate user approval, scope connections and trigger filters narrowly, prefer Maton-hosted destinations, use minimal body templates, and remove automation when it is no longer needed.

Risk: Third-party API responses and trigger payloads may contain private data or adversarial instructions.

Mitigation: Treat fetched content and event payloads as untrusted data, avoid logging full responses, extract only task-relevant fields, and never execute or follow instructions embedded in external content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/motion)
- [Maton Homepage](https://maton.ai)
- [Motion API Documentation](https://docs.usemotion.com/)
- [Motion API Reference](https://docs.usemotion.com/api-reference)
- [Motion Cookbooks](https://docs.usemotion.com/cookbooks/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline shell, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for Maton CLI or raw HTTPS calls; does not directly execute Motion API calls by itself.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
