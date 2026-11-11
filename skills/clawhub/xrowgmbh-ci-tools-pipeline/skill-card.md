## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to select CI Tools components and create, review, or troubleshoot GitLab CI/CD pipelines across application, infrastructure, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CI linting may send pipeline configuration to the configured GitLab instance, including sensitive information.

Mitigation: Review the configuration for secrets and confirm the configured GitLab instance is trusted before using CI linting.

Risk: The security scan was partial because a local path-like reference could not be resolved.

Mitigation: Review the referenced local path and its target before relying on the scan as a complete assessment.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components](https://ci-tools.xrow.de/Components/)
- [xrow CI Tools Components project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with YAML pipeline examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Component selection and validation guidance for GitLab CI/CD pipelines.]

## Skill Version(s):

1.137.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
