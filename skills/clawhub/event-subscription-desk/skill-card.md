## Description:

Select callback addresses and register event subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Integration operators and developers use this skill to select a callback URL for an event subscription request and record the selected callback address for handoff or registration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A callback URL could point to an unintended service or domain, causing event traffic to be routed incorrectly.

Mitigation: Before registration, verify that the callback URL belongs to the intended service or domain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/event-subscription-desk)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [URI string for callback_url and JSON-like object for recorded_callback.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The recorded callback object includes subscription_draft_id, callback_url, callback_host, and callback_path.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
