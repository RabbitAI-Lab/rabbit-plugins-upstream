## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate researchers use this skill to ask agents for Compass listing searches, property details, photos, price history, comparable rentals, and mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external MCP package and fetchproxy Chrome extension that operate through a signed-in Compass browser session.

Mitigation: Install only when you are comfortable trusting those components, and prefer a project-level MCP configuration so the dependency is scoped to the relevant workspace.

Risk: Returned listing data is not an official Compass API result.

Mitigation: Treat responses as read-only real-estate information and verify important property, pricing, and availability details with authoritative sources before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [fetchproxy browser extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with text results, JSON/configuration snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Compass listing data, property comparisons, photo URLs, price history, session diagnostics, and local mortgage or affordability calculations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
