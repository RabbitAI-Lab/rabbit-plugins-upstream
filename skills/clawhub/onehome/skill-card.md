## Description:

Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches. Use when the user asks about real estate listings shared by their agent, OneHome links, portal.onehome.com properties, or specific addresses / MLS numbers they want to look up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search private OneHome portal listings shared by a real-estate agent, retrieve property details, photos, school information, saved searches, and compare listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome magic links, JWTs, and captured portal sessions can grant access to private portal data.

Mitigation: Install only when the agent should access that OneHome portal, keep credentials in scoped environment variables or capture flows, and do not paste full magic links, JWTs, screenshots, logs, or outputs containing token values into chat.

Risk: Expired or unavailable OneHome authentication can cause failed or stalled portal lookups.

Mitigation: Run the OneHome health check before lookup workflows and refresh the token or portal capture when expiry is near or authentication is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [guidance, configuration, text]

**Output Format:** [Markdown instructions and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API-backed OneHome MCP tool calls and local mortgage or affordability calculations; OneHome credentials and portal data should be treated as sensitive.]

## Skill Version(s):

0.13.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
