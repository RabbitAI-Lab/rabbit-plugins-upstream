## Description:

Helps find free and inexpensive events, deals, festivals, family activities, and local guides in supported US cities through the On the Cheap network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking affordable activities can ask an agent for local events, prices, venues, and deals in supported US cities, or compare options across cities.

### Deployment Geography for Use:

United States (supported On the Cheap cities)

## Known Risks and Mitigations:

Risk: Looking up events and deals can make web requests to the On the Cheap network.

Mitigation: Use the lookup only for public information and avoid including private information in queries.

Risk: Full article views can return raw HTML and larger amounts of content.

Mitigation: Prefer concise results and request full articles or HTML only when needed.

Risk: Monthly event overviews are previews, and expired deals can appear when specifically included.

Mitigation: Check daily listings for completeness and clearly identify expired offers.

## Reference(s):

- [On the Cheap network](https://livingonthecheap.com)
- [onthecheap-mcp ClawHub release](https://clawhub.ai/chrischall/skills/onthecheap-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event listings may include dates, times, prices and venues; article details may include HTML when requested.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
