## Description:

Administer a Cargo workspace and communicate with the Cargo team by managing workspace members, roles, API tokens, folders, environment variables, workspace files, sessions, and reports through the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace administrators use this skill to operate Cargo workspaces from an agent session, including member administration, token rotation, folder organization, environment variable management, file uploads, session logging, and issue reporting. Most user, role, and token writes require admin access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace administration commands can invite or remove users, change roles, create or remove tokens, and modify environment variables.

Mitigation: Use a low-privilege account or token where possible, verify the active workspace with cargo-ai whoami, and confirm every user, token, role, or environment variable mutation before execution.

Risk: The CLI install guidance uses a mutable latest package version.

Mitigation: Prefer a pinned @cargo-ai/cli version before installing or running commands in a real workspace.

Risk: Reports and session summaries may send operational context, logs, UUIDs, or transcript-derived details to the Cargo team.

Mitigation: Show report text before submission, redact secrets and customer data, and avoid automatic session hooks unless users understand what may be stored.

Risk: Workspace environment variables can expose secrets broadly if created as plain text or updated incorrectly.

Mitigation: Use the --secret option for credentials, avoid putting secret values in shell history, and review envVar updates or removals before applying them.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [User management examples](references/examples/users.md)
- [API token examples](references/examples/tokens.md)
- [Folder examples](references/examples/folders.md)
- [Report examples](references/examples/reports.md)
- [Session tracking examples](references/examples/sessions.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with Cargo CLI commands and expected JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create, update, remove, or report workspace resources through the cargo-ai CLI; command failures return JSON error messages.]

## Skill Version(s):

1.3.0 (source: skill frontmatter, skill metadata, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
