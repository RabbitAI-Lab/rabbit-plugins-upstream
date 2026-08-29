## Description:

Look up Redfin real-estate listings, property details, market reports, saved homes, and saved searches through a Redfin MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search Redfin, inspect property records, review market reports, calculate mortgage payments, and access their saved Redfin homes or searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query Redfin through a signed-in browser session, including saved homes and saved searches.

Mitigation: Use it only with agents and prompts you trust, and avoid requesting Redfin account activity you do not want exposed to the agent session.

Risk: The helper extension has broad browser permissions and is part of the data access path.

Mitigation: Review the fetchproxy extension permissions before installation and keep the extension active only for intended Redfin MCP use.

Risk: Redfin does not publish a public consumer API, and the artifact states that the server uses private Redfin web endpoints.

Mitigation: Use the skill at your discretion, avoid bulk scraping or commercial reuse, and expect Redfin challenges or endpoint changes to affect reliability.

## Reference(s):

- [ClawHub redfin skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source repository](https://github.com/chrischall/redfin-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration and bash command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing MCP setup and usage guidance; connected tools return Redfin listing, property, market, saved-home, saved-search, and mortgage-calculation data.]

## Skill Version(s):

0.10.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
