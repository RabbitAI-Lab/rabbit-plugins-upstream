## Description: <br>
Flight tracking and scheduling. Track live flights in real-time by region, callsign, or airport using OpenSky Network. Search flight schedules between airports. Use for queries like "What flights are over Switzerland?" or "When do flights from Hamburg arrive in Zurich?" or "Track flight SWR123". <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xenofex7](https://clawhub.ai/user/xenofex7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to track live flights by region, callsign, or airport and to search scheduled flights between airports. It can return live OpenSky flight details, schedule results when an AviationStack API key is configured, or manual search links when no schedule API key is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional AviationStack schedule lookup can send AVIATIONSTACK_API_KEY over an unencrypted HTTP endpoint. <br>
Mitigation: Do not configure AVIATIONSTACK_API_KEY for this version unless the AviationStack endpoint is changed to HTTPS; rotate the key if it has already been used. <br>
Risk: Flight data and schedule results come from external services and may be rate-limited, unavailable, delayed, or incomplete. <br>
Mitigation: Treat output as informational, verify operational decisions against authoritative airline or airport sources, and account for provider rate limits. <br>


## Reference(s): <br>
- [OpenSky Network API](https://openskynetwork.github.io/opensky-api/) <br>
- [OpenSky All States Endpoint](https://opensky-network.org/api/states/all) <br>
- [AviationStack](https://aviationstack.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/xenofex7/skills/flight-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain-text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live API responses, schedule lookup results, or fallback search links depending on query and API-key configuration.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
