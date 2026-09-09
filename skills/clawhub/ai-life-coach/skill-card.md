## Description:

AI Life Coach is a prompt-only coaching skill that uses Socratic dialogue to help users explore self-awareness, clarify goals, and form concrete action plans while routing crisis signals to support resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill for non-clinical life coaching conversations around emotional difficulty, self-awareness, direction setting, relationship or school stress, and practical next steps. It is not a substitute for professional mental-health, medical, legal, financial, or emergency support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad emotional or distress language.

Mitigation: Review trigger behavior before deployment and keep crisis routing ahead of normal coaching responses.

Risk: The skill can persist sensitive notes about mood, patterns, and goals locally with weak controls.

Mitigation: Use only on trusted devices, minimize stored notes, obtain user consent before writing memory, and avoid shared-device use.

Risk: Users may treat life-coaching output as professional or emergency support.

Mitigation: Keep the non-clinical disclaimer visible and route ongoing distress, self-harm signals, or emergencies to professional and crisis resources.

Risk: The hosted web version is a separate remote service with different privacy implications.

Mitigation: Review the hosted service separately before recommending or using it for sensitive conversations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [Publisher Profile](https://clawhub.ai/user/luhayden-blip)
- [Hosted Web Version](https://coach.gzccadinspect.top)
- [SKILL.md](artifact/SKILL.md)
- [FAQ.md](artifact/FAQ.md)
- [Ethics Reference](artifact/references/ethics.md)
- [Memory Reference](artifact/references/memory.md)
- [Workflow Reference](artifact/references/workflow.md)
- [Tools Reference](artifact/references/tools.md)
- [Relationship Reference](artifact/references/relationship.md)
- [Parent-Child Reference](artifact/references/parent_child.md)
- [School Mental Reference](artifact/references/school_mental.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text and Markdown coaching summaries or action blueprints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write local memory notes when the host agent grants the requested file tools.]

## Skill Version(s):

2.5.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
