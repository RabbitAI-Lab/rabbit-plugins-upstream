## Description:

AI人生教练 is a dialogue-based life coaching skill that helps users explore self-awareness, goal clarity, and concrete next steps while applying crisis-first routing, under-18 protections, anti-sycophancy guidance, and local-only memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill for structured life-coaching conversations around emotional difficulty, motivation, life direction, relationships, school stress, self-awareness, goal setting, and action planning. It is not a clinical mental-health service and includes crisis routing, minor-specific safeguards, and local memory privacy constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may save sensitive coaching notes locally under a user-chosen alias.

Mitigation: Use explicit invocation, avoid shared or untrusted local accounts, keep notes minimal, and honor requests not to remember a session.

Risk: The skill may activate in mental-health-adjacent conversations and is not a clinical service.

Mitigation: Review triggers and responses before deployment, preserve the coach-not-therapist boundary, and route crisis signals to human or emergency support.

Risk: The built-in crisis hotline numbers are China-specific and may not be reliable for global users.

Mitigation: Localize crisis resources for the intended deployment region and make emergency escalation guidance available before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [Web version](https://coach.gzccadinspect.top)
- [FAQ](FAQ.md)
- [Coaching ethics](references/ethics.md)
- [Memory and privacy](references/memory.md)
- [Parent-child relationship module](references/parent_child.md)
- [Relationship module](references/relationship.md)
- [School mental-health module](references/school_mental.md)
- [Questioning tools and signal matching](references/tools.md)
- [Workflow and output specification](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Conversational text with optional Markdown summaries and personal growth action blueprints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write concise local memory notes under a user-chosen alias; crisis interactions should avoid memory reads and writes.]

## Skill Version(s):

2.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
