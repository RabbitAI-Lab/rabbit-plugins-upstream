## Description:

AI Life Coach guides structured Socratic conversations for self-awareness, goal clarification, emotional support, and action planning, with crisis-first and under-18 safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill for structured life-coaching conversations that help users reflect on personal direction, clarify goals, and identify next actions. It is not a substitute for therapy, medical care, emergency support, legal advice, or financial advice.

### Deployment Geography for Use:

Global; crisis-support resources should be localized for users outside mainland China.

## Known Risks and Mitigations:

Risk: The skill may handle crisis-adjacent emotional conversations.

Mitigation: Review crisis handling before deployment and ensure emergency guidance is localized for the user population.

Risk: The skill can persist sensitive coaching notes to a local memory file with user consent.

Mitigation: Treat local memory as private data, obtain explicit consent before writing, and disable memory during crisis or under-18 conversations.

Risk: The included crisis numbers are specific to mainland China.

Mitigation: Provide local crisis resources for deployments serving users in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [Publisher profile](https://clawhub.ai/user/luhayden-blip)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append a short local session summary with explicit user consent; no network upload is described.]

## Skill Version(s):

2.0.9 (source: evidence release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
