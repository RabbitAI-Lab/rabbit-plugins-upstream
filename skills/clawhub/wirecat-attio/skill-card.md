## Description:

Use attio to read an Attio workspace's CRM - deals with their stage, owner, amount, company and people, the deal pipeline and its stages, people, companies, workspace members and the workspace's own attributes - with the owner's profile and JSON answers; deals are synced into the local WireCat store. Use when a question could be answered from the owner's Attio sales data (how a deal stands, what is open, who a client is, what changed), or to call an Attio API operation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Attio workspace owners and their authorized agents use this skill to answer questions from CRM records, inspect workspace data, and call Attio API operations when requested. It can also create or change CRM records, so write actions should be reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and delete operations can change or remove records in the owner's live Attio workspace.

Mitigation: Review the exact operation and target first, run writes with --dry-run, and execute only when the owner has authorized the change.

Risk: Attio access tokens grant access to workspace data and may include write permissions.

Mitigation: Have the owner sign in through their own terminal, never request or expose the token, and grant only the scopes needed for the requested operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wirecat/skills/wirecat-attio)
- [Attio API command reference](artifact/references/api.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, API Calls]

**Output Format:** [Concise text with JSON command responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may reflect locally synced CRM data or live Attio reads; sync completeness and freshness affect local-store results.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
