## Description:

Provides Go code style guidance for line breaking, variable declarations, control flow clarity, comments, function design, collection initialization, and file organization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to write or review Go code for clear, maintainable style. It is intended for Go source files and focuses on judgment-based style concerns that complement automated formatting and linting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide edits to Go files.

Mitigation: Use it only for intended Go style work and review proposed diffs before accepting changes.

Risk: The skill may use Go, golangci-lint, git, or review sub-agents for large code-style tasks.

Mitigation: Run those commands only in trusted repositories and check command intent before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-code-style)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Code Style Details](references/details.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Go code examples and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide edits to Go files and large style reviews using Go tooling, golangci-lint, git, or review sub-agents when appropriate.]

## Skill Version(s):

1.3.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
