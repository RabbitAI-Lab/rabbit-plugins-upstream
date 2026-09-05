## Description:

Build and maintain GitLab CI/CD pipelines with CI Tools catalog components for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to create, repair, and validate GitLab CI/CD pipelines using xrow CI Tools components while keeping deployment and registry writes gated by project rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated GitLab CI configuration could change build, deployment, registry, or cluster behavior if accepted without review.

Mitigation: Review any generated .gitlab-ci.yml changes before pushing and keep registry, cluster, and deployment writes gated by existing project rules.

Risk: A broadly scoped GITLAB_TOKEN could grant more repository or pipeline access than the workflow needs.

Mitigation: Use an appropriately scoped GITLAB_TOKEN and avoid exposing it in logs, generated configuration, or merge request text.

Risk: Mutable CI component references such as @main can reduce pipeline reproducibility.

Mitigation: Pin CI component versions when reproducibility matters.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab CI component includes, .gitlab-ci.yml edits, validation commands, and merge request checklist guidance.]

## Skill Version(s):

1.84.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
