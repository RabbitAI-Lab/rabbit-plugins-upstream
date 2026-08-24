## Description:

Helps agents review and edit Go code to prevent panics, silent data corruption, and subtle runtime bugs such as nil panics, append aliasing, unsafe map access, numeric conversion overflow, resource lifecycle issues, and missing defensive copies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to make Go code safer during implementation or review, especially around nil handling, slice and map aliasing, numeric conversion, resource lifetime, and defensive-copy patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can edit Go source files and run go, golangci-lint, and git commands.

Mitigation: Use it in repositories where those actions are acceptable, then review diffs and command output before accepting changes.

Risk: Safety guidance or edits may be incomplete or incorrect for project-specific APIs, concurrency assumptions, or compatibility targets.

Mitigation: Run the project's Go tests and linters, and have a maintainer review changes before release.

## Reference(s):

- [Nil Safety Deep Dive](references/nil-safety.md)
- [Slice and Map Safety Deep Dive](references/slice-map-safety.md)
- [Project Homepage](https://github.com/samber/cc-skills-golang)
- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-safety)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands]

**Output Format:** [Markdown guidance with Go code examples, suggested code edits, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit Go source files and run go, golangci-lint, and git commands when invoked.]

## Skill Version(s):

1.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
