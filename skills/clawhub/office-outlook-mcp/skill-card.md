## Description:

Helps an agent read and manage a user's Outlook and Microsoft 365 mail, calendar, contacts, and tasks using a bearer token from their signed-in browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Outlook users and their agents can review messages, folders, meetings, contacts, and tasks, and make requested mailbox or calendar changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser-derived bearer token gives the agent broad access to read and modify the user's real Outlook account, with limited built-in scoping or confirmation.

Mitigation: Keep activity narrowly tied to the user's request and review commands before sending, moving, or editing mail or creating events.

Risk: A stored bearer token can continue to provide access after the immediate task.

Mitigation: Remove ~/.outlook-fpx/curlrc or revoke the session when finished.

## Reference(s):

- [Outlook API request recipes](artifact/references/api-recipes.md)
- [Outlook access helpers](artifact/references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown, with shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include requested Outlook account content; limit disclosure to the user's request.]

## Skill Version(s):

0.6.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
