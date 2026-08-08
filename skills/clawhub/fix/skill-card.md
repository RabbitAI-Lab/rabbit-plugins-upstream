## Description:

A behavior-correction skill that responds to fix-oriented feedback by analyzing an agent mistake, improving the relevant prompt, rule, memory, hook, or procedure, and then resuming the original task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill when a user reports that an agent made a process or behavior mistake. It guides root-cause analysis, prevention-medium updates, verification, and completion of the user's original work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent, high-impact changes to agent behavior assets such as rules, settings, hooks, memories, task state, plugins, and project knowledge stores.

Mitigation: Use explicit /fix or fix: invocation, review proposed persistent changes before applying them, and keep shared-repository changes under normal code review.

Risk: Broadly worded correction requests can trigger remediation work that changes more than the user intended.

Mitigation: Clarify ambiguous fix targets before execution and prefer plan-only review for complex or cross-file changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix)
- [Fix skill source](artifact/SKILL.md)
- [Step 2 prompt improvement guidance](artifact/step2-improvement.md)
- [Step 3 resume guidance](artifact/step3-resume.md)
- [Step 4 wrap-up guidance](artifact/step4-wrapup.md)
- [Behavior discipline guidance](artifact/behavior-discipline.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional shell commands, code or configuration edits, and saved plan artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persistent changes to prompts, rules, hooks, memories, task state, plugins, project knowledge stores, or commits when the workflow calls for them.]

## Skill Version(s):

0.3.10 (source: server release evidence; changelog released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
