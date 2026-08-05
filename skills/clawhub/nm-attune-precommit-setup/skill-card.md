## Description: <br>
Configures pre-commit hooks for linting, type checking, formatting, and testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to configure local and CI-backed pre-commit quality gates for linting, formatting, type checking, testing, security scanning, and project-specific validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated pre-commit hooks and CI workflow changes can run automatically and block commits or pull requests when linting, type checking, tests, or validation checks fail. <br>
Mitigation: Review the generated .pre-commit-config.yaml, scripts, and CI workflow changes before installing them, then run the hooks manually on all files before relying on automatic commit-time execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-precommit-setup) <br>
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>
- [pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks) <br>
- [Ruff pre-commit hook](https://github.com/astral-sh/ruff-pre-commit) <br>
- [Mypy pre-commit mirror](https://github.com/pre-commit/mirrors-mypy) <br>
- [Bandit security scanner](https://github.com/PyCQA/bandit) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with YAML, TOML, Bash, and workflow examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include generated or adapted pre-commit, CI workflow, and quality-check script snippets for review before use.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
