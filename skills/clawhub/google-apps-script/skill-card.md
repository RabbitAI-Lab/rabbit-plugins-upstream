## Description:

Google Apps Script API integration with managed OAuth for managing Apps Script projects, deployments, versions, script execution, and process monitoring through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Google Apps Script through Maton-managed OAuth: list and update projects, manage versions and deployments, run functions, and inspect process or metrics data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use OAuth connections for Google Apps Script, which may grant access to projects owned by or shared with the connected Google account.

Mitigation: Review account and scope choices during OAuth, require explicit confirmation before creating a connection, and revoke unused connections promptly.

Risk: Writes, deployment changes, deletes, and script function execution can alter projects or trigger side effects.

Mitigation: Default to read and list calls, verify identifiers and current state first, and require explicit user confirmation before POST, PUT, PATCH, DELETE, deployments, or scripts.run calls.

Risk: Long-lived API keys or provider-issued tokens can leak if printed, logged, persisted, or passed on command lines.

Mitigation: Prefer Maton OAuth through the CLI credential store, never print or persist credentials, and send Maton API keys only to api.maton.ai when the CLI cannot be used.

Risk: Multiple Maton accounts or Google Apps Script connections can cause actions to land in the wrong account.

Mitigation: Specify the intended Maton profile and Google Apps Script connection whenever more than one account or connection exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-apps-script)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Apps Script API Overview](https://developers.google.com/apps-script/api)
- [Google Apps Script API Reference](https://developers.google.com/apps-script/api/reference/rest)
- [Google Apps Script Projects Resource](https://developers.google.com/apps-script/api/reference/rest/v1/projects)
- [Google Apps Script Deployments Guide](https://developers.google.com/apps-script/api/how-tos/manage-deployments)
- [Google Apps Script Function Execution Guide](https://developers.google.com/apps-script/api/how-tos/execute)
- [Related ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user confirmation for connection creation, writes, deletes, deployments, and script execution.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
