## Description:

Helps users search Resy restaurants, manage reservations and favorites, and subscribe to Priority Notify through a configured MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy users can find tables, book or cancel reservations, manage favorite restaurants, and request availability notifications through an agent with the Resy MCP server installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server receives Resy account credentials and can act on the user's account.

Mitigation: Install deliberately, keep credential files local, access-restricted, and out of source control.

Risk: Booking or cancellation may change real reservations, use a saved payment card, or incur cancellation fees.

Mitigation: Review the restaurant, time, payment card, and cancellation terms in each preview before approving the action.

## Reference(s):

- [ClawHub resy release](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package (linked in skill documentation)](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Natural-language responses with reservation details, confirmation previews, and setup examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and cancellation actions require review of a preview before confirmation.]

## Skill Version(s):

1.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
