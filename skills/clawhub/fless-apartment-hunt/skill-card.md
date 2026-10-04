## Description:

Helps renters research supported cities and build a pre-filled Fless apartment-hunt link for their review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fless-io-dev](https://clawhub.ai/user/fless-io-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Renters and their assistants can check live Fless coverage and local rental information, collect search preferences, and prepare a hunt link. The renter reviews the form, creates the hunt, and approves any building outreach.

### Deployment Geography for Use:

Washington, DC, Maryland, and Virginia (live Fless cities only)

## Known Risks and Mitigations:

Risk: Search criteria shared with Fless may contain sensitive details about a renter's plans and preferences.

Mitigation: Share only the criteria needed to build the link; let the renter review the pre-filled form and complete account creation and payment in their own browser.

Risk: Building outreach could occur without the renter understanding or approving the matched list.

Mitigation: Explain that the renter must approve matched buildings in the Fless dashboard before any outreach; the agent should not approve on their behalf.

## Reference(s):

- [Fless agent information](https://fless.io/ai-agents)
- [Fless hunt instructions](https://fless.io/hunt-how-to.md)
- [Fless MCP server](https://mcp.fless.io/mcp)
- [Hunt field reference](references/HUNT_FIELDS.md)
- [City coverage reference](references/CITIES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with rental findings and a pre-filled hunt link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The renter reviews and confirms the hunt and approves matched buildings before outreach.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
