## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to create, validate, and maintain GitLab CI/CD pipelines with reusable CI Tools catalog components for application, infrastructure, documentation, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes CI linting as local, but the lint command sends pipeline configuration to GitLab.

Mitigation: Confirm glab targets the intended GitLab project and host before linting, and use appropriately scoped credentials.

Risk: Generated pipeline changes may affect registries, clusters, or other external systems when pushed or run.

Mitigation: Review generated changes before pushing, keep secrets out of pipeline YAML, and consider pinning catalog components to reviewed versions.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components](https://ci-tools.xrow.de/Components/)
- [CI Tools GitLab Project](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with YAML configuration examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.123.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
