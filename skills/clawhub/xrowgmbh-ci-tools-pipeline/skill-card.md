## Description:

Helps developers build and maintain GitLab CI/CD pipelines using the CI Tools Components Catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select CI Tools components, create or fix GitLab pipeline configuration, and validate delivery workflows for applications, containers, charts, documentation, and infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pipeline changes can affect CI checks, deployments, or external systems.

Mitigation: Review and lint .gitlab-ci.yml before pushing; retain existing deployment gates and required checks.

Risk: Component examples reference the live main branch and may change over time.

Mitigation: Check component inputs against the live catalog and review included components before use.

Risk: GitLab commands may use a token with access to the target project.

Mitigation: Use a token with only the permissions needed for the target project.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools documentation](https://ci-tools.xrow.de/)
- [CI Tools component project](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with GitLab CI YAML and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, curl, and jq; GitLab access uses GITLAB_TOKEN.]

## Skill Version(s):

1.106.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
