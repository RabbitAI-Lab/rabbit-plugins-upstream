## Description:

Builds and maintains GitLab CI/CD pipelines using the CI Tools Components Catalog for testing, packaging, and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or repair component-driven GitLab pipelines and validate their configuration before enabling delivery jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pipeline changes may publish artifacts or deploy to registries and clusters.

Mitigation: Review generated .gitlab-ci.yml changes and deployment gates before pushing.

Risk: Component includes pinned to @main may change without notice.

Mitigation: Pin CI Tools component versions when reproducibility or change control matters.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools documentation](https://ci-tools.xrow.de/)
- [CI Tools component source](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with GitLab CI YAML and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CI Tools components; validation may require glab, curl, jq, and GITLAB_TOKEN.]

## Skill Version(s):

1.111.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
