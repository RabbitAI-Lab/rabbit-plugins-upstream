## Description:

Todoist API integration with managed OAuth for managing tasks, projects, sections, labels, and comments through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect and manage Todoist tasks, projects, sections, labels, and comments from an agent session while keeping OAuth access mediated by Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, complete, or delete Todoist data after user authorization.

Mitigation: Confirm the exact target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: A user with multiple Todoist connections or Maton profiles could act on the wrong account.

Mitigation: Specify the intended connection or profile when more than one account is available.

Risk: Credential exposure is possible when using API keys or raw HTTP fallback instead of the CLI OAuth flow.

Mitigation: Prefer Maton OAuth through the CLI, avoid printing or persisting credentials, and send Maton API keys only to api.maton.ai.

## Reference(s):

- [Maton](https://maton.ai)
- [Todoist API v1 Documentation](https://developer.todoist.com/api/v1)
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters)
- [Todoist OAuth Documentation](https://developer.todoist.com/guides/#oauth)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration instructions]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-authorized Todoist access.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
