## Description:

Baserow API integration with managed API key authentication for reading, creating, updating, deleting, and querying database rows, fields, and tables through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Baserow databases through managed Maton authentication, including listing, filtering, creating, updating, and deleting rows, fields, tables, and files. It is intended for API-backed workflows where the agent should prefer read/list calls and get user approval before new connections or data-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account can read or change Baserow data available to that account.

Mitigation: Use OAuth where possible, connect only the account needed for the task, prefer read/list calls first, and confirm the target database, table, row, payload, and intended effect before write or delete calls.

Risk: New Baserow connections can grant the skill access to account data.

Mitigation: Create connections only after explicit user approval, choose the least privileged scopes available, specify the intended connection when multiple connections exist, and revoke unused Maton or Baserow connections.

Risk: Credentials or provider-issued tokens could be exposed if handled outside the Maton CLI flow.

Mitigation: Prefer Maton OAuth, keep credentials in the operating system credential store, do not print or persist tokens, and send raw API keys only to api.maton.ai when the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/baserow-api)
- [Maton Homepage](https://maton.ai)
- [Baserow API Documentation](https://baserow.io/api-docs)
- [Baserow Database API](https://baserow.io/user-docs/database-api)
- [Baserow API Spec (OpenAPI)](https://api.baserow.io/api/redoc/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with shell command examples and JSON API payload snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Baserow connection.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
