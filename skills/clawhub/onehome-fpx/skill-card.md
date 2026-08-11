## Description:

Query OneHome (CoreLogic), the agent magic-link real-estate portal at portal.onehome.com, from a shell with the fpx CLI instead of running the onehome-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query a signed-in OneHome real-estate share from a shell, including saved-search scope, shared listings, listing details, photos, and LocalLogic endpoints. It is useful when the MCP server is not installed or when OneHome data is needed in scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to extract and reuse live OneHome bearer credentials that may grant access to private account data until they expire.

Mitigation: Use it only on trusted machines and shells, do not paste or log tokens, and refresh or discard credentials when work is complete.

Risk: Examples write token-bearing request bodies and responses under /tmp, which can be exposed on shared systems.

Mitigation: Avoid shared temporary storage, restrict file permissions where possible, and delete generated token, body, and response files after use.

Risk: Some OneHome fields and endpoints are agent-only and can return authorization errors for consumer-share sessions.

Mitigation: Prefer consumer-readable saved-search flows first and check GraphQL errors before trusting results.

## Reference(s):

- [OneHome GraphQL and REST operations for fpx](references/graphql-operations.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [OneHome portal](https://portal.onehome.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell, GraphQL, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided OneHome session scope and bearer credentials; outputs are intended for review before execution.]

## Skill Version(s):

0.13.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
