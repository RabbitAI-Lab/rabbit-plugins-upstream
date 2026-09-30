## Description:

Selects an event callback address and records a local receipt for a supplied callback URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration operators use this skill to select a callback URL from a subscription request and create a local record of the selected address.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration writes a receipt file to the caller-selected directory.

Mitigation: Provide a dedicated writable output folder rather than a broad project or home directory.

Risk: A local receipt could be mistaken for confirmation of an external subscription.

Mitigation: Treat the receipt as a local record and verify any external registration separately.

## Reference(s):

- [Event Subscription Desk release](https://clawhub.ai/wxt-ai/skills/event-subscription-desk)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a callback URL or recorded-callback object; registration also writes a local receipt under the chosen output directory, not an external subscription.]

## Skill Version(s):

3.0.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
