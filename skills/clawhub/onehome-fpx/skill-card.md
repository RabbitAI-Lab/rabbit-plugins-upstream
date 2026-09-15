## Description:

Query OneHome, the CoreLogic real-estate portal at portal.onehome.com, from a shell with the fpx CLI instead of running the onehome-mcp server, including saved-search scope resolution, shared-listing search, and listing-detail reads through one-shot GraphQL calls routed through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with authorized OneHome access use this skill to configure fpx, obtain a session bearer, and run targeted GraphQL or REST calls for saved searches, listings, listing details, photos, and LocalLogic data without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles OneHome account and session credentials, including bearer tokens, email magic-link tokens, share tokens, and contact data.

Mitigation: Use it only for your own OneHome share or another clearly authorized workflow, avoid saving tokens or full API responses to disk, and treat captured tokens and contact data as secrets.

Risk: The workflow can access broad private listing and contact data through reused session credentials.

Mitigation: Review generated commands before execution, keep browser and fpx access scoped to the intended OneHome share, and discard captured credentials after use.

## Reference(s):

- [OneHome GraphQL and REST operations for fpx](references/graphql-operations.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell, JSON, and GraphQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes command templates that may return JSON API responses when executed.]

## Skill Version(s):

0.15.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
