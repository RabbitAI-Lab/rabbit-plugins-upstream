## Description:

Use attio to read an Attio workspace's CRM - deals with their stage, owner, amount, company and people, the deal pipeline and its stages, people, companies, workspace members and the workspace's own attributes - with the owner's profile and JSON answers; deals are synced into the local WireCat store. Use when a question could be answered from the owner's Attio sales data (how a deal stands, what is open, who a client is, what changed), or to call an Attio API operation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

CRM owners and operators use the skill to answer questions from an Attio workspace and to carry out requested CRM operations with the attio command line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security scan coverage was partial, with one local path-like reference unresolved.

Mitigation: Review the skill's referenced files and command guidance before granting it access to a workspace.

Risk: The skill can use an access token and its API operations include deletion and other changes to real CRM records.

Mitigation: Keep the token private, grant only needed scopes, and review dry-run details before confirming writes.

## Reference(s):

- [Attio API operation reference](artifact/references/api.md)
- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-attio)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Text and JSON answers with attio CLI command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe or perform CRM reads and requested writes; writes can affect real records.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
