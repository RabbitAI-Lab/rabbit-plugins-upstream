## Description:

Validates an event callback URL and creates a local subscription draft and receipt without registering it with an external service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration operators use this skill to validate a callback address and prepare a local subscription draft with a receipt. It does not activate a real event subscription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local draft could be mistaken for a callback registered with a live event service.

Mitigation: Treat the receipt as a local record only; complete and verify any live registration separately.

Risk: Running the skill creates JSON draft and receipt files in the selected output directory.

Mitigation: Choose a dedicated writable output directory and review its contents before sharing or retaining them.

## Reference(s):

- [Subscription Receipt Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/event-callback-url-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local JSON subscription draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response includes recorded_callback and an effect receipt with the local file path and checksum.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
