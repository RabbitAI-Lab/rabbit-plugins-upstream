## Description:

Helps developers build and maintain GitLab CI/CD pipelines using the CI Tools Components Catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or repair GitLab CI/CD configuration, select catalog components, validate their inputs, and plan delivery pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pipeline changes may alter deployment rules or publish artifacts.

Mitigation: Review .gitlab-ci.yml changes and existing deployment gates before merging.

Risk: Pushing branches or running merge-request pipelines may trigger external CI actions.

Mitigation: Confirm the intended branch and pipeline actions before executing them.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools Catalog](https://ci-tools.xrow.de/)
- [CI Tools component source](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Configuration instructions, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance and GitLab CI YAML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Component selection and validation guidance for GitLab CI/CD pipelines.]

## Skill Version(s):

1.105.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
