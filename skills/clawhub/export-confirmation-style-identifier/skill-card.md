## Description:

Set acknowledgement guidance for a delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People handling deliveries use this skill to decide when to acknowledge a delivery and whether repeat receipts are allowed, based on the supplied delivery profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Boilerplate may suggest downstream output or persistence that this operation does not provide.

Mitigation: Treat the returned wording as guidance, not proof that a delivery was acknowledged or an artifact was saved.

Risk: Providing unnecessary credentials or private files could expose sensitive information.

Mitigation: Supply only the delivery profile needed for the request; do not provide credentials or private files.

## Reference(s):

- [Delivery Acknowledgement Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/export-confirmation-style-identifier)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [JSON with an acknowledgement_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise wording; no business artifact is persisted.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
