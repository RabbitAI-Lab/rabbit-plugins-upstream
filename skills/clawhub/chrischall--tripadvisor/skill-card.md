## Description:

TripAdvisor travel data via the Terra API through MCP for finding hotels, restaurants, attractions, place details, ratings, reviews, photos, and nearby options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to search TripAdvisor listings, compare hotels, restaurants, and attractions, and retrieve place details, reviews, ratings, and photos through MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses an external MCP package that may be installed through npx without a pinned version.

Mitigation: Review or pin the @chrischall/tripadvisor-mcp package or source revision before installation where practical.

Risk: The skill requires a TripAdvisor Terra API key, which could be exposed if placed in committed configuration files.

Mitigation: Use a revocable key with appropriate limits and keep it out of committed project files.

Risk: The external MCP server runs with the permissions granted by the local MCP runtime.

Mitigation: Install it only in runtimes where those permissions are acceptable and review the server before deployment.

## Reference(s):

- [ClawHub tripadvisor skill listing](https://clawhub.ai/chrischall/skills/tripadvisor)
- [@chrischall/tripadvisor-mcp npm package](https://www.npmjs.com/package/@chrischall/tripadvisor-mcp)
- [TripAdvisor developer portal](https://www.tripadvisor.com/developers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may summarize compact or full TripAdvisor location, review, rating, and photo data returned by the MCP tools.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
