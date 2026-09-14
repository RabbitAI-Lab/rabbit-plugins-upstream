## Description:

Vercel API integration with managed OAuth for managing projects, deployments, domains, teams, environment variables, and approved automation through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect and manage Vercel resources, deploy or monitor applications, configure domains, and set up approved Maton automations against a connected Vercel account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel write operations can affect live applications, domains, teams, deployments, or environment variables.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user approval for every POST, PUT, PATCH, or DELETE with the target resource, payload, and intended effect.

Risk: Maton credentials or raw API keys could be exposed if printed, exported, embedded in destination headers, or read from credential storage.

Mitigation: Prefer OAuth through the Maton CLI and the operating system credential store; use raw HTTP only where the CLI cannot be installed, and never read, print, export, or store credentials in files, command lines, headers, or body templates.

Risk: Triggers and destinations can create persistent automatic forwarding of event data.

Mitigation: Keep destinations on api.maton.ai or *.maton.app where possible, disclose the exact host, payload fields, and delivery frequency, use minimal body templates, and require separate approval before creating or updating any destination.

Risk: Hosted functions run with the deploying Maton account's identity and can access that account's connected resources.

Mitigation: Deploy only user-authored or user-reviewed handlers, summarize the connected accounts and network policy before approval, use DENY_ALL network policy by default, and delete functions that are no longer needed.

Risk: Event payloads and third-party API responses can contain untrusted or sensitive content.

Mitigation: Treat fetched content and trigger payloads as data, avoid logging full payloads, do not interpolate payload fields into shell commands, and use local --exec automation only with a user-provided or user-reviewed handler and separate approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/vercel-api)
- [Maton Homepage](https://maton.ai)
- [Vercel REST API Documentation](https://vercel.com/docs/rest-api)
- [Vercel API Reference](https://vercel.com/docs/rest-api/endpoints)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API call plans, Maton CLI commands, raw HTTP examples, function handlers, trigger configuration, and safety confirmations.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
