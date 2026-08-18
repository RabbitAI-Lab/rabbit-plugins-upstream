## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines based on the CI Tools Components Catalog. It helps choose components, confirm inputs, lint pipeline configuration, and design delivery flows for applications, containers, Helm charts, packages, documentation, infrastructure, and GitOps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to use a GitLab token, push branches, or trigger merge request pipelines.

Mitigation: Review proposed GitLab actions and generated pipeline changes before allowing pushes or token-backed operations.

Risk: Pipeline changes can affect registries, clusters, deployment rules, or GitOps flows.

Mitigation: Keep deployment and write operations gated by existing project rules, and review deployment-related jobs before execution.

Risk: Live catalog lookups can make recommendations depend on current external documentation.

Mitigation: Verify component names and inputs against the CI Tools catalog before committing pipeline configuration.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab CI configuration changes, validation commands, component recommendations, and review checklists.]

## Skill Version(s):

1.84.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
