## Description:

Opinionated Python development setup with uv, ty, ruff, pytest, and just. Use when creating a new Python project, writing or fixing pyproject.toml, or configuring linting, formatting, type checking, testing, pre-commit hooks, or build and CI tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to create or modernize Python projects with an opinionated uv, ty, ruff, pytest, pre-commit, and just workflow. It helps produce project configuration, command recipes, CI snippets, and migration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated project configuration can overwrite or conflict with an existing Python project's conventions.

Mitigation: Review pyproject.toml, Justfile, pre-commit, and CI snippets before applying them to an existing repository.

Risk: The clean recipe deletes build, cache, coverage, and __pycache__ directories from the current project tree.

Mitigation: Run cleanup commands only from the intended project root and inspect the recipe before execution.

Risk: The update recipe can change locked dependencies.

Mitigation: Review dependency changes and test the project after running update commands.

Risk: ty is beta software and may produce false positives or miss behavior in heavily typed frameworks.

Mitigation: Use pyright instead of ty for projects that need mature type checking, as the skill itself recommends.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/python-dev)
- [Source Homepage](https://github.com/tenequm/skills/tree/main/skills/python-dev)
- [uv Reference](references/uv-reference.md)
- [ty Reference](references/ty-reference.md)
- [ruff Reference](references/ruff-reference.md)
- [pytest Reference](references/pytest-reference.md)
- [Justfile Reference](references/justfile-reference.md)
- [uv Documentation](https://docs.astral.sh/uv/)
- [ty Documentation](https://docs.astral.sh/ty/)
- [ruff Documentation](https://docs.astral.sh/ruff/)
- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [just Manual](https://just.systems/man/en/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, TOML, YAML, and Justfile code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped setup and migration guidance; generated configuration should be reviewed before use in an existing repository.]

## Skill Version(s):

0.2.4 (source: SKILL.md frontmatter and CHANGELOG, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
