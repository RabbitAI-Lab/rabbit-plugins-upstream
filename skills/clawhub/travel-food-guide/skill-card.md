## Description:

Helps travelers find restaurants near attractions, discover local specialties, and generate multi-day dining plans with cuisine, budget, and distance preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers use this skill to search for nearby restaurants, identify city-specific foods and dining areas, and plan meals across a trip based on itinerary, budget, cuisine, and dietary preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live restaurant search sends destination, attraction, hotel or address, cuisine, budget, radius, and similar food-search details to an external proxy service.

Mitigation: Use the skill only when that proxy relationship is acceptable, and avoid entering highly sensitive locations.

Risk: Restaurant data and local food guidance may be incomplete, stale, or unavailable for some cities or venues.

Mitigation: Treat recommendations as planning assistance and verify time-sensitive details such as opening hours, reservations, dietary constraints, and current reviews before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-food-guide)
- [Live map proxy endpoint](https://1439498936-bl10af74fl.ap-guangzhou.tencentscf.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Natural-language travel dining guidance with JSON tool results and inline shell command usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include restaurant names, addresses, distances, ratings when available, average cost estimates, local specialty lists, food street recommendations, and multi-day meal plans.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
