## Description:

Helps agents find Redfin listings, property details, market reports, and a user's saved homes and searches through a read-only connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching homes can ask an agent to search for listings, review property and market details, estimate mortgage payments, and inspect their saved Redfin activity when signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge can access personal saved homes and searches in a signed-in Redfin session.

Mitigation: Treat saved activity as personal data and install only if comfortable granting the bridge access to the signed-in session.

Risk: Installing a third-party package and browser extension introduces software trust concerns.

Mitigation: Review the package and extension source or verify release checksums before installation; remove the configuration and extension when no longer needed.

## Reference(s):

- [ClawHub Redfin skill release](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source (linked in skill documentation)](https://github.com/chrischall/redfin-mcp)
- [ContextMint Bridge source and installation](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown with listing details, market summaries, and setup examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; saved homes and searches require a signed-in Redfin session.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
