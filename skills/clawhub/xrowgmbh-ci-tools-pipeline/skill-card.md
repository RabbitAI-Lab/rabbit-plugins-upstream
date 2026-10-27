## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose CI Tools catalog components and create, maintain, or troubleshoot GitLab CI/CD pipeline configuration for their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended label component can delete existing project labels.

Mitigation: Remove the label component or set its prune input to false unless deleting existing labels is intended.

Risk: Pipeline changes can affect deployment behavior, credentials, or the destination receiving lint requests.

Mitigation: Review generated pipeline changes, pin reviewed component versions, use narrowly scoped credentials, verify the GitLab lint destination, and keep secrets out of pipeline YAML.

## Reference(s):

- [CI Tools catalog](https://ci-tools.xrow.de/)
- [CI Tools Components index](https://ci-tools.xrow.de/Components/)
- [CI Tools source repository (listed in skill documentation)](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands]

**Output Format:** [Markdown guidance with YAML configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.122.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
