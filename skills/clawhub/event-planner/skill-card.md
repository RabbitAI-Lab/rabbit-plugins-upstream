## Description: <br>
Plan events (night out, weekend, date night, team outing, meals, trips) by searching venues via Google Places API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[udiedrichsen](https://clawhub.ai/user/udiedrichsen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to plan outings, meals, team events, dates, weekend activities, and trips based on location, budget, party size, timing, and preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Location, preference, date, and meetup details are sent to Google APIs when the skill searches for venues and travel information. <br>
Mitigation: Use a restricted Google API key with quota and billing controls, and avoid entering private addresses or sensitive meetup details unless sharing them with Google APIs is acceptable. <br>
Risk: Venue hours, availability, travel times, and budget estimates may be incomplete, stale, or approximate. <br>
Mitigation: Confirm venue hours, reservations, routes, and expected costs before relying on the itinerary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/udiedrichsen/skills/event-planner) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, json, guidance] <br>
**Output Format:** [Markdown itinerary by default; optional JSON with venue details, coordinates, travel estimates, warnings, and map links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv and GOOGLE_PLACES_API_KEY; Google Directions API support is optional for more accurate travel estimates.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
