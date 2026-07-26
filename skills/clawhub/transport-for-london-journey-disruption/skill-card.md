## Description: <br>
Plan TfL journeys from start/end/time, resolve locations (prefer postcodes), and warn about disruptions; suggest alternatives when disrupted. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[diegopetrucci](https://clawhub.ai/user/diegopetrucci) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to plan London public transport journeys, resolve ambiguous TfL locations, check active disruption status, and surface alternative routes when a candidate journey is affected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Journey start and end locations, travel times, and optional TfL API credentials are sent to TfL API endpoints. <br>
Mitigation: Use the skill only when sharing those trip details with TfL is acceptable, and configure TFL_APP_ID and TFL_APP_KEY only when credentialed TfL requests are intended. <br>
Risk: Disruption statuses reflect current TfL conditions and may change before future travel. <br>
Mitigation: For journeys later today or on another date, recheck the route near the travel time before relying on a disruption summary. <br>


## Reference(s): <br>
- [TfL API Documentation](https://tfl.gov.uk/info-for/open-data-users/api-documentation) <br>
- [TfL Unified API](https://api.tfl.gov.uk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with concise route summaries and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include TfL disambiguation options, route recommendations, active disruption warnings, and alternative journey suggestions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
