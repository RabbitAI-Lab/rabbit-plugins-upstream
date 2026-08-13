## Description:

Inspect and edit a workspace's git-backed GTM context repository and runtime sandbox using the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to browse, read, author, edit, and validate GTM context files and inspect the derived knowledge graph for a Cargo workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo CLI write and edit operations push commits to the workspace context repository's default branch.

Mitigation: Confirm the intended workspace with cargo-ai whoami before any write or edit, read back the workspace name, and review each proposed file change before committing.

Risk: Incorrect or malformed context files can reduce discoverability or introduce misleading GTM knowledge.

Mitigation: Use the documented domain templates, keep YAML title and description frontmatter intact, and verify graph links after changes.

Risk: CLI access applies to the selected Cargo workspace context repository.

Mitigation: Install only when Cargo CLI access to that workspace is intended and use workspace-scoped authentication where available.

## Reference(s):

- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Context Repo Conventions](references/conventions.md)
- [Authoring Examples](references/examples/authoring.md)
- [Context Repo Lifecycle](references/examples/lifecycle.md)
- [Knowledge-Graph Queries](references/examples/graph-queries.md)
- [Response Shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide Cargo CLI commands that read context, inspect graph data, or push write/edit commits to the workspace context repository.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
