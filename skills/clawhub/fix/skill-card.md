## Description:

User behavior correction skill that responds to fix-prefixed feedback by analyzing an agent mistake, improving the relevant persistent prompt or guard, and resuming the current task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to handle behavior-correction feedback by forcing root-cause analysis, recurrence prevention, guarded prompt or rule updates, and completion of the original work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad persistent authority over agent rules, memories, hooks, settings, and project knowledge.

Mitigation: Use explicit fix-prefixed invocations, prefer --plan and --local where possible, and review proposed persistent changes before allowing them to proceed.

Risk: Broad behavior-correction triggers can affect workflows when feedback is ambiguous.

Mitigation: Require clarification for ambiguous targets and review the planned correction before edits, commands, or configuration changes are applied.

Risk: Self-modifying behavior-correction flows can encode incorrect or misleading guidance into future agent behavior.

Mitigation: Review diffs, scan the skill before deployment, and run relevant verification or tests for the behavior being corrected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix)
- [Publisher profile](https://clawhub.ai/user/drumrobot)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional code, shell command, configuration, and file-edit outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persistent prompt, rule, hook, memory, settings, or project-knowledge changes when the fix flow calls for them.]

## Skill Version(s):

0.3.12 (source: release evidence and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
