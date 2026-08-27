## Description:

Guides agents working in Go repositories that use or adopt uber-go/fx for application wiring, lifecycle hooks, modules, annotations, decorators, supplied values, replacement, logging, testing, and signal-aware run loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to modify, review, and test Go services that use uber-go/fx for dependency injection, lifecycle management, module organization, event logging, and graceful shutdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose Go dependency commands or code edits that affect important repositories.

Mitigation: Review suggested commands such as go get before running them, and run the repository's normal Go tests or lint checks after changes.

Risk: fx examples can involve configuration and secrets being supplied into the application graph.

Mitigation: Check config and secret handling before committing changes, especially when wiring values with fx.Supply or named annotations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-uber-fx)
- [Metadata Homepage](https://github.com/samber/cc-skills-golang)
- [pkg.go.dev: go.uber.org/fx](https://pkg.go.dev/go.uber.org/fx)
- [uber-go/fx Documentation](https://uber-go.github.io/fx/)
- [uber-go/fx Repository](https://github.com/uber-go/fx)
- [Advanced uber-go/fx Reference](references/advanced.md)
- [uber-go/fx Recipes](references/recipes.md)
- [Testing with uber-go/fx](references/testing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May suggest Go dependency, lint, test, and code-navigation commands when they are relevant to the user's fx task.]

## Skill Version(s):

1.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
