## Description:

Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to create, fix, and validate GitLab CI/CD pipelines that rely on the CI Tools Components Catalog. It supports component selection, input validation, and pipeline design for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable @main CI component references can change future pipeline behavior without normal project review.

Mitigation: Replace @main references with reviewed commit SHAs or protected release tags before adopting generated pipeline changes.

Risk: Generated pipeline changes may affect release, registry, GitOps, or deployment jobs.

Mitigation: Review changes in sensitive repositories, use least-privilege GitLab tokens, and confirm the GitLab and catalog hosts are approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)
- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source Repository](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose changes to .gitlab-ci.yml and related pipeline configuration.]

## Skill Version(s):

1.91.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
