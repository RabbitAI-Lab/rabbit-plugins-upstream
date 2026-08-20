## Description:

Generates Makefiles with testing, linting, formatting, and automation targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or update Makefiles for Python, Rust, and TypeScript projects with standard targets for installation, linting, formatting, testing, building, cleaning, and release workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Makefile targets can change developer workflows or replace an existing Makefile if accepted without review.

Mitigation: Review the generated Makefile as a diff and require confirmation before replacing or writing a project Makefile.

## Reference(s):

- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-makefile-generation)

## Skill Output:

**Output Type(s):** [code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Makefile snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose writing or replacing a project Makefile; generated files should be reviewed before acceptance.]

## Skill Version(s):

1.9.18 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
