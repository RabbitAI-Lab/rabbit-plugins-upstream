## Description:

Google Apps Script API integration with managed OAuth for managing Apps Script projects, deployments, versions, function execution, and process monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate through Maton and operate the Google Apps Script API for project management, deployment and version workflows, remote function runs, and execution monitoring. It is intended for workflows where read/list operations are default and connection, write, delete, or function execution actions are confirmed by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected-account operations can modify Apps Script projects, deployments, versions, or run script functions with side effects.

Mitigation: Default to read/list calls, specify the intended Maton profile and connection when needed, and require explicit user confirmation before creating connections, changing resources, deleting resources, or running functions.

Risk: Credential exposure or overly broad authorization could expose Maton or Google account access.

Mitigation: Use OAuth where possible, keep credentials in the operating system credential store, do not print or persist tokens or API keys, and authorize only the accounts and scopes needed for the task.

Risk: Content returned from Google Apps Script APIs may include untrusted text or data.

Mitigation: Treat API responses as data, validate identifiers and payloads before reuse, and avoid executing or interpolating returned content into shell commands or follow-up requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-apps-script)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Apps Script API overview](https://developers.google.com/apps-script/api)
- [Google Apps Script API reference](https://developers.google.com/apps-script/api/reference/rest)
- [Google Apps Script projects resource](https://developers.google.com/apps-script/api/reference/rest/v1/projects)
- [Google Apps Script deployments guide](https://developers.google.com/apps-script/api/how-tos/manage-deployments)
- [Google Apps Script function execution guide](https://developers.google.com/apps-script/api/how-tos/execute)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-confirmed OAuth or API-key authentication.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
