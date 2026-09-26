## Description:

AI KEY·从哪儿下手 helps Chinese-language users turn a vague goal into a measurable path with one confirmed bottleneck, costed route options, an if-then first step, and a prewritten failure criterion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when someone has a broad ambition but does not know where to start. It guides the conversation toward a decidable goal, measurable factors, one confirmed bottleneck, practical route options, and a concrete next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Goal context, assumptions, checkpoints, and lessons may be persisted in configured AI KEY memory or tracking paths.

Mitigation: Avoid using the skill for goals or business details that should not be stored, and review configured memory/tracking paths before use.

Risk: Weak or missing baseline data can produce a path that looks actionable but rests on unverified assumptions.

Mitigation: Require measured baselines where the skill asks for them, keep AI-inferred assumptions marked as unverified, and use the prewritten failure criterion to revisit the path.

Risk: The skill can route symptom, decision, allocation, or product questions to other AI KEY workflows instead of completing the current path workflow.

Mitigation: Check the opening classification and use the recommended adjacent workflow when the request is not actually a vague-goal path problem.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-path)
- [Skill definition](artifact/SKILL.md)
- [机制式库](artifact/references/机制式库.md)
- [理论底座](artifact/references/理论底座.md)
- [问题清单](artifact/references/问题清单.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown conversation output with tables, numbered options, an if-then action, and a reusable prompt template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include memory and tracking entries when configured by the user]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
