## Description:

Select a contact for a client brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees handling client briefs use this skill to select a configured recipient from a request's message kind and account tier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured contact may be mistaken for an approved, deliverable business address.

Mitigation: Confirm the recipient against the current approved routing directory before using it; bundled examples use a .invalid domain.

## Reference(s):

- [Client Brief Routing Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/routing-contact-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object containing a recipient email string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses configured local contact data; does not send messages or contact a network service.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
