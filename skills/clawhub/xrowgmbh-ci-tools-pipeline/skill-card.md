## Description: <br>
Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, validate, and repair GitLab CI/CD pipelines using CI Tools components for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated CI/CD changes could alter deployment, registry, or pipeline behavior. <br>
Mitigation: Review generated pipeline diffs and validate changes with GitLab CI linting before pushing or running merge request pipelines. <br>
Risk: A GitLab token with excessive permissions could expand the impact of mistakes. <br>
Mitigation: Provide only the minimum GitLab token permissions needed for the repository task. <br>


## Reference(s): <br>
- [CI Tools Catalog](https://ci-tools.xrow.de/) <br>
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/) <br>
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools) <br>
- [CI Tools Pipeline on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference GitLab CI configuration, CI Tools component inputs, glab, curl, jq, and GITLAB_TOKEN.] <br>

## Skill Version(s): <br>
1.78.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
