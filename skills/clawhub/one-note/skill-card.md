## Description:

Microsoft OneNote helps agents work with OneNote notebooks, sections, section groups, and pages through Microsoft Graph using Maton-managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to read and manage OneNote content from a connected Microsoft account. It is intended for notebook organization, page management, and approved OneNote automation through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad OneNote connection may expose more notebooks or pages than the current task requires.

Mitigation: Authorize only the needed account and scopes, prefer read-only access when available, and revoke unused connections.

Risk: Write operations can create, modify, or delete OneNote content.

Mitigation: Default to read and list calls first, then require explicit approval with the target resource and intended effect before POST, PUT, PATCH, or DELETE requests.

Risk: Raw API-key mode can expose a long-lived Maton credential through environment leaks, logs, shell history, or child processes.

Mitigation: Use OAuth through the Maton CLI when possible; if raw HTTP is necessary, keep the key only in the calling environment, never print or persist it, and rotate it after exposure.

Risk: Hosted functions or trigger event execution can continue acting without a human in the loop.

Mitigation: Use user-reviewed handlers, deny outbound network access unless specifically approved, and require separate approval before deployment, invocation, or event execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/one-note)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [OneNote API Overview](https://learn.microsoft.com/en-us/graph/integrate-with-onenote)
- [OneNote REST API Reference](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview)
- [Page HTML Reference](https://learn.microsoft.com/en-us/graph/onenote-input-output-html)
- [Microsoft Graph Explorer](https://developer.microsoft.com/graph/graph-explorer)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, API paths, and small code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference connected OneNote account data and should avoid exposing raw responses or credentials.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
