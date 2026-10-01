## Description:

Helps agents access Artsonia student-art portfolios, comments, fans, and notifications through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Artsonia account holders use this skill to ask an agent about linked students' artwork, activity, comments, and fans, and to request artwork downloads or confirmed updates to comments, fan invitations, and notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artsonia credentials and a cached session cookie could expose account access if shared.

Mitigation: Protect the MCP environment configuration and session files; use an account you are comfortable granting this access to.

Risk: Artwork downloads and metadata may include private student content and be stored locally.

Mitigation: Choose download destinations carefully, protect downloaded files, and exclude private artwork when it is not needed.

Risk: Posting comments, inviting fans, or changing notifications can modify the account.

Mitigation: Keep the default ask-user confirmation mode and review each preview before approving a write.

## Reference(s):

- [ClawHub artsonia-mcp release](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Shell commands, Files]

**Output Format:** [Markdown guidance with JSON configuration and shell examples; MCP tool results include artwork information and optional downloaded files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloads can include images, an optional JSON index and metadata sidecars; inline results report omissions when the 10 MiB cap is reached.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
