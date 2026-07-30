## Description: <br>
Configures GitHub Actions CI/CD workflows for testing, linting, and deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to set up or update GitHub Actions workflows for CI/CD, testing, linting, type checking, publishing, and deployment in Python, Rust, or TypeScript projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or suggested GitHub Actions workflows can change repository CI/CD behavior, including publish or deploy jobs that may run on releases. <br>
Mitigation: Review all .github/workflows changes before committing, with extra scrutiny for jobs that publish artifacts, deploy services, or access repository secrets. <br>
Risk: Workflow guidance may include shell snippets where incorrect error handling can hide failing checks. <br>
Mitigation: Use explicit shell error handling such as pipefail or captured exit codes, and validate workflow YAML before relying on the workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-workflow-setup) <br>
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML, Python, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces workflow setup guidance and example GitHub Actions configuration for repository review before use.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
