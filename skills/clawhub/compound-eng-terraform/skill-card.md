## Description:

Guides Terraform and OpenTofu configuration, modules, testing, state management, and HCL review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to write, review, test, and refactor Terraform or OpenTofu configurations while preserving infrastructure state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying or replacing resources can alter infrastructure, state, and costs.

Mitigation: Review the plan and obtain authorization before running apply, replace, or real-service tests.

Risk: Force-unlocking or running tests against live services can disrupt shared infrastructure or expose credentials.

Mitigation: Confirm no active operation before force-unlocking; distinguish mocked tests from live tests and review credentials and effects first.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-terraform)
- [Native test patterns](references/native-test-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Text and Markdown with HCL and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggested changes and commands require review before execution.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
