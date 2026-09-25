## Description:

Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zlc000190](https://clawhub.ai/user/zlc000190)

### License/Terms of Use:


## Use Case:

Developers and coding agents use this skill to split independent failures, bugs, or subsystem tasks across parallel subagents and then review and integrate the returned work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parallel delegated work can conflict or drift when tasks share state or hidden dependencies.

Mitigation: Use the skill only for independent problem domains, give each agent a narrow scope, review returned summaries, check for conflicting edits, and run the full test suite.

Risk: Independent debugging or coding proposals may be incorrect in high-impact repositories.

Mitigation: Apply normal code review discipline before accepting changes, especially for security-sensitive or production-critical work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zlc000190/skills/dispatching-parallel-agents)

## Skill Output:

**Output Type(s):** [guidance, markdown, code]

**Output Format:** [Markdown guidance with prompt examples and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
