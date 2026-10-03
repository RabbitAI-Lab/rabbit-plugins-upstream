## Description:

Select an event callback address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration operators use this skill to obtain a callback URL for an event subscription request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled callback address uses a .invalid domain and cannot serve as a live integration endpoint.

Mitigation: Confirm a real, approved callback destination before using the result in a live subscription.

Risk: Including credentials or private files in the subscription request is unnecessary.

Mitigation: Provide only the intended request JSON; do not include credentials or private files.

## Reference(s):

- [Event Callback Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/event-callback-url-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON with a callback_url URI string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a local result without contacting the callback endpoint.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
