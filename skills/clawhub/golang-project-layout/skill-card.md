## Description:

Provides a guide for setting up Golang project layouts and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and apply Go project layouts for new projects, existing codebases, CLI tools, services, libraries, monorepos, and workspace setups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to add a persistent always-load directive to CLAUDE.md, AGENTS.md, or an equivalent agent configuration file.

Mitigation: Review and explicitly approve the exact configuration-file change before allowing it to be written.

## Reference(s):

- [Project homepage](https://github.com/samber/cc-skills-golang)
- [12-Factor App](https://12factor.net/)
- [Application Configuration with Cobra + Viper](references/config.md)
- [Directory Layouts](references/directory-layouts.md)
- [Tests, Benchmarks, and Examples](references/testing-layout.md)
- [Go Workspaces for Multi-Package Repositories](references/workspaces.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Go directory trees, code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go tooling for command examples; may propose edits to project layout and agent configuration files.]

## Skill Version(s):

1.4.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
