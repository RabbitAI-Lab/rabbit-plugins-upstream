## Description:

Helps developers build and maintain GitLab CI/CD pipelines using the CI Tools Components Catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to select CI Tools components, create or repair GitLab pipeline configuration, and validate continuous delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pipeline changes may introduce unintended deployments or registry writes.

Mitigation: Review generated CI configuration, especially deployment jobs and write permissions, before running a pipeline.

Risk: Mutable component references such as @main may change after review.

Mitigation: Review component references and their live documentation before adopting or updating them.

Risk: GitLab commands may use GITLAB_TOKEN to push branches or run merge-request pipelines.

Mitigation: Use an appropriately scoped token and authorize pushes or pipeline runs before execution.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools Pipeline on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration instructions, Code, Shell commands, Guidance]

**Output Format:** [Markdown with GitLab CI YAML and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose changes to .gitlab-ci.yml and related CI configuration.]

## Skill Version(s):

1.97.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
