## Description:

Builds and maintains GitLab CI/CD pipelines with CI Tools Components Catalog guidance for creating or fixing .gitlab-ci.yml files, choosing components, validating inputs, and designing delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, update, and validate GitLab CI/CD pipelines that use the CI Tools Components Catalog. It helps select catalog components, prepare .gitlab-ci.yml configuration, and plan validation for application, container, Helm, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pipeline changes can affect registry, cluster, deployment, or GitOps behavior.

Mitigation: Use a least-privilege GitLab token and review generated pipeline changes before pushing, especially when deployment components are involved.

Risk: Stale or incorrect CI Tools component inputs can break pipeline validation.

Mitigation: Verify component inputs against the live CI Tools Components Index and run glab ci lint .gitlab-ci.yml before pushing.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with YAML snippets and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose .gitlab-ci.yml component includes and validation commands; requires glab, curl, jq, and a least-privilege GITLAB_TOKEN when accessing GitLab.]

## Skill Version(s):

1.82.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
