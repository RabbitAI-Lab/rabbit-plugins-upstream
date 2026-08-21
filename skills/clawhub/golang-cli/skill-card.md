## Description:

Golang CLI application development for building, modifying, and reviewing Go CLI tools, including command structure, flags, configuration, versioning, exit codes, I/O, signals, completions, argument validation, and tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, extend, and review Go command-line applications with predictable Cobra/Viper structure, configuration layering, shell behavior, and tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to edit Go code and run Go, golangci-lint, and git commands in a repository.

Mitigation: Use it in repositories where Go CLI development actions are intended, and review proposed commands and diffs before accepting changes.

Risk: Generated CLI changes can alter observable command behavior such as configuration precedence, exit codes, stdout/stderr separation, and shell completion.

Mitigation: Run focused CLI tests and inspect command output, error handling, flag binding, and exit-code behavior before release.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-cli)
- [Project Homepage](https://github.com/samber/cc-skills-golang)
- [Root Command Example](assets/examples/root.go)
- [Configuration Example](assets/examples/config.go)
- [CLI Test Example](assets/examples/cli_test.go)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go code examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for Go CLI implementation and review; examples focus on Cobra, Viper, Unix exit codes, stdout/stderr separation, signal handling, completions, and tests.]

## Skill Version(s):

1.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
