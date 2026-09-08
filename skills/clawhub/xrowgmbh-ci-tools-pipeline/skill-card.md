## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines built from the CI Tools Components Catalog for applications, containers, Helm charts, packages, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated CI guidance may bypass normal validation or weaken required pipeline checks.

Mitigation: Require GitLab CI linting and review before merging generated pipeline changes, and approve any validation skip explicitly.

Risk: Pipeline includes may execute mutable external component code from @main.

Mitigation: Prefer pinned component versions or reviewed protected tags for repositories with sensitive code, credentials, releases, deployments, or privileged runners.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference glab, curl, jq, and GITLAB_TOKEN for GitLab CI validation workflows.]

## Skill Version(s):

1.90.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
