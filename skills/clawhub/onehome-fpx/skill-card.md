## Description:

Query OneHome (CoreLogic), the agent magic-link real-estate portal at portal.onehome.com, from a shell with the fpx CLI instead of running the onehome-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data users with authorized OneHome access use this skill to resolve saved-search scope, search shared listings, and fetch listing detail from a shell without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic links, captured Authorization headers, sessionToken values, and temporary files can expose private OneHome session access.

Mitigation: Use the skill only with authorized OneHome access, avoid shared machines, avoid logging or committing outputs, and clean up temporary files after use.

Risk: The security evidence flags weak safeguards around capturing and reusing private session tokens.

Mitigation: Prefer a pinned or local fpx CLI install, keep credentials short-lived and local, and consider an official supported integration when available.

## Reference(s):

- [OneHome GraphQL + REST operations for fpx](references/graphql-operations.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/onehome-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with shell, GraphQL, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands depend on authorized OneHome access, fpx CLI setup, and a paired Transporter browser extension.]

## Skill Version(s):

0.15.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
