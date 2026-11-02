## Description:

Read and manage a user's Outlook and Microsoft 365 email, folders, calendar, contacts, and tasks using their signed-in Outlook session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to read and manage Outlook and Microsoft 365 mail, folders, calendar events, contacts, and tasks through the user's paired Outlook account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A saved browser bearer token is used by requests that do not restrict destinations or mailbox changes.

Mitigation: Require explicit approval for mailbox changes, restrict authenticated requests to approved Microsoft HTTPS destinations, and remove the saved token and revoke browser pairing when finished.

## Reference(s):

- [Outlook API recipes](references/api-recipes.md)
- [Outlook environment setup](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/office-outlook-mcp)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Text]

**Output Format:** [Markdown instructions, shell commands, Outlook API data, and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Handles user-specific mailbox data; mailbox changes require explicit approval.]

## Skill Version(s):

0.7.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
