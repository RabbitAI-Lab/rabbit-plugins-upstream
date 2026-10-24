## Description:

Search and explore GetYourGuide tours, activities, attraction tickets, options, and reviews through a read-only connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and other external users can find and compare GetYourGuide tours, activities, tickets, options, and customer reviews. Booking takes place on GetYourGuide rather than through this skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the connector runs an npm package from a third-party publisher.

Mitigation: Confirm the npm package publisher and source are trusted before running it.

Risk: The connector requires a GetYourGuide partner API key, and some endpoints may be unavailable to a given partner tier.

Mitigation: Use a partner key intended for this connector; if requests fail, check the partner dashboard and connector health check.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [getyourguide-mcp npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide partner program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only tour listings and details, options, reviews, and links to book on GetYourGuide.]

## Skill Version(s):

2.1.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
