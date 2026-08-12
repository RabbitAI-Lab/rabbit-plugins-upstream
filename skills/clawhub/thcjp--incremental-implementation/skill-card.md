## Description:

Provides agent guidance for incremental multi-file development changes, including reading files, running commands, applying edits, and recovering from errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to plan and execute incremental implementation work that spans multiple files, with structured outputs and error-handling guidance. It is aimed at development automation workflows rather than creative judgment tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read and command authority can expose repository contents or make unintended multi-file changes.

Mitigation: Use only in repositories where command execution is acceptable, review proposed commands and diffs before applying them, and avoid exposing sensitive environment variables.

Risk: Vague safeguards may allow incorrect or misleading implementation guidance to enter a codebase.

Mitigation: Require human code review and run relevant tests, linters, or scanners before deployment.

Risk: The artifact describes API key and credential setup workflows that could mishandle secrets if followed carelessly.

Mitigation: Use scoped credentials through approved secret-management channels and avoid placing secrets directly in prompts, files, or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/incremental-implementation)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured responses with code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include implementation plans, file edits, command suggestions, execution status, and error recovery notes.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
