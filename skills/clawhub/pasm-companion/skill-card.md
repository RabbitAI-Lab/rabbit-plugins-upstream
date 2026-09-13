## Description:

PASM Elderly Companion Agent helps developers build an offline elderly companion agent that stores key facts, prompts scheduled medication reminders, detects crisis phrases, and returns escalation context for a human notifier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate an offline elderly companion agent that can recall essential user facts, provide scheduled medication prompts, and package crisis context for a designated human contact. It is intended for companion and record-keeping workflows, not diagnosis, treatment decisions, emergency dispatch, or medical-device use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External package installation can change over time and may introduce unreviewed behavior.

Mitigation: Review pasm-agents and pasm-skills before installing, and pin package versions or source commits where possible.

Risk: The companion may store sensitive medication, allergy, family, and emergency-contact data.

Mitigation: Run it under a restricted user or account and apply appropriate local data-access controls before using real personal or health-related data.

Risk: Crisis detection and escalation context could be mistaken for medical advice or emergency-service automation.

Mitigation: Use crisis output only as an aid for contacting a human and keep medical, emergency, and medication decisions with qualified people or services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-companion)
- [PASM agents project homepage](https://github.com/arronJack/pasm-agents)
- [PASM skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)
- [Alternative source install URL](https://gitee.com/arronzheng/pasm-agents)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and git; may handle sensitive medication, allergy, family, and emergency-contact data when implemented.]

## Skill Version(s):

0.4.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
