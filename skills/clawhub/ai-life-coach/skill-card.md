## Description:

AI人生教练 is a Socratic life-coaching skill for self-awareness, goal clarity, and action planning, with crisis-first routing, under-18 safeguards, anti-sycophancy behavior, and local-only memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for reflective coaching conversations about life direction, emotional difficulty, relationships, school issues, career questions, and concrete next steps. The agent provides supportive dialogue and planning guidance rather than clinical diagnosis, medical care, legal advice, or irreversible decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive coaching notes are stored in local files keyed by a user-chosen code name, which can expose or alter the wrong records on shared systems.

Mitigation: Use non-identifying, hard-to-guess code names; avoid shared devices for sensitive sessions; validate storage identifiers; and provide a clear delete or reset path before treating the release as low risk.

Risk: Users may assume the website and local skill share the same privacy boundary.

Mitigation: Explain that local skill memory and website memory are separate, and do not imply that one environment inherits the other's privacy or storage behavior.

## Reference(s):

- [AI Life Coach ClawHub Page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [AI Life Coach Website](https://www.ailifecoach.cn)
- [FAQ](FAQ.md)
- [Coach Ethics](references/ethics.md)
- [Memory Handling](references/memory.md)
- [Questioning Tools and Signal Matching](references/tools.md)
- [Conversation Workflow](references/workflow.md)
- [Relationship Module](references/relationship.md)
- [Parent-Child Module](references/parent_child.md)
- [School Mental Health Module](references/school_mental.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Conversational text and Markdown summaries, with optional local Markdown memory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write local Markdown memory records when the user consents and the runtime permits file tools.]

## Skill Version(s):

2.7.0 (source: frontmatter, manifest, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
