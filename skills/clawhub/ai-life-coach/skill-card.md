## Description:

AI人生教练 is a Socratic life-coaching agent for self-awareness, goal clarity, and action planning, with crisis-first routing, under-18 safeguards, anti-sycophancy behavior, and local-only memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill for structured life-coaching conversations around emotional difficulty, personal direction, motivation, relationships, self-awareness, goals, and concrete next steps. It supports reflective dialogue and action planning while routing crisis signals to safety resources and limiting depth for minors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save sensitive local notes about mood, relationships, family issues, patterns, and commitments.

Mitigation: Use a non-identifying alias, decline memory when needed, and protect or delete the local memory directory if the device is shared, managed, or backed up.

Risk: The skill may activate on broad emotional language and handle mental-health-adjacent conversations.

Mitigation: Review conversations carefully before use in sensitive settings, keep crisis routing active, and rely on professional or local emergency resources for urgent safety concerns.

Risk: The built-in crisis resources are China-focused and may not fit users in other countries.

Mitigation: Users outside China should use local emergency services and crisis resources instead of relying only on the listed hotlines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [FAQ](FAQ.md)
- [Coaching ethics](references/ethics.md)
- [Session memory](references/memory.md)
- [Parent-child module](references/parent_child.md)
- [Relationship module](references/relationship.md)
- [Questioning tools](references/tools.md)
- [Conversation workflow](references/workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and Markdown summaries or action plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local memory notes after user consent; full action blueprints are generated only after enough conversation material is available and the user agrees.]

## Skill Version(s):

2.4.3 (source: frontmatter, manifest, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
