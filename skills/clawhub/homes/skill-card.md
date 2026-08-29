## Description:

Look up real-estate listings, property details, price/tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate researchers use this skill to query homes.com listings, property records, histories, market reports, saved homes, saved searches, and photo galleries through an MCP-backed workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes homes.com requests through a signed-in browser session, including auth-gated saved homes and saved searches.

Mitigation: Install only if that session access is acceptable, treat saved homes and saved searches as private account data, and review browser extension permissions before use.

Risk: Reproducibility can vary if homes-mcp or fetchproxy dependencies are installed without version pinning.

Mitigation: Prefer pinned package versions when reproducibility matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source](https://github.com/chrischall/homes-mcp)
- [fetchproxy extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown responses with structured real-estate data, setup snippets, and comparison tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only homes.com data access; requires homes-mcp and an active fetchproxy browser extension session.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
