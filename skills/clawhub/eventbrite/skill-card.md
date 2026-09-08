## Description:

Eventbrite API integration with managed OAuth for managing events, venues, ticket classes, orders, attendees, and Eventbrite reference data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an Eventbrite account through Maton and perform event-management tasks such as listing organizations, creating or updating events and venues, managing ticket classes, and reviewing orders or attendees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, publish, cancel, update, or delete Eventbrite resources in an authorized account.

Mitigation: Require the agent to show the exact target resource, request payload, and intended effect before any write operation, and proceed only after explicit user confirmation.

Risk: Authorization gives Maton access to the connected Eventbrite account.

Mitigation: Prefer OAuth, review the selected Maton account and Eventbrite connection, use least-privilege scopes when available, and revoke unused connections.

Risk: Multiple Maton profiles or Eventbrite connections can make the target account ambiguous.

Mitigation: Require the agent to identify and pin the intended profile and connection before making account-specific or modifying calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/eventbrite)
- [Maton Homepage](https://maton.ai)
- [Eventbrite API Documentation](https://www.eventbrite.com/platform/api)
- [Eventbrite API Basics](https://www.eventbrite.com/platform/docs/api-basics)
- [Eventbrite API Explorer](https://www.eventbrite.com/platform/docs/api-explorer)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Eventbrite connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
