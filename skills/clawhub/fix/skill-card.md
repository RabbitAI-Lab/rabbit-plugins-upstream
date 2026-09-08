## Description:

A behavior-correction skill for agent workflows that responds to fix-style feedback, analyzes mistakes, updates relevant prompts or agent guidance, and resumes the interrupted work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to handle behavior-correction feedback, identify why an agent missed an expectation, improve the relevant behavioral guidance or hooks, and then complete the interrupted task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently change agent memory, behavioral rules, settings, hooks, and task flow beyond a narrowly scoped correction request.

Mitigation: Use it intentionally for explicit fix requests, keep changes local when possible, and review exact paths, diffs, saved memory, hook scripts, and settings changes before allowing persistence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text guidance with inline shell commands and configuration edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply persistent changes to agent memory, rules, settings, hooks, or skill files when permitted by the workflow.]

## Skill Version(s):

0.6.0 (source: server release metadata and CHANGELOG, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
