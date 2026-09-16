## Description:

Looks up Redfin real-estate listings, property details, market reports, saved homes, and saved searches through an MCP server that uses the user's signed-in Redfin browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve Redfin property listings, property details, market information, mortgage calculations, and signed-in saved-home or saved-search information for real-estate research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser extension operate against a signed-in Redfin session, which can expose saved homes, saved searches, and session-scoped browsing context.

Mitigation: Use a dedicated browser profile, keep the MCP configuration project-local, and explicitly approve any saved-home or saved-search request.

Risk: Setup asks users to run mutable third-party code from npm and a browser-extension repository.

Mitigation: Pin the npm package and fetchproxy repository to reviewed versions before installation.

Risk: The skill relies on Redfin web behavior and private endpoints, so availability or response shape can change without notice.

Mitigation: Treat returned Redfin data as source-derived research material and verify important property or market information before acting on it.

## Reference(s):

- [ClawHub redfin skill page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source repository](https://github.com/chrischall/redfin-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON configuration snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include compact or full Redfin-derived records depending on the requested MCP tool view.]

## Skill Version(s):

0.13.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
