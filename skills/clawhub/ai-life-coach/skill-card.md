## Description:

A conversational life coach that helps people reflect on their situation, clarify goals, and plan small next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking support with self-reflection, everyday emotional difficulties, relationships, or life planning use this skill for guided conversation and actionable next steps. It is not a substitute for mental health care or crisis support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive coaching notes may be written outside their intended location when a user alias contains path characters.

Mitigation: Use only a simple random alias without slashes or dots; do not install until alias validation and path containment are addressed if this risk is unacceptable.

Risk: Local emotional records may be accessible to others on shared accounts or devices.

Mitigation: Avoid use on shared accounts or devices; review local storage and request deletion or export controls before relying on persistent memory.

Risk: Broad distress-related triggers and China-specific crisis contacts may not fit every user or region.

Mitigation: Start coaching only with explicit user consent and provide locally appropriate crisis resources when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [Coaching workflow and outputs](artifact/references/workflow.md)
- [Memory and privacy practices](artifact/references/memory.md)
- [Coaching ethics](artifact/references/ethics.md)
- [Coaching tools and safety routing](artifact/references/tools.md)
- [Relationship support](artifact/references/relationship.md)
- [Parent–child support](artifact/references/parent_child.md)
- [School and mental wellbeing support](artifact/references/school_mental.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown files]

**Output Format:** [Conversational text with optional local Markdown notes and a copyable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local notes are optional and require user consent before first write.]

## Skill Version(s):

2.8.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
