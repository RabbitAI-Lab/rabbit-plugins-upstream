## Description:

3GPP Scout helps agents search the 3GPP TS/TR corpus across Rel-15 through Rel-20, including specification text, diagrams, figures, and hosted MCP access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chriscarrotlabs](https://clawhub.ai/user/chriscarrotlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, telecom engineers, standards researchers, and agent users use this skill to search and cite 3GPP technical specifications, figures, and sections when answering standards questions or comparing behavior across releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 3GPP research queries are sent to the 3GPP Scout hosted API.

Mitigation: Use the skill only when the user is comfortable sharing those queries with 3GPP Scout and has reviewed the provider's privacy terms.

Risk: Search and document endpoints require a Scout API key or OAuth-authenticated MCP session.

Mitigation: Store the API key in SCOUT_API_KEY or use MCP OAuth; do not paste credentials into prompts or configuration that may be shared.

Risk: Quota exhaustion can interrupt REST, MCP, or hosted-chat retrieval workflows.

Mitigation: Check quota details returned with HTTP 402 responses and wait for the reset time or upgrade through the provider dashboard.

## Reference(s):

- [3GPP Scout ClawHub Skill](https://clawhub.ai/chriscarrotlabs/skills/3gpp-scout)
- [3GPP Scout Homepage](https://3gppscout.com)
- [3GPP Scout API Documentation](https://api.3gppscout.com/docs)
- [3GPP Scout Agent Setup](https://api.3gppscout.com/agent-setup/prompt.md)
- [3GPP Scout Hosted MCP](https://api.3gppscout.com/mcp/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with endpoint descriptions, JSON request and response shapes, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call 3GPP Scout search, document, section, image, and MCP endpoints; no local files are produced by the skill itself.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
