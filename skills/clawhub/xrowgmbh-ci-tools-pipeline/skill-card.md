## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, review, and troubleshoot GitLab CI/CD pipelines using the CI Tools Components Catalog. It helps select components, configure their inputs, and validate pipeline changes before pushing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pipeline validation sends configuration to the selected GitLab destination; secrets or unreviewed changes could expose sensitive data or trigger unintended deployments.

Mitigation: Confirm the GitLab destination before linting, keep secrets out of configuration files, and review generated changes and deployment gates before pushing.

Risk: Catalog components referenced with @main can change after review.

Mitigation: Consider pinning catalog components to reviewed versions.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components](https://ci-tools.xrow.de/Components/)
- [CI Tools GitLab project](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [GitLab CI YAML configuration, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pipeline validation and deployment guidance.]

## Skill Version(s):

1.118.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
