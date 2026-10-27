## Description:

Plan meals around servings, budget, exclusions and pantry ingredients, then merge quantities into a grocery list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users can plan practical meals around servings, meal slots, budgets, dietary exclusions, and pantry ingredients, then review cooking steps and a consolidated grocery list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meal suggestions may not reliably honor allergies or dietary exclusions.

Mitigation: Review every ingredient and confirm allergy and dietary exclusions before using a meal plan.

Risk: Budget targets or price estimates may not reflect current local prices.

Mitigation: Treat costs as estimates unless supported by actual price evidence, and date any estimate.

Risk: Meal details and dietary exclusions are saved as readable local JSON and processed by the configured model.

Mitigation: Avoid including sensitive details unless appropriate for the workspace and configured model.

## Reference(s):

- [Input contract](references/input.md)
- [MochiLab](https://mochilab.bz)
- [ClawHub release](https://clawhub.ai/hznetnewpower/skills/mochi-meal-planner)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Meal plans, cooking steps, and consolidated grocery lists in readable text or Markdown; saved plans as JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved plans are stored locally in the active agent workspace. Budget targets and unverified prices should be distinguished.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
