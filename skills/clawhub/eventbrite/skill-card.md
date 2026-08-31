## Description:

Eventbrite API integration with managed OAuth for managing events, venues, ticket classes, orders, attendees, and related reference data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Eventbrite through Maton OAuth and the maton CLI, primarily to list, create, update, publish, cancel, or delete Eventbrite resources after confirming account context and user intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify real Eventbrite resources, including publishing, canceling, updating, or deleting events and related records.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user approval before POST, PUT, PATCH, or DELETE operations.

Risk: Authorization gives Maton access to a connected Eventbrite account.

Mitigation: Prefer OAuth over long-lived API keys, review connection creation prompts carefully, select only needed scopes when available, and revoke unused connections.

Risk: Multiple Maton profiles or Eventbrite connections can cause writes to land in the wrong account.

Mitigation: Specify the intended Maton profile and Eventbrite connection when more than one account or connection exists.

Risk: Eventbrite API responses can contain untrusted external content.

Mitigation: Treat fetched content as data, avoid executing or interpolating it into shell commands or prompts, and validate it before using it in follow-up requests.

## Reference(s):

- [ClawHub Eventbrite Skill](https://clawhub.ai/byungkyu/skills/eventbrite)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Eventbrite API Documentation](https://www.eventbrite.com/platform/api)
- [Eventbrite API Basics](https://www.eventbrite.com/platform/docs/api-basics)
- [Eventbrite API Explorer](https://www.eventbrite.com/platform/docs/api-explorer)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Eventbrite connection for live API calls.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
