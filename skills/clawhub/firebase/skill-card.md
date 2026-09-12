## Description:

Firebase Management API integration with managed OAuth for managing Firebase projects, web apps, Android apps, iOS apps, app configurations, and Google Analytics links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Firebase projects and app resources through Maton-managed authentication. It is also used to set up approved Firebase-related automation through Maton functions, triggers, and destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firebase writes, connection creation, function deployment, trigger setup, and destination changes can alter production resources or create ongoing automation.

Mitigation: Default to read and list calls, then get explicit user approval for each write, function deployment, trigger, and destination before execution.

Risk: Trigger destinations can continuously forward matching event payloads, including personal, financial, repository, or workspace data, to a URL.

Mitigation: Keep trigger scopes narrow, prefer Maton-controlled destinations, use body templates to forward only required fields, and require explicit approval for any third-party host.

Risk: Maton API keys and provider credentials can leak through logs, command lines, environment dumps, files, or destination templates.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist credentials, send Maton API keys only to api.maton.ai, and rotate any key that was exposed.

Risk: Third-party API responses and trigger payloads may contain untrusted instructions, secrets, or shell-sensitive content.

Mitigation: Treat external content as data, avoid verbatim logging, and never execute or interpolate it into commands without validation.

## Reference(s):

- [Firebase Management API Overview](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project)
- [Firebase Management REST API Reference](https://firebase.google.com/docs/reference/firebase-management/rest)
- [Firebase Projects Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects)
- [Firebase Web Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)
- [Firebase Android Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps)
- [Firebase iOS Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps)
- [Maton Homepage](https://maton.ai)
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

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton OAuth or, only when the CLI cannot be installed, a Maton API key for raw HTTP calls.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
