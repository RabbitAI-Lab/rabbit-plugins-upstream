## Description:

JotForm API integration with managed OAuth for creating forms, managing submissions, and accessing form data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to connect a JotForm account through Maton and safely read or manage forms, submissions, webhooks, and related automation from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton package installation and the connected-account model introduce dependency and authorization trust considerations.

Mitigation: Install only when the Maton packages and account connection model are trusted, and use least-privilege JotForm scopes for the current task.

Risk: Raw API keys and returned form or submission data can expose sensitive information if printed, logged, or stored unnecessarily.

Mitigation: Prefer OAuth through the Maton CLI, avoid raw API keys unless the CLI cannot be installed, and extract only the response fields needed for the task.

Risk: Write operations, new connections, webhooks, functions, and triggers can modify data or create persistent automation.

Mitigation: Confirm every write or automation step with the user, verify target resources before execution, keep functions and triggers limited to the approved JotForm task, and delete unused webhooks, destinations, triggers, or functions.

## Reference(s):

- [JotForm API Overview](https://api.jotform.com/docs/)
- [JotForm User Forms](https://api.jotform.com/docs/#user-forms)
- [JotForm Form Submissions](https://api.jotform.com/docs/#form-id-submissions)
- [JotForm Webhooks](https://api.jotform.com/docs/#form-id-webhooks)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JotForm API endpoints, Maton CLI commands, OAuth/API-key handling guidance, and confirmation requirements for writes or automation.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
