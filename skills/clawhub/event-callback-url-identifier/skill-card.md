## Description:

Select an event callback address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration operators use this skill for routine integration work when they need to select a callback URL for an event subscription request or service handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A selected callback URL may be used before its endpoint ownership or security is validated.

Mitigation: Review the generated URL and verify endpoint ownership, transport security, and intended routing before using it in a real integration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/event-callback-url-identifier)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Concise URI string in the callback_url field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user-supplied subscription_request; does not validate live endpoint ownership or security.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
