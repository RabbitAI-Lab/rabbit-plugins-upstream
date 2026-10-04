## Description:

Helps agents find GetYourGuide tours, activities, attraction tickets, options, and reviews through a read-only search connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to discover GetYourGuide tours, tickets, availability options, and customer reviews before following a listing to book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted npm package could expose the agent environment to unwanted behavior.

Mitigation: Confirm that you trust the referenced npm package before enabling the connector.

Risk: A GetYourGuide partner API key is placed in MCP configuration.

Mitigation: Store the key securely in the intended MCP configuration and avoid sharing it in prompts or published files.

Risk: Broad travel-activity requests may be answered from GetYourGuide inventory rather than a broader set of providers.

Mitigation: Make the source of recommendations clear and consider other providers when the request calls for a broad comparison.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [getyourguide-mcp npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide partner program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries of tour searches, details, options, and reviews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only discovery; booking takes place on GetYourGuide.]

## Skill Version(s):

2.1.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
