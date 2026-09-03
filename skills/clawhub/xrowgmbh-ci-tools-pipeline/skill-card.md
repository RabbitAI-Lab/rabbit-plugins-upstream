## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to create, repair, and review GitLab CI/CD pipelines that use CI Tools catalog components. It helps choose components, validate inputs, and keep pipeline behavior aligned with existing project release, registry, deployment, and GitOps rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pipeline changes can affect registries, packages, clusters, Helm charts, or deployments.

Mitigation: Review proposed pipeline changes before pushing, preserve existing deployment gates, and run GitLab CI lint before executing the pipeline.

Risk: GitLab validation may require a token with access to repository or CI actions.

Mitigation: Use an appropriately scoped GITLAB_TOKEN and avoid exposing it in generated configuration, command output, or logs.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires project context and GitLab tooling when validation is requested.]

## Skill Version(s):

1.84.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
