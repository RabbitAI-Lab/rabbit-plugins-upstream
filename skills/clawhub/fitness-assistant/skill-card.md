## Description:

Plan daily meals and workouts from a user's age and health profile with customizable ingredients, then schedule localized plans via OpenClaw automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[l1mufeng](https://clawhub.ai/user/l1mufeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to generate personalized one-day meal and workout plans from their profile, ingredients, goals, restrictions, and training preferences. When requested, it can schedule localized daily delivery through OpenClaw automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reuses sensitive health profile data for future plans and scheduled runs.

Mitigation: Review what profile data is saved, avoid storing sensitive medical details, and use one-time plans when persistence is not needed.

Risk: Scheduled automations can reuse saved profile data in recurring prompts.

Mitigation: Confirm timezone, delivery destination, and payload content before scheduling; prefer structured automations over CLI prompts for dynamic data.

Risk: Fitness and meal guidance may be inappropriate for minors, pregnancy, chronic conditions, or medication-sensitive diets.

Mitigation: Keep guidance general, apply documented calorie floors and conservative adaptations, and recommend professional consultation for those profiles.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/l1mufeng/skills/fitness-assistant)
- [Server-resolved source provenance](https://github.com/L1MuFeng/fitness-assistant-skill/tree/main/skills/fitness-assistant)
- [Dialogue scripts](references/dialogues.md)
- [Output languages](references/languages.md)
- [Meal planning rules](references/meal-planning.md)
- [Opening message and intake](references/opening.md)
- [User profile](references/profile.md)
- [Scheduling the daily plan](references/scheduling.md)
- [Training rules](references/training.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text daily plans with optional JSON automation payloads and bash command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include calorie and macro calculations, localized labels in one of 8 supported languages, and scheduling details when requested.]

## Skill Version(s):

0.1.3 (source: server release metadata; artifact frontmatter lists 0.1.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
