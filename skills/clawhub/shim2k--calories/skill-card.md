## Description:

Track calories and macros conversationally. Auto-adapts to your goals and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shim2k](https://clawhub.ai/user/shim2k)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to log meals, estimate calories and macros from photos or text, adapt tracking style to goals such as weight loss, maintenance, or muscle gain, and maintain a reusable local food library. It is educational support only and is not medical or nutritional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores calorie goals, eating patterns, preferences, label data, recipes, and restaurant favorites in ~/calories/memory.md without clear consent or deletion controls.

Mitigation: Tell users before retaining food or goal history, offer an opt-out path, and provide a clear way to delete ~/calories/memory.md.

Risk: Calorie tracking can be medically or emotionally unsafe for users with contraindications such as eating disorder history, pregnancy or breastfeeding, diabetes without clinician supervision, being under 18, or BMI below 18.5.

Mitigation: Screen for contraindications before tracking, decline calorie tracking when contraindicated, and direct users to qualified medical or support resources.

Risk: Photo and text calorie estimates are approximate and can mislead users if presented as exact measurements.

Mitigation: Use ranges, communicate uncertainty plainly, focus on weekly trends, and avoid encouraging exact weighing or precision-focused behavior.

## Reference(s):

- [Calorie Tracker on ClawHub](https://clawhub.ai/shim2k/skills/calories)
- [Calorie Estimation Framework](artifact/estimation.md)
- [Calorie Tracking Goals](artifact/goals.md)
- [Calorie Tracking Safety](artifact/safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Conversational Markdown with approximate calorie and macro estimates, optional ranges, brief clarifying questions, and local Markdown memory entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update ~/calories/memory.md with calorie goals, eating patterns, preferences, label data, recipes, and restaurant favorites.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
