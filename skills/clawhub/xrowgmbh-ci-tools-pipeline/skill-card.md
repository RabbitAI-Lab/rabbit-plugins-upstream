## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de for creating or fixing .gitlab-ci.yml files, choosing components, validating inputs, and designing delivery pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select CI Tools components, update GitLab pipeline configuration, validate component inputs, and troubleshoot CI/CD workflows for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated GitLab CI/CD configuration can change validation, release, registry, cluster, or deployment behavior.

Mitigation: Review proposed .gitlab-ci.yml changes, confirm component inputs against the live catalog, and lint the pipeline before pushing.

Risk: GitLab commands or tokens can affect the target project if run with broad permissions.

Mitigation: Use a GitLab token scoped appropriately for the project and review git push or pipeline-run commands before allowing them.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with YAML and bash snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose .gitlab-ci.yml edits and GitLab CLI commands for validation or pipeline runs.]

## Skill Version(s):

1.80.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
