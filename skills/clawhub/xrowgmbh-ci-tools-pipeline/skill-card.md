## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or repair GitLab CI/CD pipeline configurations using documented CI Tools components. It guides component selection, input validation, pipeline linting, and delivery safeguards for application and infrastructure projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pipeline configuration may be uploaded to GitLab during linting, and could contain secrets or information that should remain local.

Mitigation: Review the configuration for sensitive information and confirm which GitLab instance receives it before linting.

Risk: The security scan was partial because it could not resolve a local path-like reference, so its coverage is incomplete.

Mitigation: Review the unresolved reference and inspect the full skill contents before use.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools GitLab Project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance with YAML configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.147.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
