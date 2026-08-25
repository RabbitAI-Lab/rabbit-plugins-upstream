## Description:

Opinionated Python development setup with uv, ty, ruff, pytest, and just for creating or modernizing Python projects and configuring linting, formatting, type checking, testing, pre-commit hooks, build, and CI tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to set up or modernize Python projects with a consistent uv, ty, ruff, pytest, pre-commit, and just workflow. It helps produce project configuration, command recipes, CI checks, and migration guidance for day-to-day Python development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated project files and recipes can change an existing project's dependencies, formatting, checks, or local cleanup behavior.

Mitigation: Review the proposed pyproject.toml, Justfile, pre-commit configuration, migration steps, update recipes, and cleanup commands before applying them, preferably on a branch or disposable copy.

Risk: The recommended ty type checker is beta software and may produce false positives or miss behavior in heavily typed frameworks.

Mitigation: Pin tool versions for repeatable checks and use pyright instead of ty when the project needs more mature type checking.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/python-dev)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/python-dev)
- [uv Reference](references/uv-reference.md)
- [ty Reference](references/ty-reference.md)
- [ruff Reference](references/ruff-reference.md)
- [pytest Reference](references/pytest-reference.md)
- [Justfile Reference](references/justfile-reference.md)
- [uv docs](https://docs.astral.sh/uv/)
- [ty docs](https://docs.astral.sh/ty/)
- [ruff docs](https://docs.astral.sh/ruff/)
- [pytest docs](https://docs.pytest.org/en/stable/)
- [just manual](https://just.systems/man/en/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline TOML, YAML, Justfile, Python, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project configuration templates and command sequences that should be reviewed before applying to existing projects.]

## Skill Version(s):

0.2.5 (source: SKILL.md frontmatter, CHANGELOG.md release entry, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
