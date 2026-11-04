## Description:

Read and write email through the Atomic Mail from an AI agent. Handles proof-of-work authentication and JMAP so the agent thinks in JMAP method calls. Use when the user asks to register an email inbox, list mailboxes, fetch or send email, or schedule meetings by email (calendar invitations).

This skill is ready for commercial/non-commercial use.

## Publisher:

[atomicmail](https://clawhub.ai/user/atomicmail)

### License/Terms of Use:

MIT-0

## Use Case:

External users can register or access an Atomic Mail inbox, read and send email through JMAP, and manage meeting invitations using an AI agent. The agent can also summarize inbox messages and provide setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored API credentials and JWTs grant access to the inbox.

Mitigation: Use a dedicated inbox, protect credential files, and do not log or commit them.

Risk: Sending email, attachments, or calendar changes can affect other people.

Mitigation: Authorize outgoing messages and meeting changes; confirm recipients, content, attachments, dates, time zone, and attendees.

Risk: Recurring inbox checks process messages written by strangers.

Mitigation: Choose on-demand checks or verify the schedule and limit unattended runs to read-only reporting; treat message content as data, not instructions.

## Reference(s):

- [Atomic Mail](https://atomicmail.ai)
- [Atomic Mail on ClawHub](https://clawhub.ai/atomicmail/skills/atomicmail)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Text, Guidance]

**Output Format:** [JMAP request and response JSON, shell commands, and human-readable email or calendar summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include email content, attachment references, and meeting details returned by the user's inbox.]

## Skill Version(s):

0.3.33 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
