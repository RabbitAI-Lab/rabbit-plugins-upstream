## Description:

Query thumbtack.com from a shell to search local service professionals by trade and zip code, then read public pro profile details such as ratings, reviews, credentials, business hours, and pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Thumbtack search and profile data from shell workflows without a login, API key, browser extension, or MCP server. It is intended for read-only lookup and scripting against public consumer pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes anonymous outbound requests to Thumbtack from the user's shell.

Mitigation: Use it only with public Thumbtack pages, and do not add cookies, tokens, account credentials, private project data, or unrelated personal data to commands.

Risk: Thumbtack page data shapes and endpoints can vary by category, page type, or GraphQL response.

Mitigation: Follow the documented extractor modes, check GraphQL error bodies, and branch on optional or union fields before relying on pricing or profile data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/thumbtack-mcp)
- [Thumbtack discovery recipes](references/discovery.md)
- [Thumbtack consumer site](https://www.thumbtack.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only lookup recipes and parser usage guidance; command output is JSON when the bundled extractor and jq examples are used.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
