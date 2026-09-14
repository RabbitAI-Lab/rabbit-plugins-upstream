## Description:

Google Apps Script API integration with managed OAuth for managing Apps Script projects, deployments, versions, remote function execution, and script process monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation builders use this skill to manage Google Apps Script projects, deployments, versions, and remote function execution through Maton-managed OAuth. The skill is suited to account-scoped Apps Script administration where reads are preferred by default and writes, deployments, runs, connections, functions, and triggers require explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Apps Script access can expose or modify projects, deployments, versions, executions, and process data through the connected account.

Mitigation: Use OAuth, prefer read-only scopes and calls, and confirm every write, deployment, run, connection, function, trigger, or destination action before execution.

Risk: Long-lived Maton API keys or raw HTTP usage can leak credentials if printed, exported broadly, logged, or pasted into shared output.

Mitigation: Prefer OAuth through the Maton CLI, use raw HTTP only when the CLI cannot be installed, send keys only to api.maton.ai, and rotate any key that may have been exposed.

Risk: Hosted functions and triggers can create persistent automation that continues after the initial task.

Mitigation: Review hosted function code before deployment, keep network policy DENY_ALL unless a named host is necessary, and remove unused triggers, destinations, functions, and connections.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-apps-script)
- [Maton Homepage](https://maton.ai)
- [Apps Script API Overview](https://developers.google.com/apps-script/api)
- [Apps Script API Reference](https://developers.google.com/apps-script/api/reference/rest)
- [Projects Resource](https://developers.google.com/apps-script/api/reference/rest/v1/projects)
- [Deployments Guide](https://developers.google.com/apps-script/api/how-tos/manage-deployments)
- [Executing Functions](https://developers.google.com/apps-script/api/how-tos/execute)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Maton CLI, OAuth or API-key authentication, network access, and explicit approval before sensitive actions.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
