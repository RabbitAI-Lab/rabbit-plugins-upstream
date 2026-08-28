## Description:

Helps users narrow takeout meal choices to three recommendations based on budget, dietary restrictions, and hunger level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangyang7-star-jpg](https://clawhub.ai/user/yangyang7-star-jpg)

### License/Terms of Use:

MIT-0

## Use Case:

People who feel stuck choosing takeout can use this skill to turn meal preferences into a short, decision-ready Top 3 list. It collects budget, dietary restrictions, and hunger level, then produces concise recommendations with prices and reasons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on casual meal-indecision phrases.

Mitigation: Confirm the user's meal intent and collect only the budget, dietary restrictions, and hunger level needed for the recommendation.

Risk: Real restaurant availability, prices, or delivery times may be unavailable to the agent.

Mitigation: Do not invent real stores or dishes; clearly label simulated recommendations and ask the user to verify details in their takeout app.

Risk: The skill may ask for preference or local context, such as dietary restrictions or nearby restaurant information.

Mitigation: Keep collection limited to meal-planning context and avoid requesting sensitive information that is not needed for the recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangyang7-star-jpg/skills/takeout-decision-fatigue-rescuer)
- [Server-resolved source provenance](https://github.com/Yangyang7-star-jpg/skills/tree/main/takeout-decision-fatigue-rescuer)
- [Publisher profile](https://clawhub.ai/user/yangyang7-star-jpg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a ranked Top 3 takeout recommendation list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations should reflect the user's budget, dietary restrictions, and hunger level; simulated recommendations should be labeled when real takeout data is unavailable.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
