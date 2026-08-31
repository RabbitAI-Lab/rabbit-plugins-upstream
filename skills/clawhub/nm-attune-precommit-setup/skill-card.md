## Description:

Configures pre-commit hooks for linting, type checking, formatting, and testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add pre-commit quality gates to git projects, including linting, formatting, type checking, tests, custom validation hooks, and CI workflows that mirror local checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated hook and CI configuration can block commits, run project tests, or modify formatted files.

Mitigation: Review the proposed pre-commit and CI configuration before installing hooks or enabling workflows.

Risk: The setup may install or execute third-party quality tooling from configured repositories.

Mitigation: Verify the listed repositories, pinned revisions, and project dependency changes before running installation commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/athola/skills/nm-attune-precommit-setup)
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)
- [pre-commit hooks repository](https://github.com/pre-commit/pre-commit-hooks)
- [Ruff pre-commit repository](https://github.com/astral-sh/ruff-pre-commit)
- [mypy pre-commit mirror](https://github.com/pre-commit/mirrors-mypy)
- [Bandit repository](https://github.com/PyCQA/bandit)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with YAML, TOML, bash, and CI workflow snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose git hook installation commands, pre-commit configuration, quality-check scripts, and CI configuration.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
