## Description:

Helps an agent administer a Cargo workspace by guiding CLI-based user, role, token, folder, file, environment variable, session, and report workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and workspace administrators use this skill to manage Cargo workspace access, API tokens, folders, workspace files, environment variables, and feedback reports through the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide workspace user, role, token, folder, file, and environment-variable changes that may affect broad workspace access.

Mitigation: Use a least-privilege Cargo account or token and confirm target users, roles, folders, tokens, and environment variables before executing write commands.

Risk: API tokens and secret environment variables can expose credentials if mishandled.

Mitigation: Store newly created token values in a secrets manager immediately, avoid printing secrets, and prefer secret environment-variable workflows that keep values out of command history.

Risk: Session hooks can persist transcript-derived session summaries to Cargo workspace management.

Mitigation: Enable session hooks only after confirming what data is stored, who can access it, and how session logging can be disabled or deleted.

Risk: The metadata installs @cargo-ai/cli@latest, which may change behavior over time.

Mitigation: Use a pinned CLI version where practical and review CLI updates before running administrative workflows.

## Reference(s):

- [Cargo Workspace Management Skill](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management)
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [User management examples](references/examples/users.md)
- [API token examples](references/examples/tokens.md)
- [Folder examples](references/examples/folders.md)
- [Report examples](references/examples/reports.md)
- [Session tracking examples](references/examples/sessions.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands commonly return JSON; failures are described as non-zero exits with an errorMessage field.]

## Skill Version(s):

1.3.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
