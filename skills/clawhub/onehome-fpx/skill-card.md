## Description:

Query OneHome, the CoreLogic real-estate portal, from a shell with the fpx CLI to resolve consumer scopes, search shared listings, and read listing details through an authorized signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate workflow operators use this skill to generate shell-based fpx setup, authentication, GraphQL, REST, and jq workflows for authorized OneHome shares without running the OneHome MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles live OneHome bearer tokens and magic-link tokens.

Mitigation: Use only authorized OneHome accounts or shares, avoid shared or recorded terminals, do not paste or log tokens, and remove temporary token files immediately.

Risk: The workflow can expose private real-estate portal data from signed-in sessions.

Mitigation: Run it only in trusted environments and limit requests, storage, and sharing to data the user is authorized to access.

Risk: The security summary notes weak guardrails around token and portal-data handling.

Mitigation: Prefer a pinned and reviewed fpx version and review generated commands before execution.

## Reference(s):

- [OneHome GraphQL + REST operations for fpx](references/graphql-operations.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, GraphQL, JSON, and jq snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup commands, bearer-token capture or exchange flows, request bodies, endpoint guidance, and response-checking examples.]

## Skill Version(s):

0.15.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
