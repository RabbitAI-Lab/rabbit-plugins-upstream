## Description:

pasm-companion helps developers build offline elderly companion agents with deterministic memory for medication, allergy, family, and self facts, medication reminders, crisis detection, and escalation context for human notification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and care-technology teams use this skill to add an offline elderly companion agent that remembers critical personal facts, prompts scheduled medication, and returns crisis escalation context for a human-managed notification channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store sensitive elder-care, medication, allergy, family, and emergency-contact information locally.

Mitigation: Run it in an isolated environment, review local persistence behavior before use, and avoid entering unnecessary personal data.

Risk: Installation examples reference mutable external packages or repositories.

Mitigation: Review pasm-agents and pasm-skills before installing, and prefer a pinned package version or reviewed commit.

Risk: The skill detects crisis language and returns escalation context, but it is not a medical device and does not replace emergency services.

Mitigation: Keep medical decisions, emergency calls, and notifications under human or caller-owned systems, and present escalation output as advisory context only.

## Reference(s):

- [pasm-agents repository](https://github.com/arronJack/pasm-agents)
- [pasm-skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)
- [pasm-agents Gitee source install](https://gitee.com/arronzheng/pasm-agents)
- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-companion)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes local persistence, offline operation, crisis escalation context, and caller-owned notification integration.]

## Skill Version(s):

0.4.9 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
