## Description:

BigFood helps users identify ingredients from fridge or food photos, combine visible ingredients, and receive recipe, grocery, calorie, and meal-planning suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn fridge, pantry, or ingredient photos and text descriptions into practical recipe options, shopping suggestions, freshness notes, and calorie estimates. It is intended for Chinese and bilingual cooking conversations where the agent can analyze user-provided food images and respond with Markdown recipe guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad cooking and ingredient triggers may activate the skill during general Chinese food conversations.

Mitigation: Review activation behavior before deployment and confirm that broad food-related prompts are appropriate for the target agent experience.

Risk: Ingredient freshness, calorie values, and recipe suggestions are based on user-provided context and model interpretation rather than verified measurements.

Mitigation: Treat outputs as cooking guidance, ask for clarification when images or descriptions are ambiguous, and avoid presenting estimates as precise nutritional or safety determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/bigfood)
- [ClawHub publisher profile](https://clawhub.ai/user/kobenfang)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown recipe guidance with ingredient analysis, numbered options, shopping suggestions, and calorie estimates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on the host agent's vision capability for user-provided food images; does not define executable code, backend calls, credential handling, or cross-session persistence.]

## Skill Version(s):

0.1.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
