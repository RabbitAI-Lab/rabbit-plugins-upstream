## Description:

Administers Cargo workspaces by managing members, roles, API tokens, folders, workspace files, and feedback reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cargo workspace administrators use this skill to manage members, access roles, tokens, folders, workspace files, and CLI feedback reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic reports sent to Cargo may include private information from command output.

Mitigation: Show a sanitized preview and get approval before submitting a report; check error messages for private data.

Risk: Workspace administration can expose credentials or grant broader access than needed.

Mitigation: Use only the permissions needed, avoid listing unrelated tokens, and import only secrets intended for the whole workspace. Pin a reviewed CLI version.

## Reference(s):

- [Cargo skills project homepage (declared in skill metadata)](https://github.com/getcargohq/cargo-skills)
- [Cargo Workspace Management on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management)
- [Troubleshooting](references/troubleshooting.md)
- [Response shapes](references/response-shapes.md)
- [API token examples](references/examples/tokens.md)
- [Report examples](references/examples/reports.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes command options and example JSON response shapes]

## Skill Version(s):

1.7.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
