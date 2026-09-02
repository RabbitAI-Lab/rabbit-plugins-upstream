## Description:

Builds and maintains GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or fix .gitlab-ci.yml files, choose CI Tools components, validate component inputs, and design delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed pipeline changes may trigger GitLab pushes, merge request pipeline runs, registry writes, or deployment-related behavior.

Mitigation: Review proposed GitLab commands and configuration changes before allowing them, especially in production repositories.

Risk: Incorrect component selection or inputs can weaken required checks or alter protected branch behavior.

Mitigation: Verify component inputs against the live CI Tools catalog and lint the resulting .gitlab-ci.yml before pushing.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools Components Index](https://ci-tools.xrow.de/Components/)
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with YAML snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose GitLab CI configuration changes and validation commands using glab, curl, jq, and GITLAB_TOKEN when available.]

## Skill Version(s):

1.84.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
