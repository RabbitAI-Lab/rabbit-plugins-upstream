## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines that rely on the CI Tools Components Catalog for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide edits to GitLab CI/CD configuration and workflows that may affect deployments, registries, or merge request pipelines.

Mitigation: Review suggested pipeline changes, pushes, MR pipeline runs, registry writes, and deployment-related changes before allowing them, especially when GITLAB_TOKEN is available.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source Repository](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with YAML snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference GitLab CLI, curl, jq, and GITLAB_TOKEN-backed validation workflows.]

## Skill Version(s):

1.81.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
