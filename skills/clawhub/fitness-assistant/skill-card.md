## Description:

Plan daily meals and workouts from a user's age and health profile, then schedule localized daily plans via OpenClaw automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[l1mufeng](https://clawhub.ai/user/l1mufeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to generate a one-day meal and workout plan from their profile, preferences, and health limitations. They can also ask it to schedule recurring daily fitness plans in a supported language and timezone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may collect or save sensitive health profile details such as age, body metrics, health limitations, dietary restrictions, routine, timezone, and language.

Mitigation: Confirm the user is comfortable storing these details and ask only for the profile fields needed to generate the plan.

Risk: Recurring daily automations may continue sending plans after a user's routine, timezone, or health situation changes.

Mitigation: Create schedules only after explicit confirmation and advise the user to review, update, or remove the automation when circumstances change.

Risk: Fitness and nutrition plans can be inappropriate for users with chronic conditions, pregnancy, medications affecting diet or training, minors, older adults, or injuries.

Mitigation: Keep guidance general, apply conservative adaptations and calorie floors, and recommend professional consultation for higher-risk profiles.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/L1MuFeng/fitness-assistant-skill/tree/main/skills/fitness-assistant)
- [ClawHub skill page](https://clawhub.ai/l1mufeng/skills/fitness-assistant)
- [Meal planning rules](references/meal-planning.md)
- [Workout planning rules](references/training.md)
- [User profile](references/profile.md)
- [Scheduling the daily plan](references/scheduling.md)
- [Output languages](references/languages.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown daily plan with optional shell or automation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include calorie and macro targets, meal sections, workout steps, hydration guidance, language localization, and scheduled delivery details.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
