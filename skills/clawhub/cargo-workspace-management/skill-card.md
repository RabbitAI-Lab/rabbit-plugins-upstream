## Description:

Administers Cargo workspaces by managing members, API tokens, folders, roles, workspace files, reports, and session records through the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to manage access, API tokens, folders, roles, workspace files, reports, and session records with the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recommended session hooks upload conversation-derived session titles and summaries without clear consent or scope limits.

Mitigation: Review session tracking before enabling hooks, limit uploads to approved content, and establish how to disable tracking and delete stored sessions.

Risk: Token listings and reports can expose credentials or sensitive workspace details.

Mitigation: Use scoped credentials, avoid unnecessary token listings, and redact sensitive values from reports.

## Reference(s):

- [Cargo CLI workspace administration guide](SKILL.md)
- [Cargo CLI response shapes](references/response-shapes.md)
- [Cargo CLI troubleshooting](references/troubleshooting.md)
- [API token examples](references/examples/tokens.md)
- [Session tracking examples](references/examples/sessions.md)
- [Cargo Skills project homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and examples depend on the installed Cargo CLI, workspace permissions, and Cargo service behavior.]

## Skill Version(s):

1.6.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
