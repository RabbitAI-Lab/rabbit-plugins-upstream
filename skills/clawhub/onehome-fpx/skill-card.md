## Description:

Query OneHome, the CoreLogic real-estate portal at portal.onehome.com, from a shell with the fpx CLI to resolve authorized saved-search scope, search shared listings, and read listing detail through one-shot GraphQL calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with authorized OneHome access use this skill to query saved searches, shared listings, listing detail, listing photos, and LocalLogic data from a shell without running the onehome-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusable OneHome session credentials may be exposed through the fpx browser bridge, shell workflows, or temporary files.

Mitigation: Use only authorized accounts and magic links, avoid shared machines, do not save or share tokens or outputs, and delete /tmp files containing tokens or account data.

Risk: The fpx CLI and Transporter browser extension require access to OneHome session credentials.

Mitigation: Pin and review the CLI package before use, and remove the fpx capture profile or pairing when finished.

## Reference(s):

- [OneHome GraphQL + REST operations for fpx](references/graphql-operations.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command examples and JSON/GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized OneHome session context and fpx/Transporter pairing.]

## Skill Version(s):

0.15.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
