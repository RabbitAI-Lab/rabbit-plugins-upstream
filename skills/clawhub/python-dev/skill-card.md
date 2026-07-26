## Description: <br>
Opinionated Python development setup with uv, ty, ruff, pytest, and just for creating or modernizing Python projects and configuring linting, type checking, testing, and build tooling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to bootstrap or modernize Python projects with a consistent uv, ty, ruff, pytest, pre-commit, and just workflow. It provides setup guidance, configuration templates, shell commands, and reference material for common project maintenance tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested setup and maintenance commands can change project files or developer environment state. <br>
Mitigation: Review generated templates and commands before applying them, especially ruff --fix, uv lock --upgrade, uv sync --all-groups, pre-commit install, cleanup commands, global Python pinning, and publishing commands. <br>
Risk: The ty type checker is described by the artifact as beta software and may produce false positives for heavily typed frameworks. <br>
Mitigation: For projects that require stable type checking, review ty results carefully or swap ty for pyright while keeping the rest of the stack. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/python-dev) <br>
- [Publisher Profile](https://clawhub.ai/user/tenequm) <br>
- [OpenClaw Homepage](https://github.com/tenequm/skills/tree/main/skills/python-dev) <br>
- [uv Reference](references/uv-reference.md) <br>
- [ty Reference](references/ty-reference.md) <br>
- [ruff Reference](references/ruff-reference.md) <br>
- [pytest Reference](references/pytest-reference.md) <br>
- [justfile Reference](references/justfile-reference.md) <br>
- [uv Documentation](https://docs.astral.sh/uv/) <br>
- [ty Documentation](https://docs.astral.sh/ty/) <br>
- [ruff Documentation](https://docs.astral.sh/ruff/) <br>
- [pytest Documentation](https://docs.pytest.org/en/stable/) <br>
- [just Manual](https://just.systems/man/en/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with TOML, YAML, justfile, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project setup guidance and editable templates for Python project configuration, CI, pre-commit hooks, and local development commands.] <br>

## Skill Version(s): <br>
0.2.3 (source: frontmatter, changelog, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
