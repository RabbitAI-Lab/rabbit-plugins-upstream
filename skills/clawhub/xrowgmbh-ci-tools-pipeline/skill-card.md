## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI/CD maintainers use this skill to create, repair, and validate GitLab CI/CD pipelines based on CI Tools components for applications, containers, Helm charts, infrastructure, documentation, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use of a GitLab token can let an agent push branches or start CI pipelines.

Mitigation: Require explicit approval before any git push or glab ci run command.

Risk: CI jobs may write to registries, clusters, or production-like systems through existing project rules.

Mitigation: Verify deploy and protected-branch rules before allowing pipeline runs that can publish or deploy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)
- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools source repository](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with YAML snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference live catalog documentation and requires glab, curl, jq, and a GitLab token for full validation and pipeline operations.]

## Skill Version(s):

1.91.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
