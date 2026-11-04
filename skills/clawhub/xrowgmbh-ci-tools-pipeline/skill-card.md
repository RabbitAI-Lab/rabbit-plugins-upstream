## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or maintain GitLab CI/CD pipelines, select CI Tools catalog components, check component inputs, and plan continuous delivery for application, infrastructure, and documentation projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote pipeline linting sends the YAML to GitLab, where secrets included in it could be exposed.

Mitigation: Verify the GitLab host and project, use appropriately scoped credentials, and keep secrets out of pipeline YAML.

Risk: External catalog component implementations may change and are not bundled or audited with this skill.

Mitigation: Review component implementations, pin components to reviewed versions where practical, and inspect generated jobs before pushing or starting CI, especially publishing and deployment jobs.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source Repository](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance with YAML configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and examples depend on the repository and selected CI Tools components.]

## Skill Version(s):

1.128.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
