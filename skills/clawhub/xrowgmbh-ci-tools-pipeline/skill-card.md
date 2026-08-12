## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines that use the CI Tools Components Catalog for applications, containers, Helm charts, packages, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to inspect or edit CI configuration and use a GitLab token for validation or merge request pipeline actions.

Mitigation: Install it only in workspaces where that access is acceptable, scope the GitLab token appropriately, and review generated CI changes before pushing or deploying.

Risk: Pipeline changes may affect registry, cluster, deployment, or GitOps behavior if accepted without review.

Mitigation: Keep deployment writes gated by existing project rules, run GitLab CI linting, and verify component inputs against the live CI Tools catalog before merging.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab CI component selections, .gitlab-ci.yml snippets, validation commands, and review checklist guidance.]

## Skill Version(s):

1.81.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
