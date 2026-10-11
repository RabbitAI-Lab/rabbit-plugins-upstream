## Description:

Provides Terraform and OpenTofu guidance for configuration, modules, testing, state management, and HCL review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to write and review Terraform or OpenTofu configurations, modules, tests, and state migrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying, importing, unlocking, or refreshing state can change real cloud resources or state and incur costs.

Mitigation: Require authorization, appropriate credentials, a cost boundary, and a cleanup plan before executing these operations.

Risk: Plan tests can read live data sources, and real infrastructure tests can create billable resources.

Mitigation: Inspect providers and external effects; prefer verified local or mocked tests, and run real-service tests only within the approved cost and cleanup boundary.

## Reference(s):

- [Native test patterns](references/native-test-patterns.md)
- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-terraform)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with HCL and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

5.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
