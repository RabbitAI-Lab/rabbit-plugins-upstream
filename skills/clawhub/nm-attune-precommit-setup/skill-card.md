## Description: <br>
Configures pre-commit hooks for linting, type checking, formatting, and testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add or improve pre-commit quality gates for linting, formatting, type checking, tests, security scans, component-level checks, and CI-aligned validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or adopted pre-commit hooks can execute local scripts automatically during commits. <br>
Mitigation: Review the generated .pre-commit-config.yaml and any referenced local scripts or Makefile targets before installing hooks. <br>
Risk: CI examples can upload coverage data to Codecov if the optional workflow step is enabled. <br>
Mitigation: Review CI configuration and remove or configure coverage upload for the project's data-sharing policy. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-attune-precommit-setup) <br>
- [OpenClaw Metadata Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>
- [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) <br>
- [Ruff pre-commit](https://github.com/astral-sh/ruff-pre-commit) <br>
- [mypy pre-commit mirror](https://github.com/pre-commit/mirrors-mypy) <br>
- [Bandit](https://github.com/PyCQA/bandit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML, TOML, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes layered pre-commit patterns, CI examples, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
