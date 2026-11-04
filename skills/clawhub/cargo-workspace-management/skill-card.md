## Description:

Administer a Cargo workspace by managing members, roles, API tokens, folders, workspace files, and reports with the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators use this skill to manage membership, roles, API tokens, folders, workspace files, and reports through the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic reports sent to Cargo may include confidential troubleshooting details.

Mitigation: Preview and approve reports before submission, and remove confidential information from commands, errors, and titles.

Risk: API token output can expose credentials, and broad credentials can increase their impact.

Mitigation: Use narrowly scoped credentials and keep token output private.

Risk: The external CLI behavior and unavailable sibling workflows have not been verified.

Mitigation: Pin a reviewed CLI version before using the skill.

## Reference(s):

- [Cargo Skills homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub release page](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [User management examples](references/examples/users.md)
- [API token examples](references/examples/tokens.md)
- [Folder examples](references/examples/folders.md)
- [Report examples](references/examples/reports.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with shell command examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create or modify workspace resources and settings.]

## Skill Version(s):

1.7.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
