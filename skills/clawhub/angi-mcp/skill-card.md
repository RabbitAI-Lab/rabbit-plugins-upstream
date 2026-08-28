## Description:

Read angi.com from a shell with the fpx CLI to find home-service pros by trade and city, inspect pro profiles, review ratings and reviews, and list trade/city taxonomy without running the angi-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to gather Angi directory data for US home-service providers, including taxonomy, search results, provider profiles, ratings, and reviews. It is useful when Angi data is needed from shell workflows or environments where the MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pairing my.angi.com can let the agent read signed-in account pages through the user's browser session.

Mitigation: Pair my.angi.com only when account data is intentionally needed, and avoid prompts that request account areas the user does not want exposed in session output.

Risk: Angi content fetches depend on fpx and the Transporter browser extension using an open, cleared tab.

Mitigation: Pair only the host being fetched, keep the relevant Angi tab open, and refresh the tab or run fpx health when fetches return bridge or bot-wall errors.

## Reference(s):

- [Angi Skill Release](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi Page Shapes and Recipes](references/angi-pages.md)
- [Angi RSC Flight Extractor](references/rsc.mjs)
- [Angi Trade Sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)
- [Angi Plumbing Geo Sitemap Example](https://www.angi.com/sitemap/angi-geocat-plumbing.xml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples and JSON extraction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fpx, curl, node, and jq commands for read-only Angi data retrieval.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
