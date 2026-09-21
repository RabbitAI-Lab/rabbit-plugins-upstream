## Description:

Fless Apartment Hunt helps an agent research live Fless apartment data for supported Washington, DC, Maryland, and Virginia cities, collect a renter brief, and generate a pre-filled hunt link for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fless-io-dev](https://clawhub.ai/user/fless-io-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External renters and their assisting agents use this skill to research Fless-supported apartment markets, collect budget, bedroom, move-in, POI, amenity, pet, smoking, and age-restriction criteria, and prepare a validated hand-off link. The human reviews the pre-filled form and handles account creation, email verification, and any payment directly on Fless.

### Deployment Geography for Use:

Global use; apartment hunt coverage is limited to Washington, DC, Maryland, and Virginia.

## Known Risks and Mitigations:

Risk: Apartment criteria such as budget, move-in date, desired locations, pets, smoking, and similar restrictions may be sent to Fless to build a pre-filled hunt link.

Mitigation: Review the hunt criteria and generated link before submission, and avoid including unnecessary personal, account, password, email verification, or payment details.

Risk: The skill can prepare a hand-off link but must not complete account creation, email verification, or payment for the user.

Mitigation: Keep sign-in, password entry, email verification, and payment actions in the user's browser under the user's control.

Risk: Apartment hunts are only valid for live Fless coverage areas; unsupported or coming-soon cities cannot start a hunt.

Mitigation: Check city coverage before collecting the full brief, offer waitlists for coming-soon cities, and do not build hunt links for unsupported locations.

Risk: Rent, score, neighborhood, and availability information can be stale or unavailable if not retrieved from current Fless data.

Mitigation: Use live Fless data or clearly state when information is unknown, then verify that the generated link is complete and matches the target city.

## Reference(s):

- [Fless Hunt How-To](https://fless.io/hunt-how-to.md)
- [Fless MCP Server](https://mcp.fless.io/mcp)
- [Fless AI Agents](https://fless.io/ai-agents)
- [API reference](references/API.md)
- [City coverage](references/CITIES.md)
- [Hunt fields](references/HUNT_FIELDS.md)
- [Error catalog and recovery](references/ERRORS.md)

## Skill Output:

**Output Type(s):** [guidance, API calls, markdown, configuration]

**Output Format:** [Markdown guidance with JSON API/MCP request parameters and URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a pre-filled Fless hunt link when the brief is complete; account creation, email verification, and payments stay with the human.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
