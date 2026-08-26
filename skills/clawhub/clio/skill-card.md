## Description:

Clio API integration with managed OAuth for reading, creating, updating, and deleting legal practice data in Clio Manage, with explicit approval required for write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to interact with Clio Manage legal practice records through Maton-managed OAuth. It supports read/list workflows by default and write workflows only after explicit user confirmation of the target resource and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access privileged legal practice data through the connected Clio account.

Mitigation: Install only when the publisher and Maton gateway are trusted, use the narrowest OAuth scopes available, and revoke unused connections.

Risk: Write-capable operations can create, update, or delete legal practice records.

Mitigation: Default to read/list calls and require explicit user approval with specific resource identifiers before any create, update, or delete action.

Risk: Using MATON_API_KEY can expose a long-lived credential to the local environment.

Mitigation: Prefer OAuth through the Maton CLI and avoid MATON_API_KEY unless the CLI cannot be used.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/clio)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Clio API Documentation](https://docs.developers.clio.com/api-reference/)
- [Clio Fields Guide](https://docs.developers.clio.com/api-docs/clio-manage/fields/)
- [Clio Rate Limits](https://docs.developers.clio.com/api-docs/clio-manage/rate-limits/)
- [Clio Permissions](https://docs.developers.clio.com/api-docs/permissions/)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Clio API request guidance and Maton CLI, SDK, or raw HTTP command examples; write actions require explicit user approval.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
