## Description:

Modernize Golang code to use recent language features, standard library improvements, and idiomatic patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review and update Go projects for newer language features, standard library APIs, testing patterns, and tooling. It supports focused inline suggestions while coding and broader full-codebase modernization scans when explicitly invoked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can propose and apply broad Go modernization edits across a codebase.

Mitigation: Use full-scan mode only for broad reviews, prefer the documented isolated worktree flow for sweeping changes, and review generated changes before merging.

Risk: The skill can run Go, golangci-lint, and git commands as part of modernization work.

Mitigation: Review command intent before execution and run tests or lint checks appropriate to the target project before accepting changes.

Risk: Ignored modernization suggestions may be recorded in a project .modernize file.

Mitigation: Review any .modernize updates during code review to confirm they reflect team decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-modernize)
- [Project homepage](https://github.com/samber/cc-skills-golang)
- [Tooling modernization](artifact/references/tooling.md)
- [Go version modernizations](artifact/references/versions.md)
- [Go 1.21 release notes](https://go.dev/doc/go1.21)
- [Go 1.22 release notes](https://go.dev/doc/go1.22)
- [Go 1.23 release notes](https://go.dev/doc/go1.23)
- [Go 1.24 release notes](https://go.dev/doc/go1.24)
- [Go 1.25 release notes](https://go.dev/doc/go1.25)
- [Go 1.26 release notes](https://go.dev/doc/go1.26)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits, isolated worktree changes, and modernization review findings for Go projects.]

## Skill Version(s):

1.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
