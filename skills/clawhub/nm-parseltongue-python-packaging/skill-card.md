## Description: <br>
Python package creation and PyPI distribution via pyproject.toml and entry points. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for Python packaging tasks, including pyproject.toml setup, dependency management with uv, entry point configuration, CI/CD publishing workflows, and PyPI distribution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing examples can push packages to the wrong registry or use sensitive PyPI tokens if copied without review. <br>
Mitigation: Inspect build artifacts, prefer TestPyPI first, confirm the target registry, and keep PyPI tokens in secrets. <br>
Risk: Cleanup examples can remove build or distribution directories in the current working directory. <br>
Mitigation: Double-check the current directory before deleting build/ or dist/. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-parseltongue-python-packaging) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/parseltongue) <br>
- [uv workflow module](modules/uv-workflow.md) <br>
- [pyproject.toml patterns module](modules/pyproject-patterns.md) <br>
- [entry points module](modules/entry-points.md) <br>
- [CI/CD integration module](modules/ci-cd-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; outputs packaging recommendations and examples for user review.] <br>

## Skill Version(s): <br>
1.9.16 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
