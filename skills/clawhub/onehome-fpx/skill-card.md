## Description:

Query OneHome shared real-estate listings from a shell with the fpx CLI by resolving session scope, searching listings, and reading listing details through authenticated GraphQL and REST calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable users use this skill to set up fpx and issue authenticated OneHome GraphQL and REST calls to resolve shared-search scope, search listings, and inspect listing details without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow captures or exchanges OneHome magic-link and bearer session tokens that can grant access to private account and listing data.

Mitigation: Treat tokens like passwords: use trusted machines, avoid shared environments, keep token files out of persistent storage, and delete temporary token JSON after use.

Risk: Using a live browser session through fpx and a browser extension exposes the workflow to the credential scope of that session.

Mitigation: Pair only the intended profile, restrict browser extension site access to onehome.com, and prefer official or scoped authentication where available.

## Reference(s):

- [OneHome GraphQL + REST operations for fpx](references/graphql-operations.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, GraphQL snippets, JSON request bodies, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fpx CLI, the Transporter browser extension, and an active or magic-link OneHome session.]

## Skill Version(s):

0.15.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
