## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to select CI Tools catalog components and create, review, or troubleshoot GitLab CI/CD pipelines for application, infrastructure, packaging, documentation, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended label component can automatically delete existing project labels.

Mitigation: Omit the label component or set prune:false unless deleting other project labels is intended.

Risk: Pipeline linting sends configuration to GitLab, where embedded secrets could be exposed.

Mitigation: Verify the lint destination and remove embedded secrets before linting.

Risk: Component defaults and complete remote implementations are not verified for each project.

Mitigation: Review component defaults, pin reviewed versions, and restrict token access to the intended project.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools GitLab Project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Text, Markdown, YAML configuration, Shell commands, Guidance]

**Output Format:** [Markdown with GitLab CI YAML examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pipeline configuration and review guidance tailored to the project.]

## Skill Version(s):

1.127.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
