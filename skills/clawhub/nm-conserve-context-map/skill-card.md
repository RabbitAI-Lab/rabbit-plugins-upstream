## Description:

Generates a compressed project context map to avoid expensive Read/Grep calls at session start or before implementing features in an unfamiliar codebase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering-focused agents use this skill to quickly understand a project before exploration or implementation work. It summarizes structure, dependencies, entry points, routes, environment variables, schemas, and high-blast-radius files so subsequent file reads can be targeted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scans the current project to build structural context.

Mitigation: Use it only in repositories where project-structure scanning is intended, and review the generated context before relying on it for implementation decisions.

Risk: The scanner may create .codesight files that affect repository cleanliness.

Mitigation: Run with --no-wiki when persistent wiki files are not wanted, or add .codesight/ to .gitignore before use.

Risk: Broad trigger words may invoke the skill during general codebase exploration.

Mitigation: Confirm that a context-map scan is appropriate before running scanner commands in sensitive or change-controlled workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-context-map)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON scanner output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default scanner output targets a compact project map; options can emit JSON, write to a file, select one section, or adjust the token cap.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
