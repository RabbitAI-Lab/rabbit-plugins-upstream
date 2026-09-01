## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines that rely on the CI Tools Components Catalog for application, container, Helm, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Validation commands, git pushes, and pipeline runs can perform real GitLab remote actions, publish commits, or consume CI resources.

Mitigation: Confirm the target GitLab project and branch before execution, use a GitLab token with only the required permissions, and run pipeline actions deliberately.

Risk: Incorrect component choices or input names can produce broken or misleading GitLab CI/CD configuration.

Mitigation: Check the live CI Tools catalog before editing and lint the resulting pipeline with glab ci lint before pushing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools source](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, curl, jq, and a GitLab token for validation or remote pipeline actions.]

## Skill Version(s):

1.84.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
