## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to select CI Tools catalog components and build or repair GitLab CI/CD pipelines for application, package, infrastructure, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CI lint workflow contacts GitLab and uploads pipeline configuration, although the skill describes validation as local.

Mitigation: Confirm the intended GitLab host before linting and review changes before pushing or running CI.

Risk: Components referenced through the moving @main version may change after review.

Mitigation: Consider pinning components to reviewed versions.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools GitLab Project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with YAML configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include component selections, inputs, and validation steps.]

## Skill Version(s):

1.115.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
