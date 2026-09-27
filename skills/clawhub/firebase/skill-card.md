## Description:

Firebase Management API integration with managed OAuth for managing Firebase projects, web apps, Android apps, iOS apps, app configurations, and Google Analytics links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to authenticate through Maton, inspect Firebase resources, manage Firebase apps, retrieve configurations, link Google Analytics, and set up explicitly approved Firebase-related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firebase write operations, connection changes, and hosted automation can affect real resources or create persistent data flows.

Mitigation: Default to read and list calls, verify the target Firebase connection and exact resource or payload, and require explicit user approval before writes, destructive actions, or persistent automation.

Risk: Raw API keys or provider credentials can be exposed through environment variables, logs, files, or command arguments.

Mitigation: Prefer OAuth through the Maton CLI and operating-system credential storage; use raw HTTP keys only when the CLI is unavailable and avoid printing, storing, or passing credentials unnecessarily.

Risk: Hosted functions and triggers can run user-approved Firebase actions automatically after setup.

Mitigation: Use user-authored or user-reviewed handlers, keep functions private, prefer DENY_ALL network policy, require separate approval for deploys and trigger destinations, and remove automation when it is no longer needed.

## Reference(s):

- [Firebase Management API Overview](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project)
- [Firebase Management REST API Reference](https://firebase.google.com/docs/reference/firebase-management/rest)
- [Projects Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects)
- [Web Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps)
- [Android Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps)
- [iOS Apps Resource](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
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

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands, JSON examples, API paths, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Firebase connection.]

## Skill Version(s):

1.2.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
