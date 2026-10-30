## Description:

Plan a walkable bar crawl, craft beer crawl, dinner and drinks, or club night near a place, using only venues DrinkedIn has validated against an official licence register or premises census, or the venue's own site.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haim-barad](https://clawhub.ai/user/haim-barad)

### License/Terms of Use:

MIT

## Use Case:

Adults of legal drinking age where they are can use the skill to plan a walkable night out from venues that DrinkedIn has validated. It helps an agent gather the user's chosen location and preferences, request a route from the DrinkedIn Night Out service, and relay the returned stops and walking estimates without inventing venue details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A typed address is sent to the external OpenStreetMap Nominatim geocoder, and route-link copies are described as lasting 30 days; server-side retention guarantees were not independently verified.

Mitigation: Use only a location the person is comfortable sharing with DrinkedIn, prefer coordinates when available to avoid geocoding, and consult DrinkedIn's privacy policy for details.

Risk: Anyone who receives a saved route link can open it.

Mitigation: Share route links only with the intended recipients.

Risk: Venue hours and prices are unverified and may be out of date or unavailable.

Mitigation: Ask the person to check hours and prices with each venue before going.

## Reference(s):

- [DrinkedIn Night Out documentation](https://drinkedin.net/docs/night-out)
- [DrinkedIn Night Out MCP server](https://ai.drinkedin.net/mcp/night-out)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [A route summary with ordered venue stops, addresses, categories, walking estimates, and a share link when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes contain 2 to 4 stops when available; venue hours and prices are unverified.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
