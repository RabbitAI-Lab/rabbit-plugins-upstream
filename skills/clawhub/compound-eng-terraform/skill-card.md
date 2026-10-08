## Description:

Provides Terraform and OpenTofu guidance for configuration, modules, testing, state management, and HCL review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to write and review Terraform or OpenTofu modules, validate HCL, plan safe state changes, and choose appropriate infrastructure tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infrastructure changes can replace resources or incur costs.

Mitigation: Review plans for unintended replacements and require explicit authorization and budget controls before real infrastructure tests or applies.

Risk: State files or hardcoded credentials can expose sensitive information.

Mitigation: Keep state and credentials out of version control; use a protected remote backend and managed credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-terraform)
- [Native test patterns](references/native-test-patterns.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with HCL and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated plans and authorize tests that access real services.]

## Skill Version(s):

5.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
