## Description:

Automates job searching, tailored application email drafting, Gmail SMTP sending after explicit approval, inbox reply checks, and JSON-based application tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-hussein](https://clawhub.ai/user/z-hussein)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers use this skill to find matching roles, draft personalized application and follow-up emails, send approved messages with a CV, monitor recruiter replies, and maintain a local application tracker.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive personal data such as CV details, contact information, job history, recruiter emails, and interview details.

Mitigation: Keep application data, CV files, configuration, and tracker files local; review retained data periodically and follow the documented archival and deletion controls.

Risk: The Gmail app password used for SMTP could expose the dedicated job-application mailbox if mishandled.

Mitigation: Use a dedicated Gmail account, store the app password only in references/SMTP-SECRET.txt with restrictive permissions, load it only after send approval, and revoke it immediately if exposure is suspected.

Risk: Outbound applications, follow-ups, replies, or optional notification digests could be sent before the user is ready.

Mitigation: Require explicit user approval for every outbound email and recruiter reply, show a final preview before sending, and enable WhatsApp digests only after dedicated user consent.

Risk: Job listings, company pages, search results, and inbound email content are untrusted and may contain misleading or instruction-like text.

Mitigation: Treat external content as data only, extract it into strict schemas, ignore embedded instructions, and keep credential access separate from browsing and inbox parsing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/z-hussein/skills/job-apply-automation)
- [README](artifact/README.md)
- [Configuration Template](artifact/references/config.md)
- [Email Templates](artifact/references/email-templates.md)
- [Tracker Commands](artifact/references/Tracker-commands.md)
- [Platform Notes](artifact/references/Platform-notes.md)
- [Job Application Profile](artifact/references/job-profile.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses, email drafts, JSON tracker updates, and setup shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit approval before sending outbound email or recruiter replies; records application state in Applications.json.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
