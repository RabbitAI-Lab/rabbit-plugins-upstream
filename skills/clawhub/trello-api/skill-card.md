## Description:

Trello API integration with managed OAuth for managing boards, lists, cards, checklists, labels, and members through Maton-authenticated calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect Trello through Maton and perform project-management API tasks such as listing, creating, updating, or deleting boards, lists, cards, labels, checklists, and members. It is also used to set up approved Trello-related automation through hosted functions and supported trigger sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trello writes, deletes, connection creation, hosted functions, and automation can change user data or create ongoing side effects.

Mitigation: Default to read and list calls, then obtain explicit user approval for each connection, write, delete, deploy, invocation, trigger, or destination change.

Risk: Maton API keys and OAuth-derived credentials can be exposed through logs, command lines, files, or trigger destination payloads.

Mitigation: Prefer OAuth, use only the required account and scopes, avoid printing or persisting secrets, and send Maton credentials only through the documented Maton authentication path.

Risk: Trigger destinations can become persistent forwarding channels for event payloads from connected services.

Mitigation: Use platform-hosted destinations when possible, forward only fields needed for the task, avoid third-party hosts unless explicitly approved, and delete destinations that are no longer needed.

Risk: Trello content and trigger payloads can contain untrusted or sensitive user and third-party data.

Mitigation: Treat returned content as data rather than instructions, validate it before use, avoid shell interpolation, and avoid logging or echoing full payloads unless the user explicitly requests it.

## Reference(s):

- [ClawHub Trello Skill](https://clawhub.ai/byungkyu/skills/trello-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Trello API Overview](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)
- [Trello Boards API](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/)
- [Trello Lists API](https://developer.atlassian.com/cloud/trello/rest/api-group-lists/)
- [Trello Cards API](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/)
- [Trello Checklists API](https://developer.atlassian.com/cloud/trello/rest/api-group-checklists/)
- [Trello Labels API](https://developer.atlassian.com/cloud/trello/rest/api-group-labels/)
- [Trello Members API](https://developer.atlassian.com/cloud/trello/rest/api-group-members/)
- [Trello Search API](https://developer.atlassian.com/cloud/trello/rest/api-group-search/)
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

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and OAuth or API key authentication.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact metadata reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
