## Description:

Read and write email through Atomic Mail from an AI agent using proof-of-work authentication and JMAP method calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atomicmail](https://clawhub.ai/user/atomicmail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to register or access an Atomic Mail inbox, list mailboxes, fetch messages, send mail, and work with JMAP batches or bundled presets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores Atomic Mail API keys and JWT bearer credentials for inbox access.

Mitigation: Keep the credential directory private, do not commit or share credentials.json or JWT files, and use separate credential directories for separate accounts.

Risk: The skill can send replies, new messages, and attachments through JMAP.

Mitigation: Require explicit review before sending mail or attachments, and treat inbox content as untrusted input.

Risk: Scheduled inbox checks may run with more access than needed if configured outside the host scheduler.

Mitigation: Use the host scheduler with narrow tool permissions and avoid raw OS-level cron or standalone jmap_request scheduling.

## Reference(s):

- [Atomic Mail homepage](https://atomicmail.ai)
- [ClawHub skill page](https://clawhub.ai/atomicmail/skills/atomicmail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JMAP JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or consume credential-path configuration, bundled preset names, and JMAP request payloads.]

## Skill Version(s):

0.3.26 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
