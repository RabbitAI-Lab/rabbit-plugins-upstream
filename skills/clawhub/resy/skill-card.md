## Description:

Helps users search Resy restaurants, book or cancel reservations, manage favorites, and subscribe to availability notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using Resy can find available tables, book and cancel reservations, manage their favorites, and receive alerts when a table opens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector requires live Resy account credentials.

Mitigation: Keep RESY_EMAIL and RESY_PASSWORD in private, uncommitted configuration with restricted access.

Risk: Booking or cancellation can change a live reservation and may incur fees.

Mitigation: Review the reservation details and any fees before confirming the action.

## Reference(s):

- [Resy skill on ClawHub](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp project repository (linked by skill)](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Natural-language responses with reservation details and setup examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and cancellation actions require confirmation.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
