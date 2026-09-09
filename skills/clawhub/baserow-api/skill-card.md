## Description:

Baserow lets agents manage Baserow database rows, fields, tables, filtering, sorting, pagination, and file uploads through Maton-managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to let an agent read and manage Baserow databases through approved Maton connections, including row CRUD, schema lookup, filtering, batch operations, and file upload workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change Baserow data through a connected Maton account.

Mitigation: Install only when agent access to Baserow is intended, and approve each create, update, delete, and batch operation only after reviewing the target resource and payload.

Risk: Long-lived API keys or provider credentials could be exposed through logs, command history, files, or process environments.

Mitigation: Prefer OAuth and the Maton CLI credential store; never print, persist, or pass credentials on the command line, and rotate any key that is exposed.

Risk: An ambiguous Maton account or Baserow connection could send reads or writes to the wrong workspace.

Mitigation: Specify the intended connection when multiple Baserow connections exist and verify account context with read or list calls before writes.

Risk: Connected permissions may be broader than the immediate task requires.

Mitigation: Use the narrowest available Baserow connection and scopes, prefer read-only access where possible, and revoke unused connections.

Risk: Baserow content returned by the API may contain untrusted text or instructions.

Mitigation: Treat API responses as data, not instructions; do not execute or interpolate returned content into shell commands or follow-up requests without validation.

## Reference(s):

- [ClawHub Baserow skill page](https://clawhub.ai/byungkyu/skills/baserow-api)
- [Maton homepage](https://maton.ai)
- [Baserow API Documentation](https://baserow.io/api-docs)
- [Baserow Database API](https://baserow.io/user-docs/database-api)
- [Baserow Database Tokens](https://baserow.io/user-docs/personal-api-tokens)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, Python, JavaScript, and JSON examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Baserow API paths, filters, payload examples, connection identifiers, and risk checks; API responses can contain user data.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
