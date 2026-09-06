## Description:

Plan daily meals and workouts from a user's age and health profile with customizable ingredients, then schedule localized plans via OpenClaw automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[l1mufeng](https://clawhub.ai/user/l1mufeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to generate a personalized one-day meal plan and workout plan from profile, health, diet, training, language, and timezone details. The skill can also configure recurring daily delivery through OpenClaw automations when the user confirms schedule and delivery settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist sensitive fitness and health profile details for future scheduled runs without clear consent, retention limits, or deletion controls.

Mitigation: Before recurring delivery is enabled, ask what profile details will be saved, avoid sharing medical details you do not want retained, and request deletion or no-memory use when the environment supports it.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/L1MuFeng/fitness-assistant-skill/tree/main/skills/fitness-assistant)
- [ClawHub skill page](https://clawhub.ai/l1mufeng/skills/fitness-assistant)
- [Output languages](references/languages.md)
- [Meal planning rules](references/meal-planning.md)
- [Opening message and intake](references/opening.md)
- [User profile](references/profile.md)
- [Scheduling the daily plan](references/scheduling.md)
- [Workout planning rules](references/training.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured daily plan sections, inline shell commands, and optional automation configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include localized meal, hydration, workout, calorie, macro, and recurring delivery details.]

## Skill Version(s):

0.1.2 (source: server release metadata; artifact frontmatter reports 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
