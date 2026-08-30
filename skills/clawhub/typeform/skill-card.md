## Description:

Typeform API integration with managed OAuth for creating forms, managing responses, and accessing insights through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access Typeform account data through Maton, list and inspect forms and responses, and prepare approved form or workspace changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Typeform data for the connected account through Maton.

Mitigation: Use OAuth, confirm the intended account and connection before use, and choose the least privileged scopes available for the task.

Risk: Write operations such as creating, updating, or deleting forms can change or remove Typeform resources.

Mitigation: Require explicit user approval for POST, PUT, PATCH, and DELETE calls, including the target resource, payload, and expected effect.

Risk: Fallback API-key use can expose a long-lived Maton credential if it is printed, logged, or persisted.

Mitigation: Prefer OAuth through the Maton CLI; when fallback HTTP access is unavoidable, keep the key out of command arguments, logs, files, and non-Maton hosts.

## Reference(s):

- [ClawHub typeform skill](https://clawhub.ai/byungkyu/skills/typeform)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Typeform API Overview](https://www.typeform.com/developers/get-started)
- [Typeform Forms API](https://www.typeform.com/developers/create/reference/retrieve-forms)
- [Typeform Responses API](https://www.typeform.com/developers/responses/reference/retrieve-responses)
- [Typeform Workspaces API](https://www.typeform.com/developers/create/reference/retrieve-workspaces)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-approved Maton OAuth connections and defaults to read or list operations before write actions.]

## Skill Version(s):

1.1.0 (source: server release metadata; frontmatter lists 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
