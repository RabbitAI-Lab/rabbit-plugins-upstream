## Description: <br>
Generates personalized travel packing checklists using destination weather, trip length, trip type, traveler makeup, packing progress, and travel tips. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to generate weather-aware packing lists, check packed items against the list, and produce a quick checklist when live weather is not needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Destination and travel-context inputs may be sent to an external weather proxy despite contradictory privacy language in the artifact. <br>
Mitigation: Install only if that data flow is acceptable, use quick mode when live weather is unnecessary, and prefer a corrected release with consistent privacy disclosure. <br>
Risk: The manifest and actual commands are not fully aligned. <br>
Mitigation: Confirm command wiring before deployment and prefer a corrected release whose manifest matches the generate, check, and quick commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/smart-packing-list) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Guidance] <br>
**Output Format:** [JSON objects with weather summaries, categorized checklist items, essential/optional flags, packing progress, alerts, and travel tips.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The generate command may use an external weather proxy for destination weather; quick mode produces a checklist from local rules.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
