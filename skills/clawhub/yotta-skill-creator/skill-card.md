## Description:

Generates release-ready or self-use YottaMeta agent skill scaffolds from templates, validates naming and required structure, and reports whether the generated scaffold passes its self-check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent maintainers use this skill to create new yotta-prefixed skill directories with consistent release files, bilingual documentation, installer assets, references, and optional CLI scaffolding. It is intended for scaffolding new skills, not for writing the final skill content, implementing business logic, or batch-migrating existing skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers can place the skill into multiple agent skill directories and may overwrite an existing installed copy when rerun.

Mitigation: Use a pinned package version with a specific --dir or --agent target, review the target path before installing, and avoid global installation unless each destination is intended.

Risk: User-selected installation paths can affect directories outside the current project.

Mitigation: Install only into directories controlled by the current user and not writable by other users, then review the installed files before enabling the skill.

## Reference(s):

- [CLI reference](references/cli-reference.md)
- [Scaffold structure](references/scaffold-structure.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Generated skill directory containing Markdown, JSON, shell, JavaScript, optional Python files, reference documents, and status text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Refuses to generate into an existing target directory and runs a structure self-check before reporting success.]

## Skill Version(s):

0.1.2 (source: frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
