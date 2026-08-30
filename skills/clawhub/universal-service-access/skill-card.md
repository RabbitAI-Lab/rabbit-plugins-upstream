## Description:

Helps agents manage credentials and access for external services such as Vercel, Supabase, and GitHub with minimum-privilege handling, redaction, connection verification, and destructive-operation guards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill when a user explicitly asks to set up, rotate, or verify credentials for a specific external service. It supports safer workflows that require API keys, OAuth tokens, service keys, project identifiers, or account-level validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles credentials for external services and could request broader access than a task requires.

Mitigation: Use narrowly scoped tokens or OAuth connections, prefer project- or repository-specific permissions, and request credentials only after confirming the service and required capability.

Risk: Secrets could be exposed in chat, logs, configuration files, or generated code.

Mitigation: Redact secret values from all visible output, avoid plaintext storage, use native secret stores or protected environment variables, and scan proposed commits or configuration changes for leaked credentials.

Risk: External-service actions can affect the wrong project, account, repository, or production resource.

Mitigation: Verify the target account, project, repository, environment, and permission scope before making changes, and require explicit confirmation before destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/universal-service-access)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, code, text]

**Output Format:** [Markdown with inline commands, configuration snippets, and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Secrets should be redacted from user-visible output, logs, repository files, and ordinary memory.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
