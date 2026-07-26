## Description: <br>
Google Maps integration for OpenClaw that supports traffic-aware distance and travel-time calculations, turn-by-turn directions, distance matrices, geocoding and reverse geocoding, place search and details, and transit planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaharsha](https://clawhub.ai/user/shaharsha) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to answer mapping and navigation requests through Google Maps APIs, including route planning, traffic-aware travel estimates, geocoding, reverse geocoding, place search, and place details. <br>

### Deployment Geography for Use: <br>
Global, subject to Google Maps API coverage and feature availability. <br>

## Known Risks and Mitigations: <br>
Risk: Search and details results can include the user's Google API key in returned photo URLs. <br>
Mitigation: Use a restricted Google Maps API key with quotas and API restrictions, and avoid sharing transcripts or logs from place search and details results. <br>
Risk: Map queries, locations, and place lookups are sent to Google APIs. <br>
Mitigation: Do not submit sensitive location data unless the user is authorized to share it with Google Maps services. <br>
Risk: Google Maps API usage can consume quota or incur billing charges. <br>
Mitigation: Configure quotas and monitor usage for the API key before enabling the skill in routine workflows. <br>


## Reference(s): <br>
- [Google Maps Platform Coverage Details](https://developers.google.com/maps/coverage) <br>
- [ClawHub Skill Page](https://clawhub.ai/shaharsha/skills/google-maps) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses and concise text guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Google Maps API key and the Python requests package; supports optional language configuration through GOOGLE_MAPS_LANG.] <br>

## Skill Version(s): <br>
3.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
