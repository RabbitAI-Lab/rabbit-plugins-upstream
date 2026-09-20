## Description:

pasm-companion helps developers build offline elderly-care companion agents that retain key facts, provide medication reminders, detect crisis phrases, and return escalation context for human notification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integrators use this skill to add offline companion behavior for elder-care applications, including durable key-fact recall, medication-time checks, crisis phrase detection, and escalation context for a human notifier. It is not a medical device and does not replace medical, emergency, or medication decisions by qualified people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive elder-care details such as medications, allergies, family contacts, mood, crisis history, and long-lived memory snapshots.

Mitigation: Before using it with real people, decide where saved state lives, who can read snapshots, and how records are deleted, redacted, or retained.

Risk: Escalation snapshots and notifier integrations may expose more personal context than an emergency contact needs.

Mitigation: Send only minimal emergency details to notifier integrations unless the user or care workflow explicitly requires broader context.

Risk: The skill is documented as not being a medical device and does not make clinical, emergency, or medication decisions.

Mitigation: Keep human escalation and qualified medical judgment in the workflow for diagnosis, treatment, medication changes, and emergency response.

## Reference(s):

- [Artifact SKILL.md](artifact/SKILL.md)
- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-companion)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python examples, shell commands, configuration notes, and JSON-like escalation structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The described agent can return companion text, medication reminder lists, crisis labels, and escalation context snapshots for a caller-managed notifier.]

## Skill Version(s):

0.4.11 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
