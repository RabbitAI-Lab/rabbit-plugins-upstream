## Description:

Guides agents in querying shared OneHome real-estate listings through the fpx CLI and an authorized browser session without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers with authorized access to a OneHome account or share can retrieve saved-search scope, shared listings, and listing details from a shell instead of using the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session credentials or magic links may be exposed through shell commands, logs, or temporary files.

Mitigation: Use only authorized sessions; keep links and tokens out of shared machines, shell logs, and predictable temporary files, and do not reuse them beyond the intended session.

Risk: Queries may disclose private OneHome listing or contact data beyond the intended share.

Mitigation: Confirm authorization for the specific account and share, limit queries to its intended scope, and handle returned contact data as sensitive.

## Reference(s):

- [GraphQL operations reference](references/graphql-operations.md)
- [OneHome fpx ClawHub release](https://clawhub.ai/chrischall/skills/onehome-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return private listing and contact data when run with an authorized session.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
