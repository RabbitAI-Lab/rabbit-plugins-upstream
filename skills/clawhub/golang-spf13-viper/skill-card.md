## Description:

Guides Go developers using spf13/viper through layered configuration precedence, flag and environment binding, config files, unmarshalling, sub-trees, hot reload, test isolation, and remote key-value configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill when adding, debugging, or reviewing spf13/viper configuration in Go projects, especially when the codebase imports github.com/spf13/viper or combines files, flags, environment variables, defaults, and optional remote configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate in Go projects that import spf13/viper even when only a narrow configuration issue is being handled.

Mitigation: Review proposed guidance and edits for relevance before applying dependency, configuration, or code changes.

Risk: Generated configuration advice can introduce incorrect precedence, binding, reload, or test-isolation behavior if applied without project context.

Mitigation: Validate changes with project tests and inspect viper setup for flag binding, environment key replacement, mapstructure tags, and isolated viper instances.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-spf13-viper)
- [Publisher Profile](https://clawhub.ai/user/samber)
- [OpenClaw Homepage](https://github.com/samber/cc-skills-golang)
- [pkg.go.dev/github.com/spf13/viper](https://pkg.go.dev/github.com/spf13/viper)
- [github.com/spf13/viper](https://github.com/spf13/viper)
- [Viper Config Sources and File Formats](references/sources-and-formats.md)
- [Viper Env Binding and Flag Binding](references/binding-and-env.md)
- [Viper Unmarshal and Struct Mapping](references/unmarshal.md)
- [Viper WatchConfig and Hot Reload](references/watch-and-reload.md)
- [Viper Test Isolation](references/testing-and-isolation.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Go code edits, configuration patterns, diagnostic commands, and dependency commands for projects using spf13/viper.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
