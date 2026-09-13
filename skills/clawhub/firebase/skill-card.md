## Description:

Firebase Management API integration with managed OAuth for managing Firebase projects, web apps, Android apps, iOS apps, app configurations, and Google Analytics links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an authenticated Firebase account through Maton and perform approved Firebase Management API tasks such as listing projects, creating or managing apps, retrieving app configurations, and linking Google Analytics. It also documents how approved Firebase actions can be wrapped in hosted functions or trigger-driven automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations, connection creation, hosted functions, and trigger destinations can modify Firebase resources or create persistent automation.

Mitigation: Default to read and list operations, confirm the target resource and effect before any write, and require separate explicit approval for each new connection, function, invocation, trigger, or destination.

Risk: Long-lived API keys and broad Firebase OAuth scopes can expose more access than the task requires.

Mitigation: Prefer OAuth, use least-privilege Firebase scopes, avoid exporting MATON_API_KEY when the CLI can be used, and rotate any key that was printed, committed, or pasted.

Risk: Trigger destinations and event payloads can continuously forward personal, private, or payment-related data.

Mitigation: Use narrow trigger scopes, forward only required fields, avoid public inspection endpoints, do not place credentials in destination headers or templates, and prefer api.maton.ai or *.maton.app destinations unless the user approves a named external host.

## Reference(s):

- [ClawHub Firebase skill](https://clawhub.ai/byungkyu/skills/firebase)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Firebase Management API Overview](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project)
- [Firebase Management REST API Reference](https://firebase.google.com/docs/reference/firebase-management/rest)
- [Firebase Projects Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects)
- [Firebase Web Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)
- [Firebase Android Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps)
- [Firebase iOS Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps)
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

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated Firebase and Maton operations; write operations, new connections, hosted functions, and persistent trigger destinations require explicit user approval.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
