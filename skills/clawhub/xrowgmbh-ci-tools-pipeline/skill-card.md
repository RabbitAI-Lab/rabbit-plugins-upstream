## Description:

Helps developers build and maintain GitLab CI/CD pipelines using the CI Tools Components Catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI/CD engineers use this skill to create, troubleshoot, and validate GitLab pipelines for applications, containers, Helm charts, documentation, infrastructure, and GitOps delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect pipeline changes can break required checks or trigger unintended deployment and registry writes.

Mitigation: Review generated changes and lint the pipeline before pushing; keep deployment and registry writes gated by existing project rules.

Risk: A GitLab access token with broad permissions can increase the impact of unintended CI actions.

Mitigation: Keep GITLAB_TOKEN least-privileged and scrutinize jobs that write to registries, clusters, or deployment environments.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools component repository](https://gitlab.com/xrow-public/ci-tools)
- [CI Tools Pipeline on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [GitLab CI YAML and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review proposed pipeline changes and validate component inputs before pushing.]

## Skill Version(s):

1.110.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
