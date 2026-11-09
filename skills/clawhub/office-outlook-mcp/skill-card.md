## Description:

Read and manage a user's Outlook mailbox, folders, calendar, contacts, and tasks through Microsoft 365.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Microsoft 365 mailbox users can ask an agent to find messages, check schedules, review contacts or tasks, and carry out supported mailbox or calendar changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated mailbox requests could send a bearer token to an unintended destination; the security analysis is partial and medium-confidence.

Mitigation: Before installing, consider the mailbox-credential risk and restrict request options and destinations to approved Outlook endpoints.

## Reference(s):

- [Outlook API recipes](references/api-recipes.md)
- [Outlook access helper](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Outlook REST API endpoint](https://outlook.office.com/api/v2.0)

## Skill Output:

**Output Type(s):** [Text, JSON, API calls]

**Output Format:** [Mailbox data and concise natural-language responses; API results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain private mailbox content and may create or modify messages, events, and tasks when requested.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
