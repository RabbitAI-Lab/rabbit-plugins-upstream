## Description:

Read angi.com, a US home-services directory, from shell workflows with the fpx CLI to find pros by trade and city, inspect pro profiles, review ratings and reviews, and list trade and city taxonomy without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to retrieve Angi public provider, rating, review, and taxonomy data in shell-based workflows. Users may optionally inspect signed-in Angi account data from their own browser session when they intentionally pair the my.angi.com host.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Optional my.angi.com workflows can read information from the user's signed-in Angi account through the paired browser session.

Mitigation: Only pair the my.angi.com host when account-data access is intentional, and keep the profile scoped to the hosts needed for the task.

Risk: Pairing through @fetchproxy/cli and the Transporter extension persists and creates a browser-session trust boundary.

Mitigation: Review the fpx and Transporter trust boundary before installation, use a dedicated profile where appropriate, and remove pairing when it is no longer needed.

Risk: Search pages can emit duplicate provider records and optional signed-in account fields are not fully characterized.

Mitigation: Use the documented --dedupe id option for search results and inspect returned account-data fields directly instead of assuming a stable schema.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi RSC flight extractor](references/rsc.mjs)
- [Angi](https://angi.com/)
- [Angi trade sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown instructions with inline shell commands and JSON-processing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce command recipes and extracted JSON records when used with fpx, node, jq, and the bundled RSC extractor.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
