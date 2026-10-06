## Description:

Selects a contact for a client brief and returns the configured recipient email address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees handling client communications use the skill to obtain a recipient email address for a brief using a message kind and account tier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled recipient uses a non-deliverable .invalid address and may not be a usable contact for a real client brief.

Mitigation: Verify the recipient against approved contact records before sending any client communication.

## Reference(s):

- [Client Brief Routing Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/routing-contact-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object containing a recipient email address]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a bundled .invalid email address; does not send a message or save a business artifact.]

## Skill Version(s):

1.1.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
