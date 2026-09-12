## Description:

Find flights with Starlink satellite WiFi, filter to Starlink-equipped airlines, rank by WiFi score, price, duration, or jet lag, and return booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[assistant-design](https://clawhub.ai/user/assistant-design)

### License/Terms of Use:

MIT

## Use Case:

External users and travel-focused agents use ClawFlight to search routes where in-flight connectivity matters, compare Starlink-equipped carriers, and get ranked flight options with booking links. The skill is aimed at business travelers and digital nomads who need to work during flights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an Amadeus bearer token locally.

Mitigation: Document token storage clearly, restrict cache file permissions, and rotate or delete cached tokens when uninstalling or sharing a workspace.

Risk: The skill writes saved flights and user-submitted WiFi ratings to local files.

Mitigation: Provide retention and deletion controls, and avoid saving sensitive itinerary details unless needed for the rating workflow.

Risk: The skill returns affiliate-tagged booking links.

Mitigation: Disclose the affiliate relationship anywhere booking links are shown so users can make an informed choice.

Risk: The security scan notes scanner-flagged HTTP dependencies.

Mitigation: Review and update HTTP dependencies before broad installation, and rescan the release after dependency changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/assistant-design/skills/clawflight)
- [Amadeus for Developers self-service](https://developers.amadeus.com/self-service)
- [Kiwi.com Tequila API](https://tequila.kiwi.com)
- [Amadeus production API endpoint](https://api.amadeus.com)
- [Amadeus test API endpoint](https://test.api.amadeus.com)
- [Publisher profile](https://clawhub.ai/user/assistant-design)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Console text and optional JSON flight-search results with booking links and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Amadeus API credentials for live flight search; saves selected flights, ratings, and an Amadeus bearer-token cache under the local data directory.]

## Skill Version(s):

1.0.0 (source: release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
