## Description:

Helps developers build and maintain GitLab CI/CD pipelines using the CI Tools Components Catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI/CD engineers use this skill to create, repair, and validate component-based GitLab pipelines for builds, tests, packaging, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab credentials may grant access beyond the intended projects.

Mitigation: Scope GITLAB_TOKEN to the intended projects and confirm credential use before installing.

Risk: Pipeline edits may affect deployments, registries, or cluster workflows.

Mitigation: Review generated .gitlab-ci.yml changes and lint the pipeline before pushing; retain existing deployment gates.

## Reference(s):

- [CI Tools Pipeline on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools source repository](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration instructions, Code, Shell commands]

**Output Format:** [Markdown with GitLab CI YAML and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pipeline changes should be linted and reviewed before pushing.]

## Skill Version(s):

1.96.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
