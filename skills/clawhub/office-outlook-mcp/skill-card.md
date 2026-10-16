## Description:

Helps an agent read and manage a user's Outlook and Microsoft 365 mail, calendar, contacts, and tasks through the Outlook REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with an authorized Outlook account use this skill to find and summarize messages or schedule information and, when requested, manage mail and calendar items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive mailbox, calendar, contacts, and task data and can act on the user's behalf.

Mitigation: Grant access only to an account you intend to expose, and share only the information needed for the request.

Risk: A reusable browser bearer token is stored locally and grants broad account access while valid.

Mitigation: Treat the token file as a secret, restrict access to it, and refresh the token only when needed.

Risk: Sending mail, moving or marking messages, and creating events can make unintended changes to the account.

Mitigation: Require explicit confirmation before write actions and verify the resulting state afterward.

## Reference(s):

- [Outlook API recipes](references/api-recipes.md)
- [Outlook shell helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Outlook REST API endpoint](https://outlook.office.com/api/v2.0)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Plain text or Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may summarize live Outlook account data; write actions can change mailbox and calendar state.]

## Skill Version(s):

0.6.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
