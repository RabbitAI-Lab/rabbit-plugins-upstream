## Description:

Meta Agent Eval Harness helps developers evaluate agent behavior with regression checks, self-verification, reflection, adversarial validation, and a local learner loop for usage outcomes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to define agent evaluation cases, run pass-rate and regression checks, and add review loops that record usage outcomes for later improvement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags local cross-session memory about usage, errors, notes, and preferences.

Mitigation: Review learned_patterns.json regularly and avoid recording sensitive user content in notes or preferences.

Risk: The skill describes self-modifying behavior that can change instructions over time without clear retention or deletion controls.

Mitigation: Disable or remove the learner step before deployment unless change control, retention, and deletion expectations are defined.

Risk: The artifact notes that distilled behavior may not cover all implicit knowledge from the teacher skill.

Mitigation: Verify critical evaluation decisions against the original teacher skill or a trusted benchmark before relying on results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qq435912743/skills/meta-agent-eval-harness)
- [Distillation Report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and code references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May record local usage outcomes and notes through the bundled learner script.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
