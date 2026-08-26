## Description:

A Go CLI engineering guide for building, extending, and reviewing spf13/cobra command trees, flags, completions, documentation generation, and tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when adopting or maintaining spf13/cobra in Go CLIs, including command-tree design, flags, argument validation, completions, documentation generation, and test patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested dependency or scaffolding commands may change a Go module or create project files.

Mitigation: Review the proposed command and resulting diff before committing generated dependency or scaffold changes.

Risk: Generated Cobra handlers, hooks, or validators may encode incorrect CLI behavior for the application.

Mitigation: Review generated code against the intended command contract and run focused command tests before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-spf13-cobra)
- [Publisher profile](https://clawhub.ai/user/samber)
- [ClawHub metadata homepage](https://github.com/samber/cc-skills-golang)
- [spf13/cobra package docs](https://pkg.go.dev/github.com/spf13/cobra)
- [spf13/cobra GitHub repository](https://github.com/spf13/cobra)
- [Cobra documentation](https://cobra.dev)
- [Cobra commands, hooks, and args validators](references/commands-and-args.md)
- [Cobra flags reference](references/flags.md)
- [Cobra shell completions reference](references/completions.md)
- [Cobra documentation generators](references/generators.md)
- [Testing Cobra commands](references/testing.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Markdown]

**Output Format:** [Markdown with Go and bash code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Go code changes, dependency commands, cobra-cli scaffolding commands, and test patterns for caller review.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
