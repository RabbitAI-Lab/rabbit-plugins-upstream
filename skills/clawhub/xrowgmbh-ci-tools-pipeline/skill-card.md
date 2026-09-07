## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines with CI Tools components for applications, containers, Helm charts, packages, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable third-party GitLab CI component references could later execute changed pipeline code with project credentials.

Mitigation: Pin CI components to reviewed commit SHAs or immutable release tags and verify the external catalog source before adoption.

Risk: Pipeline changes can affect repositories with protected variables, release publishing, deployments, or regulated CI controls.

Mitigation: Review proposed changes in those repositories before installation and preserve existing gates for registry, cluster, and deployment writes.

Risk: Using `ci.skip` can bypass expected pipeline execution on branches where that workflow is not permitted.

Mitigation: Use `ci.skip` only on branches where the team explicitly permits it, then start the intended merge-request pipeline through GitLab controls.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source Repository](https://gitlab.com/xrow-public/ci-tools)
- [CI Tools Pipeline on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [guidance, configuration, code, shell commands]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces pipeline recommendations and validation steps for GitLab CI/CD projects.]

## Skill Version(s):

1.86.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
