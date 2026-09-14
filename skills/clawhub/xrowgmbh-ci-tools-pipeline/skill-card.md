## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to create, repair, and validate GitLab CI/CD pipelines that use CI Tools catalog components for applications, containers, Helm charts, packages, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable third-party CI component references can execute changed pipeline code after a release.

Mitigation: Prefer pinned component versions or reviewed immutable refs instead of @main before merging generated pipeline changes.

Risk: CI variables, registry writes, deployments, or runner permissions may expose production secrets to component jobs.

Mitigation: Scope GitLab variables, deployment permissions, registry access, and runner privileges so third-party component jobs cannot unexpectedly reach production secrets.

Risk: Generated or revised CI pipelines may be incorrect for the target repository.

Mitigation: Review generated pipelines, validate component inputs against the live CI Tools catalog, and run GitLab CI lint before merging.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components](https://ci-tools.xrow.de/Components/)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)
- [Publisher Profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with YAML, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, curl, jq, and the GITLAB_TOKEN environment variable for live GitLab and catalog validation workflows.]

## Skill Version(s):

1.91.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
