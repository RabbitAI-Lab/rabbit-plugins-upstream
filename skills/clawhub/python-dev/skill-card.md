## Description:

Opinionated Python development setup with uv, ty, ruff, pytest, lefthook, and just. Use when creating a new Python project, writing or fixing pyproject.toml, or configuring linting, formatting, type checking, testing, git hooks, or CI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to create or modernize Python projects with a consistent uv, ruff, ty, pytest, lefthook, just, and CI setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated project files and workflow snippets may conflict with local policy for tool versions, cleanup commands, CI behavior, or auto-fixing git hooks.

Mitigation: Review the generated pyproject.toml, Justfile, lefthook.yml, and CI workflow before applying them.

Risk: Some recommended commands install dependencies, add git hooks, or modify project files.

Mitigation: Run setup in a branch or disposable workspace, inspect diffs, and keep mutating commands out of pre-push workflows.

Risk: The skill recommends ty, which the artifact identifies as beta software with type inference that can change between releases.

Mitigation: Pin ty versions tightly and use pyright instead when stable type-checker behavior is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/python-dev)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/python-dev)
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
- [lefthook docs](https://lefthook.dev/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code blocks and configuration templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project setup guidance, file templates, and command recommendations for the agent to adapt to a Python repository.]

## Skill Version(s):

0.3.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
