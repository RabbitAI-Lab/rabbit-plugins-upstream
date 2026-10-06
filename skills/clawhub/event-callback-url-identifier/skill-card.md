## Description:

Select an event callback address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Integration developers and operations staff use this skill to choose a callback URL for an event subscription request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stale documentation about downstream actions and local storage could be mistaken for active behavior.

Mitigation: Treat the skill as a local URL selector; confirm any subscription registration or storage separately before relying on it.

Risk: The bundled callback address uses a placeholder domain and may not be a usable delivery endpoint.

Mitigation: Confirm the callback address with the integration owner before using it in a live subscription.

## Reference(s):

- [Event Callback Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/event-callback-url-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [HTTPS URL in the callback_url JSON field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selects a configured URL without registering a subscription, communicating externally, or persisting a business artifact.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
