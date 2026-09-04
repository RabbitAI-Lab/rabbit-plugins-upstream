## Description:

Twenty CRM API integration with managed authentication for managing companies, people, opportunities, notes, tasks, activities, and workflows through Maton CLI OAuth-backed API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to inspect and update Twenty CRM records such as companies, people, opportunities, notes, tasks, and workflows. It is suited to agent-assisted CRM operations where reads are the default and writes require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Twenty CRM API access may exceed the user's immediate task under the connected account's permissions.

Mitigation: Use OAuth with the narrowest available scopes, prefer read-only access when possible, pin the intended connection, and revoke unused connections.

Risk: Write or workflow-triggering calls can change live CRM records or cause downstream side effects.

Mitigation: Default to read/list calls, verify target records first, and require explicit user confirmation for every POST, PUT, PATCH, DELETE, or workflow-triggering action.

Risk: Long-lived API keys can leak through environment variables, logs, command history, or copied output.

Mitigation: Prefer OAuth, never print or persist credentials, pass secrets only through the process environment when the CLI is unavailable, and rotate exposed keys.

## Reference(s):

- [Twenty CRM Skill on ClawHub](https://clawhub.ai/byungkyu/skills/twenty)
- [Maton Homepage](https://maton.ai)
- [Twenty API Documentation](https://docs.twenty.com/developers/extend/api)
- [Twenty GitHub](https://github.com/twentyhq/twenty)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, JSON, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Twenty CRM connection; defaults to read/list operations and requires user confirmation before writes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
