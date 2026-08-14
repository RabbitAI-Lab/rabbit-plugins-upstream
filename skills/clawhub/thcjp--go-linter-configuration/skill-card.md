## Description:

Configures and troubleshoots golangci-lint for Go projects, including import resolution, type checking, and linter preset tuning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Go maintainers use this skill to configure golangci-lint, generate or tune .golangci.yml settings, and troubleshoot import resolution or type-checking failures in Go repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports broad read, write, and command authority while the skill scope and execution behavior are inconsistently described.

Mitigation: Install only for golangci-lint configuration work in a Go repository, review proposed file changes and commands before execution, and keep command execution constrained to the approved task.

Risk: Broad repository access can expose unrelated secrets or sensitive files if the skill is used outside its intended scope.

Mitigation: Avoid supplying unrelated API keys or credentials, run it in the minimum necessary workspace, and inspect outputs before accepting changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/go-linter-configuration)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON examples, configuration snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file changes and commands for golangci-lint configuration; review before applying.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
