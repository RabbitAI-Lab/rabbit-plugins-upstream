## Description:

Google Contacts API integration with managed OAuth for managing contacts, contact groups, and address book search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to read, search, create, update, or delete Google Contacts records and contact groups through a Maton-connected Google account. It also provides guidance for approved hosted functions and triggers when the user explicitly requests persistent automation around Google Contacts actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Google Contacts through the user's Maton-connected account.

Mitigation: Use OAuth when possible, default to read and list operations, and require explicit approval before creating, updating, deleting, or copying contacts or contact groups.

Risk: API-key authentication can expose a long-lived credential if copied into environment variables, logs, files, command lines, or hosted destinations.

Mitigation: Prefer OAuth and the Maton CLI credential store; when an API key is unavoidable, avoid printing or persisting it and rotate it if it was exposed.

Risk: Hosted functions, triggers, and destinations can continue running or forwarding event data until removed.

Mitigation: Create automation only after separate explicit approval, scope it to the minimum required data, prefer Maton-hosted destinations, and delete functions, triggers, or destinations when the task is complete.

Risk: Contacts, event payloads, and third-party API responses can contain personal data or adversarial content.

Mitigation: Extract only the fields needed for the task, avoid logging raw responses, and treat fetched content as data rather than instructions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-contacts)
- [Maton Homepage](https://maton.ai)
- [Google People API Overview](https://developers.google.com/people/api/rest)
- [People Resource](https://developers.google.com/people/api/rest/v1/people)
- [Contact Groups Resource](https://developers.google.com/people/api/rest/v1/contactGroups)
- [Person Fields Reference](https://developers.google.com/people/api/rest/v1/people#Person)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-facing instructions and command examples for Maton CLI or raw HTTP access; authenticated calls can return Google Contacts data in JSON.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
