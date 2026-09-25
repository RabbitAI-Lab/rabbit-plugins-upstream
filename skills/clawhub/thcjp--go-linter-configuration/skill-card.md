## Description:

Configures and troubleshoots golangci-lint for Go projects, including import resolution, type-checking issues, and linter preset selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to configure golangci-lint, tune linter presets, and troubleshoot Go import or type-checking failures in a target repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated linter configuration, import fixes, or shell commands could be incorrect or unsuitable for a specific Go repository.

Mitigation: Review proposed configuration and commands before applying them, and test changes in the intended repository.

Risk: The artifact includes broad quality, security, and compliance scoring language that may be mistaken for a formal audit.

Mitigation: Treat any scoring or compliance guidance as advisory and use established review, testing, and security scanning processes for assurance.

Risk: The skill can guide file changes and command execution during troubleshooting.

Mitigation: Keep agent activity scoped to the target repository and avoid applying commands outside the intended project context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/go-linter-configuration)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose .golangci.yml configuration, import or module fixes, linter preset choices, and troubleshooting guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
