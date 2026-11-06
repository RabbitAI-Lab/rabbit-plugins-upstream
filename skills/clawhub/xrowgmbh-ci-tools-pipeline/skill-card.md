## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build or repair GitLab CI/CD pipelines, select CI Tools catalog components, validate component inputs, and plan delivery workflows for applications and infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab credentials or target settings could be used with the wrong project or host, or with broader access than needed.

Mitigation: Verify the target repository and GitLab host, and use credentials limited to the required work.

Risk: Linting sends pipeline configuration to GitLab, and pipeline changes may publish or deploy artifacts or run pipelines.

Mitigation: Review configuration before linting, remove sensitive values, and review generated changes and release or deployment rules before pushing or running pipelines.

Risk: Unreviewed component versions or changes to target-project files could affect release and deployment behavior.

Mitigation: Pin reviewed component versions, check release and deployment rules, and review target-project files and future component changes.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools GitLab Project](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Release Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration, Code, Shell commands, Guidance]

**Output Format:** [Markdown with YAML CI configuration examples, shell commands, and explanatory guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verify current component inputs and release behavior in the live catalog before use.]

## Skill Version(s):

1.130.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
