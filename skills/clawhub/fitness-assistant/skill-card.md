## Description:

Plan daily meals and workouts from a user's age and health profile with customizable ingredients, then schedule localized plans via OpenClaw automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[l1mufeng](https://clawhub.ai/user/l1mufeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to generate personalized daily meal and workout plans from their profile, health constraints, dietary preferences, routine, and available equipment. They can also request recurring localized delivery after confirming the schedule, timezone, language, and channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store health, body, dietary, routine, timezone, and ingredient preference information in the user's agent profile or memory.

Mitigation: Tell users what profile data is being saved, ask only for needed fields, and update or remove saved preferences when the user requests a change.

Risk: The skill provides general lifestyle guidance that users could mistake for medical or nutritional advice.

Mitigation: Keep guidance conservative, avoid diagnosis or treatment claims, respect calorie floors, and recommend professional consultation for minors, pregnancy, chronic conditions, medication-related issues, or injuries.

Risk: A recurring daily automation may continue sending plans after the user's routine, timezone, delivery channel, or goals change.

Mitigation: Create or update schedules only after explicit confirmation, confirm the next run time, and remind users to review or remove scheduled jobs when plans should stop.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/l1mufeng/skills/fitness-assistant)
- [Server-Resolved GitHub Provenance](https://github.com/L1MuFeng/fitness-assistant-skill/tree/main/skills/fitness-assistant)
- [Profile Requirements](references/profile.md)
- [Meal Planning Rules](references/meal-planning.md)
- [Workout Planning Rules](references/training.md)
- [Scheduling the Daily Plan](references/scheduling.md)
- [Output Languages](references/languages.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown plan text with optional inline shell commands and automation configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include localized meal, macro, hydration, workout, and schedule confirmation details.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact frontmatter reports 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
