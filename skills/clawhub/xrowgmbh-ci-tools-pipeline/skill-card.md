## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines with xrow CI Tools catalog components for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may skip push-time CI before starting a merge request pipeline.

Mitigation: Confirm the repository permits skipped push pipelines and requires normal merge checks before using that workflow.

Risk: Generated `.gitlab-ci.yml` changes can affect required checks, deployments, registries, or clusters.

Mitigation: Review pipeline edits, validate component inputs against the live catalog, and keep deployment or write operations gated by existing project rules.

Risk: GitLab operations may use `GITLAB_TOKEN` and local CLI tooling.

Mitigation: Use the narrowest practical GitLab token scope and verify `glab`, `curl`, and `jq` behavior before running commands.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference GitLab CLI, curl, jq, and GITLAB_TOKEN-dependent workflows.]

## Skill Version(s):

1.93.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
