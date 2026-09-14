## Description:

Typeform API integration with managed OAuth for creating forms, managing responses, and accessing insights through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to connect an authorized Typeform account through Maton, inspect forms, responses, workspaces, themes, and insights, and perform approved Typeform changes or hosted automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Typeform account access through Maton and may expose forms, responses, and workspace data available to the connected account.

Mitigation: Use OAuth where possible, review requested Typeform scopes, choose the least-privileged account and connection, and specify the target connection when multiple connections exist.

Risk: Writes, connection creation, hosted functions, and trigger destinations can modify data or create ongoing automation.

Mitigation: Confirm every write, new connection, function deploy or invocation, trigger, and persistent destination with the user before execution.

Risk: Long-lived Maton API keys or signing keys can leak through shell history, logs, command lines, or destination configuration.

Mitigation: Prefer OAuth and the Maton CLI credential store, avoid pasting secrets into shell commands, never print or persist keys, and rotate any key that was exposed.

Risk: Trigger payloads from connected event sources can carry personal, confidential, payment, or private repository data.

Mitigation: Scope triggers narrowly, forward only required fields, prefer Maton-controlled destinations, and avoid broad third-party trigger destinations unless explicitly approved.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Typeform API Overview](https://www.typeform.com/developers/get-started)
- [Typeform Forms API](https://www.typeform.com/developers/create/reference/retrieve-forms)
- [Typeform Responses API](https://www.typeform.com/developers/responses/reference/retrieve-responses)
- [Typeform Workspaces API](https://www.typeform.com/developers/create/reference/retrieve-workspaces)
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

**Output Format:** [Markdown with inline shell, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Typeform API request paths, Maton CLI commands, hosted function examples, trigger configuration, and security guidance.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
