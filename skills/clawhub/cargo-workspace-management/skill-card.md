## Description:

Administer Cargo workspaces by managing members, roles, API tokens, folders, workspace files, reports, and optional session records through the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, workspace administrators, and agent operators use this skill to administer a Cargo workspace from the CLI, including user access, API tokens, folders, files, feedback reports, and session records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact workspace administration actions, including user, role, token, folder, file, report, and session writes.

Mitigation: Confirm the active workspace and intended target before running write commands; use admin credentials only for operations that require them.

Risk: API token creation returns a token value once, and mishandling it can expose workspace access.

Mitigation: Store new tokens immediately in an approved secrets manager, redact token values from logs and reports, and rotate or remove unused tokens.

Risk: Workspace file uploads can send sensitive local data to Cargo storage.

Mitigation: Upload only files intended for Cargo storage and review file contents before upload.

Risk: Optional Claude session hooks can persist local hook configuration and record transcript-derived session summaries.

Mitigation: Enable session hooks only with organizational approval and avoid recording sensitive session details.

Risk: Feedback reports and session shares may include commands, errors, UUIDs, or operational context.

Mitigation: Redact secrets and sensitive business data before submitting reports or sharing session activity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [User management examples](references/examples/users.md)
- [API token examples](references/examples/tokens.md)
- [Folder examples](references/examples/folders.md)
- [Report examples](references/examples/reports.md)
- [Session tracking examples](references/examples/sessions.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Cargo CLI authentication and an active workspace; user, role, and token writes require admin access.]

## Skill Version(s):

1.2.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
