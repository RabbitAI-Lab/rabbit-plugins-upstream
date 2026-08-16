## Description:

Manage Cargo workspace users, API tokens, folders, roles, workspace files, reports, and session records using the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and workspace admins use this skill to ask an agent for Cargo CLI commands and guidance for managing users, roles, API tokens, folders, files, reports, and session records in a Cargo workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides workspace administration actions that use the active Cargo credentials and may change users, roles, tokens, folders, files, reports, or sessions.

Mitigation: Install and use it only when Cargo workspace administration is intended, verify the active account with `cargo-ai whoami`, and use appropriately scoped admin credentials for write operations.

Risk: The skill promotes Claude Code session hooks that can record session metadata and transcript-derived summaries in Cargo.

Mitigation: Enable the session hooks only with explicit consent and when session metadata and summaries are acceptable to store in Cargo.

Risk: API token creation returns a token value once, and mishandling it can expose workspace access.

Mitigation: Store generated tokens immediately in a secrets manager, avoid logging token values, and rotate or remove tokens that may be exposed.

Risk: Uploaded files and report descriptions may contain sensitive workspace or customer data.

Mitigation: Review files before upload and redact secrets, personal data, and unnecessary identifiers from report descriptions.

Risk: The referenced installer pattern downloads and executes a remote shell script.

Mitigation: Inspect or otherwise verify the installer before execution instead of piping it directly to `sh`.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [User management examples](references/examples/users.md)
- [API token examples](references/examples/tokens.md)
- [Folder examples](references/examples/folders.md)
- [Report examples](references/examples/reports.md)
- [Session tracking examples](references/examples/sessions.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline Cargo CLI commands and JSON response references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands act through the installed @cargo-ai/cli and the active Cargo credentials.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
