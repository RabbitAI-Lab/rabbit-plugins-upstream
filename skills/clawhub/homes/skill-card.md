## Description:

Look up real-estate listings, property details, price and tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate analysts use this skill to retrieve homes.com listing data, property details, historical price and tax information, saved homes, and market summaries through an agent. It is also useful for local mortgage, affordability, and rent-versus-buy calculations when users provide the required inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on mutable external components, including the homes-mcp npm package and a separately installed unpacked browser extension.

Mitigation: Review those components before installation and pin an exact package version and extension commit for controlled deployments.

Risk: The fetchproxy bridge uses a signed-in browser session, which can expose unrelated browser cookies, sessions, or browsing data if installed in a general-use profile.

Mitigation: Use a dedicated Chrome profile signed in only to homes.com for this skill.

Risk: homes.com does not provide a public consumer API, so page structure changes, AWS WAF challenges, or session state can affect reliability.

Mitigation: Run the health check before use, keep a signed-in homes.com tab available when needed, and treat failures or missing fields as retrieval limitations rather than verified absence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [fetchproxy extension repository](https://github.com/chrischall/fetchproxy)
- [homes-mcp source link from skill documentation](https://github.com/chrischall/homes-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Natural-language responses with structured JSON returned from MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools default to compact output that strips image URLs; full view can include property photos and floorplan URLs.]

## Skill Version(s):

1.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
