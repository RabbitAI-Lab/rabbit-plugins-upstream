## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines that use CI Tools catalog components for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pipeline changes can affect deployment, registry, or cluster-writing jobs.

Mitigation: Review generated .gitlab-ci.yml changes before pushing and confirm deployment or registry-writing jobs remain gated by existing project rules.

Risk: GitLab token use can expose broader project or CI permissions than intended.

Mitigation: Use a least-privilege GITLAB_TOKEN and avoid placing token values in generated files, commands, or logs.

Risk: CI Tools component inputs may differ from assumptions if the live catalog changes.

Mitigation: Verify component input names against the live catalog and run glab ci lint before merge.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with YAML and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include .gitlab-ci.yml edits, component include snippets, validation commands, and review checklists.]

## Skill Version(s):

1.79.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
