## Description: <br>
Provides Zurich waste collection schedule lookups through the public OpenERZ API for waste, cardboard, paper, organic waste, special waste, and disposal dates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mbjoern](https://clawhub.ai/user/mbjoern) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to answer questions about upcoming waste collection and disposal dates in Zurich by forming OpenERZ API queries for a selected postal code, waste type, and date range. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a public OpenERZ endpoint, so answers can be incomplete or stale if the service is unavailable or schedule data changes. <br>
Mitigation: Check returned dates against the API response and retry or consult the official Zurich disposal information when results are missing or unexpected. <br>


## Reference(s): <br>
- [OpenERZ calendar API](https://openerz.metaodi.ch/api/calendar) <br>
- [ClawHub skill page](https://clawhub.ai/mbjoern/skills/erz-entsorgung-recycling-zurich) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline HTTP query examples and JSON response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include OpenERZ API URLs, curl commands, and parsed collection-date results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
