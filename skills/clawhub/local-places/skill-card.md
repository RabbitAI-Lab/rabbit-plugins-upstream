## Description: <br>
Search for places (restaurants, cafes, etc.) via Google Places API proxy on localhost. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent users use this skill to resolve natural-language locations, search nearby places, and retrieve structured Google Places details through a local FastAPI proxy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local proxy can expose unauthenticated Google Places API-key-backed usage beyond localhost if bound to a LAN-facing address. <br>
Mitigation: Run the server on 127.0.0.1 by default and only bind to 0.0.0.0 when intentional network exposure and access controls are in place. <br>
Risk: Place and location queries are sent to Google Places. <br>
Mitigation: Use the skill only when users are comfortable sharing those queries with Google Places. <br>
Risk: An overridden GOOGLE_PLACES_BASE_URL could send requests and API-key-backed traffic to an untrusted endpoint. <br>
Mitigation: Leave GOOGLE_PLACES_BASE_URL unset or verify that it points to a trusted endpoint before use. <br>
Risk: Raw request-body logging can expose location queries or other submitted data in logs. <br>
Mitigation: Review logging behavior and remove raw request-body logging before regular use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/steipete/skills/local-places) <br>
- [Publisher Profile](https://clawhub.ai/user/steipete) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, JSON] <br>
**Output Format:** [Markdown guidance with curl examples and JSON place results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv and GOOGLE_PLACES_API_KEY; search returns place summaries and optional next_page_token, while details and location resolution return structured JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
