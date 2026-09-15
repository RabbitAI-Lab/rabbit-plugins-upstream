## Description:

Plan daily meals and workouts from a user's age and health profile with customizable ingredients, then schedule localized plans via OpenClaw automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[l1mufeng](https://clawhub.ai/user/l1mufeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to generate one-day meal and workout plans from their profile, food preferences, budget, language, and schedule. It can also help set up recurring OpenClaw delivery of fresh daily plans after the user confirms time, timezone, language, and destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores health, body, schedule, budget, and training information for future use and may embed that information in recurring automation prompts.

Mitigation: Install and use it only with profile data the user is willing to persist in agent memory and automation prompts; review saved profile and scheduled job content before enabling recurring delivery.

Risk: The authoritative security summary reports a calorie safety mismatch for older adults and flags higher-risk health situations.

Mitigation: Double-check calorie targets for older adults and higher-risk profiles with a qualified professional, and keep the skill's conservative health guidance visible to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/l1mufeng/skills/fitness-assistant)
- [Server-resolved GitHub provenance](https://github.com/L1MuFeng/fitness-assistant-skill/tree/main/skills/fitness-assistant)
- [Daily ingredient cost budget](references/budget.md)
- [Dialogue scripts](references/dialogues.md)
- [Output languages](references/languages.md)
- [Meal planning rules](references/meal-planning.md)
- [Opening message and intake](references/opening.md)
- [User profile](references/profile.md)
- [Scheduling the daily plan](references/scheduling.md)
- [Workout planning rules](references/training.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON calculator output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports eight output languages and may create recurring automation prompts when scheduling is requested.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata; artifact frontmatter says 0.1.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
