## Description:

Guides an agent through querying authorized OneHome/CoreLogic real-estate portal data with the fpx CLI using documented REST and GraphQL calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents with authorized OneHome access use this skill to obtain the relevant session scope, search shared listings, and retrieve listing details from a shell without running a separate MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to exchange or capture live OneHome session credentials and reuse them from a shell.

Mitigation: Install only when authorized to access the target OneHome data; treat bearer tokens, magic-link tokens, temporary files, and command transcripts as sensitive account material and clean them after use.

Risk: Some operations may expose data that is only available to agent sessions or specific shared-search scopes.

Mitigation: Use the consumer-readable saved-search path first, check GraphQL errors before using results, and avoid attempting agent-only queries unless the session is authorized for them.

## Reference(s):

- [GraphQL and REST operation examples](references/graphql-operations.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes command patterns for fpx, jq, REST requests, and GraphQL request bodies.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
