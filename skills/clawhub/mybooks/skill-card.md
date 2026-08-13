## Description:

MyBooks helps an agent manage a personal book library, including library and reading statistics, book search and metadata updates, email or device delivery, book uploads, reading status, third-party annotation imports, and MiMo TTS audiobook workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[poxenstudio](https://clawhub.ai/user/poxenstudio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a MyBooks server on their behalf for personal library management, metadata maintenance, reading workflows, book delivery, annotation import, and audiobook generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authenticates to a MyBooks server and can act with the permissions of the supplied account.

Mitigation: Use session-scoped credentials, avoid shared configuration files for secrets, and provide an account with only the permissions needed for the task.

Risk: The skill can modify library records, upload books, import annotations, and clear imported annotations.

Mitigation: Review proposed changes before write operations and use dry-run preview flows for annotation imports before committing them.

Risk: Book delivery, TTS conversion, and voice cloning can share book text, API keys, email or device targets, and voice samples with configured services.

Mitigation: Use HTTPS with certificate verification, confirm email and device recipients, and only configure TTS or cloning services that are trusted for the content being processed.

## Reference(s):

- [ClawHub MyBooks Skill Page](https://clawhub.ai/poxenstudio/skills/mybooks)
- [MyBooks Homepage](https://www.mybooks.top)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and MYBOOKS_HOST, MYBOOKS_USER, and MYBOOKS_PASSWORD environment variables.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
