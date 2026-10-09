## Description:

Helps developers build and maintain GitLab CI/CD pipelines using the CI Tools Components Catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI maintainers use this skill to select catalog components, edit GitLab pipeline configuration, and validate changes for application, container, Helm, documentation, and infrastructure projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Validation accesses the external CI Tools catalog and GitLab.

Mitigation: Confirm outbound access to ci-tools.xrow.de and GitLab before running validation.

Risk: GitLab operations can push branches and trigger merge request pipelines.

Mitigation: Use a least-privilege GitLab token and review proposed changes before pushing or starting CI.

Risk: Pipeline changes could write to registries, clusters, or deployment systems.

Mitigation: Keep deploy writes gated by existing project rules and validate the pipeline before deployment.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools catalog source](https://gitlab.com/xrow-public/ci-tools)
- [CI Tools Pipeline on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [GitLab CI YAML and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Component selection, validation steps, and merge request guidance.]

## Skill Version(s):

1.109.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
