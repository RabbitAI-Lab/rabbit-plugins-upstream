## Description:

Produces concise delivery retry guidance from a supplied recovery request without changing delivery systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations staff use this skill to turn a supplied delivery recovery request into a suggested retry mode. The result is guidance, not a completed delivery action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retry guidance could be mistaken for an action already taken in a delivery system.

Mitigation: Treat the result as a suggestion; confirm and perform any delivery-system changes separately.

Risk: Unnecessary sensitive information could be included in the request.

Mitigation: Provide only the delivery recovery fields needed for guidance; do not include credentials or private files.

## Reference(s):

- [Delivery Recovery Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-recovery-guidance-identifier)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [JSON with a retry_mode string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory output only; no delivery-system action or persisted business record.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
