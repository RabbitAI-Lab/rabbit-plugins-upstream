## Description:

BigFish is a fishing assistant that analyzes fishing spot photos, weather, pressure, and local knowledge to recommend target fish, techniques, bait, timing, and trip reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External fishing enthusiasts use this skill to evaluate potential fishing spots, choose target species and tackle, plan outing timing, and keep structured fishing logs. It supports freshwater, lure, shore, and sea-fishing scenarios using local knowledge files plus user-provided photos, location, weather, and catch history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fishing photos, city or spot details, and catch history can reveal sensitive location or personal activity patterns.

Mitigation: Ask users to share only the location precision needed for the recommendation and avoid retaining or repeating private spot details unless the user explicitly wants them in a trip log.

Risk: Spot and fish-activity recommendations are probabilistic and can be wrong when photos, weather, or local conditions are incomplete.

Mitigation: Present recommendations as evidence-based estimates and encourage users to verify conditions, access rules, and safety constraints before fishing.

## Reference(s):

- [BigFish ClawHub skill page](https://clawhub.ai/kobenfang/skills/bigfish)
- [Publisher profile](https://clawhub.ai/user/kobenfang)
- [Related weather skill](/skills/weather)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance with structured recommendations and trip-report summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include species likelihood scores, timing ratings, bait and tackle suggestions, and structured fishing log entries.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
