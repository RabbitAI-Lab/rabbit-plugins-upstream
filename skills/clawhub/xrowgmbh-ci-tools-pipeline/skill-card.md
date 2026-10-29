## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to create or repair GitLab CI/CD pipelines with xrow's CI Tools Components Catalog. It helps select components, validate their inputs, and plan build, test, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pipeline linting sends configuration to the active GitLab host, despite being described as local validation.

Mitigation: Confirm the GitLab host and account before linting, and use a scoped token.

Risk: Generated jobs or release and deployment rules may trigger unintended external changes.

Mitigation: Review generated jobs and deployment rules before pushing or starting pipelines.

Risk: Components referenced at @main can change over time.

Mitigation: Pin trusted component versions when a stable pipeline definition is required.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source Repository](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration, Code, Shell commands, Guidance]

**Output Format:** [Markdown with GitLab CI YAML examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.122.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
