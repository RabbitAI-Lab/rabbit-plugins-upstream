## Description:

AI人生教练 is a Socratic life-coaching skill that helps users reflect on their current state, clarify goals, and form concrete next steps while applying crisis-first and under-18 safety boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT

## Use Case:

External users invoke this skill for coaching-style conversations about confusion, motivation, life direction, self-awareness, goal clarity, and action planning. It is intended for reflective coaching support, not diagnosis, treatment, or replacement of licensed mental-health care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate on broad emotional or distress language.

Mitigation: Review trigger behavior before deployment and route urgent safety concerns to appropriate emergency or professional resources instead of treating coaching as clinical care.

Risk: The skill may keep sensitive wellbeing notes on the local machine.

Mitigation: Use a non-identifying code name, avoid shared devices for sensitive conversations, and decline memory when no local record should be kept.

Risk: The listed hotline resources are China-specific.

Mitigation: Users outside China should rely on local emergency services, crisis lines, or licensed professional support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [README](README.md)
- [FAQ](FAQ.md)
- [Coaching ethics](references/ethics.md)
- [Question methods and signal matching](references/tools.md)
- [Memory and session self-review](references/memory.md)
- [Conversation workflow and output norms](references/workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Conversational text or Markdown, with optional short local memory notes when the user consents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may store sensitive wellbeing notes locally; it does not claim to provide clinical diagnosis or therapy.]

## Skill Version(s):

2.1.3 (source: frontmatter, artifact manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
