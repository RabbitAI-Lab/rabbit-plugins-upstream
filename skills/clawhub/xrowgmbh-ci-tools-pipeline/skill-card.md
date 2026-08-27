## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, repair, and validate GitLab CI/CD pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps workflows. It guides component selection from the CI Tools Components Catalog and helps keep validation, deployment, and release behavior aligned with existing project rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide edits to CI configuration and authenticated GitLab operations that affect branches, pipelines, registries, or deployments.

Mitigation: Review generated changes before pushing or running pipelines on important branches, and preserve existing gates for protected branches, registries, clusters, and production deployments.

Risk: Incorrect component inputs or weakened required checks could make a pipeline misleading or less protective.

Mitigation: Verify component inputs against the live CI Tools catalog, run GitLab CI linting, and avoid hiding required failures with skipped tests or allow_failure settings.

## Reference(s):

- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source Repository](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference GitLab tooling such as glab, curl, and jq, and may require GITLAB_TOKEN for authenticated validation workflows.]

## Skill Version(s):

1.84.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
