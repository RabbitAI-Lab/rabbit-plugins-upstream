## Description:

Read and write email through the Atomic Mail from an AI agent. Handles proof-of-work authentication and JMAP so the agent thinks in JMAP method calls. Use when the user asks to register an email inbox, list mailboxes, fetch or send email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atomicmail](https://clawhub.ai/user/atomicmail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to register Atomic Mail inboxes, read mailboxes, fetch messages, and send email through JMAP from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access an Atomic Mail account and stores API key and JWT credential files locally.

Mitigation: Install only when that account access is acceptable, protect the credential directory, avoid logging bearer tokens, rotate credentials when needed, and remove stale credentials when the skill is no longer used.

Risk: Scheduled inbox checks can run unattended and read mail from external senders.

Mitigation: Prefer on-demand checks or configure scheduled runs with a dedicated read-only Atomic Mail tool and without broad shell, file-write, scheduler-management, browser, or delegation tools.

Risk: A recurring inbox job may persist after it is no longer needed.

Mitigation: Review and remove any created recurring job when the workflow is retired.

## Reference(s):

- [Atomic Mail homepage](https://atomicmail.ai)
- [ClawHub Atomic Mail skill page](https://clawhub.ai/atomicmail/skills/atomicmail)
- [ClawHub publisher profile](https://clawhub.ai/user/atomicmail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON JMAP request or response content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local Atomic Mail credential and JWT files during registration, and may use bundled JMAP preset JSON files for inbox, send, reply, and attachment workflows.]

## Skill Version(s):

0.3.27 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
