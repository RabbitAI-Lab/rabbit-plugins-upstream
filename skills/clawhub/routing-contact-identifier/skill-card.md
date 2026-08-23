## Description:

Select a contact for a client brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to route routine client communications by selecting a concise recipient for a client brief from the supplied routing request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill does not include an installer's routing table or policy.

Mitigation: Verify returned recipients against the organization's current business routing rules before acting on them.

Risk: Incomplete or inaccurate routing_request details may lead to an unsuitable recipient.

Mitigation: Provide the relevant message_kind and account_tier, and review the selected recipient before sending client communications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/routing-contact-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Concise recipient value in the requested output field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an email recipient derived from the supplied routing_request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
