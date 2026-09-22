## Description:

Helps an MCP-capable agent research Fless-supported apartment markets, collect a renter's hunt brief, and build a validated pre-filled Fless hunt link for the human to review and submit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fless-io-dev](https://clawhub.ai/user/fless-io-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer Fless-specific apartment hunting questions, check city coverage in the Washington, DC, Maryland, and Virginia market, collect required renter criteria, and hand off a pre-filled hunt link for human review.

### Deployment Geography for Use:

United States: Washington, DC, Maryland, and Virginia service areas

## Known Risks and Mitigations:

Risk: Broad activation wording may cause ordinary apartment, rent, or neighborhood questions to route through Fless data or endpoints.

Mitigation: Use the skill when Fless-specific apartment hunting assistance is intended, and confirm city coverage before starting the workflow.

Risk: Apartment searches can involve personal account details, payment actions, and unnecessary personal data.

Mitigation: Keep names, passwords, payment actions, and unneeded personal details out of agent-provided fields; the human creates accounts, verifies email, pays, and submits in the browser.

Risk: The workflow depends on live Fless city, rent, score, and validation data that can change.

Mitigation: Retrieve current Fless data before answering, do not invent rents or availability, and rebuild or correct hunt links when validation reports missing fields or errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fless-io-dev/skills/fless-apartment-hunt)
- [Fless agent homepage](https://fless.io/ai-agents)
- [Fless hunt documentation](https://fless.io/hunt-how-to.md)
- [Fless MCP server](https://mcp.fless.io/mcp)
- [API reference](references/API.md)
- [City coverage](references/CITIES.md)
- [Error catalog and recovery](references/ERRORS.md)
- [Hunt fields](references/HUNT_FIELDS.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, API Calls, configuration]

**Output Format:** [Markdown guidance with MCP or REST tool arguments and generated Fless URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed by the human before account creation, email verification, payment, or hunt submission.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
