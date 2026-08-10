## Description:

Foolproof Kitchen generates quick, beginner-friendly daily meal plans and HTML recipe pages from body metrics, dietary goals, available ingredients, seasonings, and cooking tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mayabts](https://clawhub.ai/user/mayabts)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn personal body metrics, health considerations, food inventory, seasonings, and kitchen tools into a one-day breakfast, lunch, dinner, and snack plan. It is intended for kitchen beginners, busy people, solo diners, and users pursuing fat loss, maintenance, or muscle gain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for body metrics and health-related dietary details and may save them in a local HTML meal plan.

Mitigation: Use only with information the user is comfortable sharing, review the saved HTML before sharing it, and delete generated files when no longer needed.

Risk: Generated meal plans may be inappropriate for pregnancy, diabetes, hypertension, gout, allergies, or other medical conditions.

Mitigation: Treat the output as meal-planning assistance, not medical advice, and have users with medical or allergy concerns review plans with a qualified professional.

Risk: The HTML template loads Chart.js from a third-party CDN.

Mitigation: Prefer a release that bundles chart assets locally or review network access before opening generated HTML in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mayabts/skills/foolproof-kitchen)
- [Chinese Dietary Guidelines and Nutrition Reference](references/dietary_guidelines.md)
- [Quick Recipe Database](references/quick_recipe_database.md)
- [Recipe HTML Template](assets/recipe_template.html)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [HTML file with concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a local visual recipe page with nutrition breakdown, meal cards, shopping reminders, and step-by-step cooking instructions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
