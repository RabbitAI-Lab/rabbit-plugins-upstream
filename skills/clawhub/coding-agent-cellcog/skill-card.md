## Description:

AI coding agent powered by CellCog Co-work. Code generation, debugging, refactoring, codebase exploration, terminal operations — executed directly on your machine. Lightweight with multimedia tools loaded on demand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to delegate code generation, debugging, refactoring, test execution, and codebase exploration to CellCog Co-work on a selected project directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate as a coding agent with read, edit, and command execution capability in the selected project.

Mitigation: Keep write and execute approvals enabled by default and review proposed changes before approving them.

Risk: Pointing Co-work at a broad or sensitive directory can expose credentials, private files, or business data.

Mitigation: Use a project-specific working directory and avoid home, credential, SSH, or sensitive data folders.

## Reference(s):

- [CellCog](https://cellcog.ai)
- [Coding Agent on ClawHub](https://clawhub.ai/cellcog/skills/coding-agent-cellcog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown text with code snippets, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits, terminal commands, dependency installation, tests, and project-specific implementation steps for user approval.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
