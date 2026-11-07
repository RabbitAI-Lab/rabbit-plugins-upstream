## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to select CI Tools catalog components, create or repair GitLab CI/CD configuration, and plan validation and delivery workflows for their repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GitLab token with broad permissions could expose more project access than pipeline work requires.

Mitigation: Use a project-scoped GitLab token.

Risk: Generated pipeline changes can affect validation, registries, clusters, or deployment actions.

Mitigation: Review generated changes before pushing or running them, and ensure deployment actions follow the project's existing permissions and gates.

Risk: External CI components can change or include code outside the supplied project files reviewed by the scanners.

Mitigation: Pin external components to reviewed immutable revisions where practical.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source Project](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with GitLab CI YAML snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapted to the repository layout, pipeline needs, and selected component inputs.]

## Skill Version(s):

1.130.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
