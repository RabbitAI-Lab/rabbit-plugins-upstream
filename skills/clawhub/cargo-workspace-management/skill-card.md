## Description:

Guides Cargo workspace administrators through managing members, roles, API tokens, folders, files, environment variables, sessions, and reports with the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to manage Cargo members, access, tokens, resources, and configuration, and to submit support reports or session summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative commands can change workspace access, tokens, environment variables, and files.

Mitigation: Use only in trusted workspaces with authorized admins; confirm the target and intended changes before running each command.

Risk: Token values, customer data, or session details may be disclosed through reports or persistent summaries.

Mitigation: Redact secrets and customer data from reports, and review or disable session hooks before sharing transcript-derived summaries.

Risk: An unpinned CLI install can introduce unexpected changes.

Mitigation: Prefer a reviewed, pinned CLI version when installing or updating.

## Reference(s):

- [Cargo workspace management skill](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [CLI response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON; workspace permissions determine which operations are available.]

## Skill Version(s):

1.4.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
