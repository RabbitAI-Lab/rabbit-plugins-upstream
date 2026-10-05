## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI/CD engineers use this skill to create, repair, and validate GitLab pipelines using CI Tools components for builds, tests, packaging, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab project context and token-backed actions, including branch pushes and MR pipeline runs, may expose project data or trigger unintended changes.

Mitigation: Confirm GitLab token access and review proposed commands and changes before allowing pushes or pipeline runs.

Risk: Pipeline changes could weaken required checks or enable unintended production deployment.

Mitigation: Preserve required validation and existing deployment gates; review production changes and lint the pipeline before pushing.

## Reference(s):

- [CI Tools Pipeline on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools component repository](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with GitLab CI YAML and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.98.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
