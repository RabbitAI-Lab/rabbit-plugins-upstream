## Description:

Query OneHome (CoreLogic), the agent magic-link real-estate portal at portal.onehome.com, from a shell with the fpx CLI instead of running the onehome-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data operators use this skill to obtain concise shell-based guidance for resolving OneHome consumer scopes, querying shared listings, and reading listing details through authorized OneHome sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides users to extract and reuse live OneHome session credentials from magic links or browser tabs.

Mitigation: Use it only with accounts and listings you are authorized to access, avoid shared machines, and treat all tokens and outputs as private credentials and data.

Risk: Temporary files and shell variables shown in the workflow may contain bearer tokens, session responses, query bodies, or real-estate listing data.

Mitigation: Delete temporary files after use, avoid command histories or shared terminals that expose credentials, and rotate or refresh sessions if a token may have been disclosed.

Risk: OneHome responses may include consumer, agent, listing, contact, or MLS-scoped information.

Mitigation: Confirm authorization before querying, prefer the consumer-readable saved-search path unless an agent session is intended, and review outputs before sharing them outside the authorized context.

## Reference(s):

- [OneHome GraphQL + REST operations for fpx](artifact/references/graphql-operations.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell, JSON, and GraphQL snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized OneHome access, fpx CLI, Transporter browser extension, and jq; examples may create temporary files containing credentials or query bodies.]

## Skill Version(s):

0.15.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
