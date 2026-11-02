## Description:

Plans walkable bar crawls, dinner-and-drinks outings, and club nights using DrinkedIn-validated venues near a specified place.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haim-barad](https://clawhub.ai/user/haim-barad)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to plan a walkable night out near a place they name or a location they share. It returns venue stops and route details based on DrinkedIn-validated venue records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A typed address is forwarded to the public OpenStreetMap Nominatim geocoder.

Mitigation: Use a general area instead of a precise address if preferred.

Risk: Anyone with a saved route link can view its stops.

Mitigation: Share route links only with people intended to see the stops.

Risk: Venue hours and prices are unverified, and the remote service's retention promises have not been independently audited.

Mitigation: Check hours and prices with venues directly, and avoid relying on unverified retention claims.

## Reference(s):

- [DrinkedIn Night Out documentation](https://drinkedin.net/docs/night-out)
- [DrinkedIn Night Out MCP server](https://ai.drinkedin.net/mcp/night-out)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown with venue stops, walking details, notices, and an optional route link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Route details are relayed from the service; venue hours and prices are identified as unverified.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
