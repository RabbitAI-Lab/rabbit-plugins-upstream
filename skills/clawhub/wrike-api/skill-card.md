## Description:

Wrike API integration with managed OAuth for managing Wrike tasks, folders, projects, spaces, collaboration resources, and administrative functions through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Wrike through Maton for project work, task tracking, time logs, team resources, and account administration. It is intended for users who have a Maton account, network access, and authorization to connect the relevant Wrike account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Wrike data and perform administrative operations.

Mitigation: Confirm every write or admin action with the user, including the target resource, payload, intended effect, and account context.

Risk: Audit log and data export requests can expose broad organizational or privacy-sensitive data.

Mitigation: Run audit log or data export operations only after the user explicitly requests them and confirms the scope.

Risk: Wrike and Maton credentials can be exposed if handled outside the recommended OAuth flow.

Mitigation: Prefer OAuth through the Maton CLI, use the narrowest available Wrike scopes, avoid printing or persisting credentials, and rotate any key that was exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/wrike-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Wrike API Documentation](https://developers.wrike.com/)
- [Wrike API Overview](https://developers.wrike.com/overview/)
- [Wrike OAuth 2.0 Authorization](https://developers.wrike.com/oauth-20-authorization/)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid Wrike connection; write and administrative actions require explicit user approval.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
