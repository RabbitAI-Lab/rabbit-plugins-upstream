## Description:

AI人生教练 is a bilingual life-coaching prompt skill that uses Socratic conversation to support self-awareness, goal clarity, and concrete action planning while applying crisis-first, under-18, anti-sycophancy, and local-memory safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luhayden-blip](https://clawhub.ai/user/luhayden-blip)

### License/Terms of Use:

MIT-0

## Use Case:

External users invoke this skill when they want a coaching-style conversation for emotional stuckness, life direction, goal clarification, parent-child relationship reflection, and next-step planning. The skill is not presented as therapy or decision-making on the user's behalf.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate on broad emotional phrases and may enter coaching mode when a user only intended a narrower task.

Mitigation: Use explicit invocations where possible and review the trigger scope before enabling it in shared or task-heavy environments.

Risk: The skill can store sensitive coaching history in local Markdown memory files.

Mitigation: Avoid use on shared machines unless local memory files are acceptable, and rely on the skill's consent and opt-out behavior for note creation.

Risk: The crisis resources described by the skill are China-specific.

Mitigation: Do not rely on those hotline numbers outside China; provide locally appropriate crisis resources for the deployment region.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luhayden-blip/skills/ai-life-coach)
- [README](README.md)
- [FAQ](FAQ.md)
- [Ethics reference](references/ethics.md)
- [Memory reference](references/memory.md)
- [Parent-child reference](references/parent_child.md)
- [Tools reference](references/tools.md)
- [Workflow reference](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text with optional Markdown summaries, action plans, and local coaching notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local Markdown memory notes with consent; no network output is described in the artifact.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
