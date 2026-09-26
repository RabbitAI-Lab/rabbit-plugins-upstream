## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, fix, and validate GitLab CI/CD pipelines with CI Tools components for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent edit CI configuration and run GitLab CLI commands.

Mitigation: Review generated .gitlab-ci.yml changes before pushing and use a GitLab token limited to the needed projects and actions.

Risk: Pipeline changes may write to registries, clusters, or external systems if deployment jobs are enabled.

Mitigation: Keep registry, cluster, and deployment writes gated by existing project rules and validate the pipeline before pushing.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require glab, curl, jq, and a GitLab token scoped to the target project.]

## Skill Version(s):

1.94.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
