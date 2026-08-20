## Description:

Meta Calibrated Autonomy helps an agent decide when to act, delegate, defer, or ask for confirmation, with self-verification, reflection, and local learning hooks layered onto a distilled calibrated-autonomy workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders can use this skill as an autonomy gate for tasks with varying confidence and risk, routing work to act, delegate, defer, or ask before execution. It is intended to add review, reflection, and learned usage patterns around autonomous decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retain usage history, errors, notes, and preferences across sessions.

Mitigation: Require explicit user opt-in for learning, disclose where learned data is stored, and provide a deletion path for learned_patterns.json.

Risk: The skill text asks for learned experience to be written back into its own instructions.

Mitigation: Remove automatic SKILL.md writeback or require human review before any instruction changes are applied.

Risk: Autonomy decisions use fixed confidence and risk thresholds that may not fit every deployment.

Mitigation: Review thresholds before deployment and require human approval for high-stakes or unclear tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-calibrated-autonomy)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and Python script behavior]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local learned usage patterns when the learner script is used.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
