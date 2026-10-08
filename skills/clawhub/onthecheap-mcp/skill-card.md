## Description:

Finds free and inexpensive events, deals, and local guides for supported US cities through the On the Cheap network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People looking for affordable activities use this skill to find local events by date, compare nearby options, and search deals and family activities in supported US cities.

### Deployment Geography for Use:

United States (supported On the Cheap cities and national deals)

## Known Risks and Mitigations:

Risk: Queries contact the On the Cheap network for city listings.

Mitigation: Share only the city and filters needed for the request; do not include sensitive information in searches.

Risk: Full article options can return upstream HTML.

Mitigation: Use compact or plain-text results by default and treat article content as untrusted source material.

Risk: Monthly event overviews show previews, not complete daily schedules.

Mitigation: Use the daily event listing before presenting a complete schedule.

## Reference(s):

- [On the Cheap network](https://livingonthecheap.com)
- [On the Cheap skill on ClawHub](https://clawhub.ai/chrischall/skills/onthecheap-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries of events, deals, and articles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listings can include dates, times, prices, venues, and source links; full article content or HTML is available on request.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
