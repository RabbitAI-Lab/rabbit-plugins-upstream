## Description: <br>
Feast helps an agent plan weekly meals with cultural themes, authentic recipes, intelligent shopping lists, dietary preferences, seasonal awareness, and immersive meal playlists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smadgerano](https://clawhub.ai/user/smadgerano) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and household meal planners use Feast through an agent to set up dietary and regional preferences, plan weekly meals, generate shopping lists, receive reminders, and reveal recipes with cultural context and playlists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Feast stores personal meal-planning data, including dietary restrictions, allergies, location, schedule, budget, store preferences, notification settings, and meal history. <br>
Mitigation: Review the data kept under workspace/meals before installation and remove or redact stored profile, history, and schedule files when the skill is no longer needed. <br>
Risk: Scheduled reminders can send meal-planning information through configured chat or push notification channels. <br>
Mitigation: Use an explicit notification channel when privacy matters, enable Pushbullet or ntfy only after reviewing those services, and remove stored cron jobs when stopping use. <br>


## Reference(s): <br>
- [ClawHub Feast Skill Page](https://clawhub.ai/smadgerano/skills/feast) <br>
- [Specification](docs/SPECIFICATION.md) <br>
- [Onboarding](references/onboarding.md) <br>
- [Theme Research](references/theme-research.md) <br>
- [Price Checking](references/price-checking.md) <br>
- [Nutrition](references/nutrition.md) <br>
- [Seasonality](references/seasonality/README.md) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and YAML-backed workspace files, with occasional shell commands for history updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update meal profile, history, weekly plan, favourites, failures, shopping list, and notification schedule files in the user's workspace.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
