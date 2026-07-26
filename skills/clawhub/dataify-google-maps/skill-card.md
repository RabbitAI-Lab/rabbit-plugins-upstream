## Description: <br>
Dataify Google Maps helps an agent collect Google Maps search or place-detail parameters, confirm them with the user, and submit the approved request to the Dataify Scraper API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when a user asks an agent to run a Google Maps search, fetch map search results, or request Google Maps place details through Dataify after reviewing the request parameters. <br>

### Deployment Geography for Use: <br>
Global, subject to Dataify availability, Google Maps-related terms, and the user's local privacy and compliance requirements. <br>

## Known Risks and Mitigations: <br>
Risk: Google Maps search terms, locations, place IDs, and related parameters are sent to Dataify when the user approves a live API call. <br>
Mitigation: Review the confirmation table before approving each call, especially for precise locations or private business queries, and use the skill only when sending those parameters to Dataify is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-maps) <br>
- [Dataify publisher profile](https://clawhub.ai/user/dataify-server) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, text] <br>
**Output Format:** [A pre-call Markdown parameter table, a Python command for the bundled Dataify Google Maps script, and the raw API response body returned as text.] <br>
**Output Parameters:** [Google Maps request fields such as q, json, ll, location, lat, lon, z, m, nearby, google_domain, hl, gl, start, type, data, place_id, data_cid, no_cache, plus a Dataify API token supplied through the environment or command argument.] <br>
**Other Properties Related to Output:** [The skill requires explicit user confirmation before live calls, omits Authorization from confirmation tables, submits form-encoded requests, and returns the API response without reshaping it.] <br>

## Skill Version(s): <br>
1.2.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
