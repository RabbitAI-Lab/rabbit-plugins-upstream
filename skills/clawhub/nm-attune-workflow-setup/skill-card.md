## Description: <br>
Configures GitHub Actions CI/CD workflows for testing, linting, and deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create or update GitHub Actions workflows for Python, Rust, and TypeScript projects, including testing, linting, type checking, build, release, and deployment pipelines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated GitHub Actions workflows can affect publishing, deployment, repository secrets, or external services. <br>
Mitigation: Review all generated .github/workflows files before committing, especially publish or deploy workflows. <br>
Risk: Broad activation phrases may trigger workflow setup guidance when an agent is working near CI/CD automation tasks. <br>
Mitigation: Install only when you want agent assistance creating or updating GitHub Actions workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-workflow-setup) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python snippets, and GitHub Actions YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may lead to new or updated .github/workflows files; review generated workflow files before committing.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
