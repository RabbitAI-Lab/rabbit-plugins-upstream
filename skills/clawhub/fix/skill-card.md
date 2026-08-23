## Description:

Fix is a user behavior correction skill that responds to fix-style feedback, analyzes the mistake, improves the relevant prompt or agent rule, memory, or hook to prevent recurrence, and then fixes the current issue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to turn user feedback about agent mistakes into a structured root-cause analysis, durable behavior improvement, verification step, and resumed task work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist changes to agent rules, hooks, memories, settings, plans, and project knowledge.

Mitigation: Use explicit fix: or /fix invocations, prefer --local when the issue is workspace-specific, and review every proposed persistent change before approval.

Risk: Broad behavior-feedback triggers can start a correction workflow that inspects global agent records or configuration.

Mitigation: Confirm the target and scope before execution, and require source-backed root-cause evidence before accepting a behavior change.

Risk: The ambiguity guard can add context when prompts match fix, ambiguous-option, or user-claim patterns.

Mitigation: Keep false-positive tests for new detection criteria and review hook output before treating it as task authority.

## Reference(s):

- [Fix Skill Definition](artifact/SKILL.md)
- [Step 2 Improvement](artifact/step2-improvement.md)
- [Step 3 Resume](artifact/step3-resume.md)
- [Step 4 Wrapup](artifact/step4-wrapup.md)
- [Behavior Discipline](artifact/behavior-discipline.md)
- [Fix and Ambiguity Guard Hook](artifact/resources/fix-and-ambiguity-guard.sh)
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/fix)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with command snippets, file-change plans, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply persistent changes to agent rules, memories, hooks, settings, plans, and project knowledge.]

## Skill Version(s):

0.4.0 (source: server release metadata and changelog, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
