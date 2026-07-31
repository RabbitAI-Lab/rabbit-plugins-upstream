## Description: <br>
Python package creation and PyPI distribution via pyproject.toml and entry points. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create Python packages, configure pyproject.toml, define entry points, manage uv workflows, and prepare PyPI or CI-based releases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing examples can upload packages to public registries. <br>
Mitigation: Before running uv publish or CI publishing workflows, confirm the target registry, credentials, package contents, package version, and whether the release will become public; test on TestPyPI first when appropriate. <br>
Risk: CI/CD examples rely on publishing credentials. <br>
Mitigation: Store registry tokens in repository secrets, limit token scope, and review workflow triggers before enabling automated publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-parseltongue-python-packaging) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [metadata.clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/parseltongue) <br>
- [uv workflow module](artifact/modules/uv-workflow.md) <br>
- [pyproject.toml patterns module](artifact/modules/pyproject-patterns.md) <br>
- [entry points module](artifact/modules/entry-points.md) <br>
- [CI/CD integration module](artifact/modules/ci-cd-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell, TOML, YAML, and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes packaging, publishing, and CI examples that require users to confirm package contents, registry targets, credentials, and release visibility before execution.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
