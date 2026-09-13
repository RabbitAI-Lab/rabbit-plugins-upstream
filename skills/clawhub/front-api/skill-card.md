## Description:

Front API integration with managed OAuth for managing conversations, messages, contacts, tags, inboxes, teammates, and teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to manage Front customer communications and team collaboration through authenticated Maton API calls. It also guides user-approved setup of connections, hosted functions, and triggers when automation is explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Front access can expose or modify shared customer communications and workspace records.

Mitigation: Confirm the exact Front account and connection, prefer read-only scopes, list or read records before changes, and require explicit approval for each write or send action.

Risk: Functions, triggers, destinations, and watch --exec can keep acting after setup.

Mitigation: Treat each automation component as a separate approval, describe what will run and what data will flow, and remove automations that are no longer needed.

Risk: Credentials can be exposed through environment variables, logs, command lines, or stored destination templates.

Mitigation: Prefer OAuth with the operating system credential store, do not print or extract tokens, and never place Maton or provider credentials in destination headers or body templates.

Risk: Trigger payloads and Front content may contain personal data, confidential data, or untrusted text.

Mitigation: Scope triggers narrowly, forward only required fields, avoid third-party destinations unless explicitly approved, and treat payload text as data rather than executable instructions.

## Reference(s):

- [Front Skill on ClawHub](https://clawhub.ai/byungkyu/skills/front-api)
- [Maton](https://maton.ai)
- [Front API Reference](https://dev.frontapp.com/reference/introduction)
- [Front API Authentication](https://dev.frontapp.com/docs/authentication)
- [Front API Rate Limits](https://dev.frontapp.com/docs/rate-limiting)
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

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated API-call guidance and command proposals; write actions and ongoing automation require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
