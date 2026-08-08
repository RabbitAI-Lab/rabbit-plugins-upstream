## Description:

Look up real-estate listings, property details, price/tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve homes.com real-estate listing data, property records, market summaries, saved homes, saved searches, and photo galleries through an MCP server. It also supports local mortgage, affordability, and rent-versus-buy calculations when the user supplies the required inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read homes.com pages visible in the user's active browser session, including saved homes and saved searches when requested.

Mitigation: Install and use it only when read access to the active homes.com session is acceptable, and treat the integration as read-only homes.com automation rather than an official homes.com API.

Risk: homes.com access depends on a signed-in browser tab and the fetchproxy extension, so availability and returned data can depend on the user's live browser session.

Mitigation: Confirm that the browser session and fetchproxy extension are active before relying on results, especially for saved homes or saved searches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [fetchproxy extension setup](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text with inline configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MCP outputs may include homes.com listing details, property history, saved-home data, photo URLs, market summaries, and calculator results.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
