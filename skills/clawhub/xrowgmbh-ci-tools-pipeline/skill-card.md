## Description:

Helps developers build and maintain GitLab CI/CD pipelines using the CI Tools Components Catalog for applications, containers, charts, documentation, infrastructure, and GitOps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select CI Tools components, create or repair GitLab CI configuration, check component inputs, and validate delivery pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned component includes can change when upstream catalog branches move.

Mitigation: Review suggested includes and pin component versions where supply-chain stability matters.

Risk: Pushes, pipeline runs, and registry or deployment operations can change project state.

Mitigation: Approve these commands only when they match the intended workflow and existing project access rules.

## Reference(s):

- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/)
- [CI Tools project](https://gitlab.com/xrow-public/ci-tools)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline)

## Skill Output:

**Output Type(s):** [Configuration, Code, Shell commands, Guidance]

**Output Format:** [Markdown with GitLab CI YAML and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Component selections, input guidance, and pipeline validation steps.]

## Skill Version(s):

1.95.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
