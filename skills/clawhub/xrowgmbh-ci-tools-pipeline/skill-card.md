## Description: <br>
Builds and maintains GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and DevOps engineers use this skill to create, repair, and validate GitLab CI/CD pipelines with CI Tools catalog components for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated pipeline changes can alter CI behavior, validation gates, or deployment flow. <br>
Mitigation: Review generated .gitlab-ci.yml changes and run GitLab CI lint before pushing. <br>
Risk: GitLab validation and merge-request commands may interact with a project when a token is available. <br>
Mitigation: Use a GitLab token with the narrowest permissions needed and review commands before execution. <br>


## Reference(s): <br>
- [CI Tools Catalog](https://ci-tools.xrow.de/) <br>
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/) <br>
- [CI Tools Source Repository](https://gitlab.com/xrow-public/ci-tools) <br>
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with YAML and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference GitLab CLI, curl, jq, and GITLAB_TOKEN based on project context.] <br>

## Skill Version(s): <br>
1.77.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
