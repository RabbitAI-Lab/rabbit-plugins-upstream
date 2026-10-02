## Description:

Helps users search Resy restaurants, manage reservations and favorites, and subscribe to Priority Notify through a connected Resy account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy account holders use this skill to find available tables, book or cancel reservations, manage favorites, and receive availability notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected server needs a Resy email and password to access the account.

Mitigation: Use project-local configuration or protected secrets, and redact credentials when troubleshooting.

Risk: Booking or cancellation can change reservations and may incur payment terms or fees.

Mitigation: Review the exact reservation, cancellation terms, and any fees before confirming each action.

## Reference(s):

- [resy-mcp package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp repository](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses with reservation details and confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and cancellation require user confirmation.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
