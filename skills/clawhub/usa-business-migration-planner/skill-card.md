## Description:

Helps maintainers, developers, and power users turn advanced hardware and virtualization configuration requests into practical plans, checklists, artifacts, analysis, code changes, or decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External maintainers, developers, and power users use this skill to convert advanced hardware and virtualization configuration needs into repeatable workflows and concrete deliverables. It is useful for producing local-hardware-friendly plans, checklists, implementation notes, or validation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The display name suggests USA business migration planning, while the artifact behavior focuses on advanced hardware and virtualization configuration.

Mitigation: Rename or rewrite the skill to match its behavior before broad release, and make the mismatch visible during review.

Risk: Broad implicit triggers may route unrelated requests to this skill.

Mitigation: Narrow or disable implicit triggers so invocation terms match the actual hardware and virtualization configuration use case.

Risk: Configuration guidance may be incorrect or unsafe for a user's specific hardware, firmware, operating system, or virtualization stack.

Mitigation: Require users to state their environment and constraints, keep assumptions explicit, and ask them to review proposed commands or configuration changes before execution.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/usa-business-migration-planner)
- [Publisher Profile](https://clawhub.ai/user/kyro-ma)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with optional checklists, code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only artifact; outputs should include assumptions, limits, validation notes, and follow-up risks when relevant.]

## Skill Version(s):

0.20260825.44155 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
