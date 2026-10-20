## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or maintain GitLab CI/CD pipelines with reusable CI Tools components. It helps select components, configure their inputs, and validate pipeline designs for application, package, documentation, infrastructure, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pipeline changes may be incorrect, and included components can change when referenced through a moving branch such as @main.

Mitigation: Review and validate generated pipeline changes, and pin components to reviewed commits or releases.

Risk: Pipeline changes may run with GitLab credentials or access deployment resources.

Mitigation: Limit token permissions and project membership, and review changes before running them with secrets.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Components Source Repository](https://gitlab.com/xrow-public/ci-tools)
- [GitLab Token Guidance](https://ci-tools.xrow.de/gitlab-token/)
- [ClawHub Skill Release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)
- [Publisher Profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [GitLab CI YAML configuration, shell command examples, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are tailored to the repository structure, pipeline needs, and deployment controls described by the user.]

## Skill Version(s):

1.114.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
