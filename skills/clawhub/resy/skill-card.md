## Description:

Helps users search Resy restaurants, book or cancel reservations, manage favorites, and subscribe to availability notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy account holders use this skill to find tables, manage reservations and favorites, and receive alerts when tables become available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account access through a signed-in browser session or token exposes sensitive reservation information.

Mitigation: Review the installed package and browser bridge, and grant access only to a Resy account you intend to use.

Risk: Cached authentication tokens can remain on disk after a session.

Mitigation: Protect the token cache or disable token caching when local persistence is inappropriate.

Risk: Bookings or cancellations can affect live reservations and may incur fees.

Mitigation: Review the reservation, payment, and fee details in each confirmation preview before approving an action.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability results, reservation details, and confirmation previews for account actions.]

## Skill Version(s):

1.3.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
