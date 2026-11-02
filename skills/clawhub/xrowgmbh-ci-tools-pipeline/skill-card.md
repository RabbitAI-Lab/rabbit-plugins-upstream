## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, review, and improve GitLab CI/CD pipelines. It helps them select CI Tools components, configure pipeline inputs, and plan validation and delivery flows for application, infrastructure, and GitOps projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CI linting can upload pipeline YAML that contains embedded secrets.

Mitigation: Remove embedded secrets and confirm the intended GitLab server before running validation.

Risk: Pipeline changes can trigger deployments or other writes to registries, clusters, or external systems.

Mitigation: Review generated pipeline changes and deployment gates before pushing or running CI.

Risk: External component implementations may change or may not be included for review.

Mitigation: Prefer pinning components to reviewed versions and review their behavior before use.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Components Source](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with YAML configuration examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pipeline examples and recommendations depend on the project layout, selected components, and delivery requirements.]

## Skill Version(s):

1.124.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
