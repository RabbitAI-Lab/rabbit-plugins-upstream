## Description:

Generates Makefiles with testing, linting, formatting, and automation targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or update standard Makefiles for Python, Rust, or TypeScript projects, including common install, lint, format, typecheck, test, build, clean, and publish targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated Makefile may replace an existing project Makefile or include targets that alter local project state.

Mitigation: Check whether a Makefile already exists, ask for a diff or temporary output before replacement, and review publish, clean, install, and build targets before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-makefile-generation)
- [ClawHub publisher profile](https://clawhub.ai/user/athola)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Makefile snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or write a Makefile; generated targets should be reviewed before execution.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
