## Description:

Guides agents in using a Notion command-line workflow for multi-workspace management, file uploads, schema changes, batch operations, templates, custom output, and audit logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and Notion workspace administrators use this skill to automate Notion workspace setup, database schema changes, file uploads, batch page operations, and audit-log review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad command-line authority can perform high-impact Notion operations such as batch deletes, schema removals, page moves, and cross-workspace changes.

Mitigation: Use the skill only for explicit Notion tasks, require dry-run output and human confirmation before destructive or cross-workspace operations, and avoid broad filters.

Risk: Notion integration tokens and workspace profiles can expose or modify sensitive workspace content.

Mitigation: Use least-privilege Notion integrations, keep credentials out of shared files, and rotate or revoke tokens that are no longer needed.

Risk: The skill depends on the third-party `notion-cli-tool` package, and the evidence recommends independent package verification.

Mitigation: Verify the package name, source, and version before installation or use in an agent environment.

Risk: The security summary notes inconsistent scope and documentation.

Mitigation: Review the artifact and generated commands before deployment, and limit use to well-scoped Notion automation workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/notion-cli)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, YAML, JSON, and Jinja2 examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may operate on Notion workspaces, databases, pages, files, and audit logs.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
