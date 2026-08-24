## Description:

MyBooks lets an agent manage a personal MyBooks library, including search, metadata updates, reading status, notes import, uploads, device delivery, and MiMo TTS audiobook workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[poxenstudio](https://clawhub.ai/user/poxenstudio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to operate a MyBooks personal library server: finding books, editing metadata, managing reading state, importing annotations, uploading books, sending books to devices, and running supported TTS audiobook tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authenticates to a MyBooks server and can expose credentials if they are stored in shared configuration.

Mitigation: Provide credentials through session-level environment variables or a secret manager, and avoid writing them to shared or global config files.

Risk: The skill can upload, download, and modify library records using local file paths and server API calls.

Mitigation: Pass only the specific ebook, audio, or output paths needed for the requested action, and confirm intended library changes before mutation-heavy operations.

Risk: Disabling SSL verification can weaken transport protections outside a trusted local or self-signed deployment.

Mitigation: Keep SSL verification enabled unless connecting to a trusted self-signed local deployment.

## Reference(s):

- [MyBooks Homepage](https://www.mybooks.top)
- [ClawHub MyBooks Skill Page](https://clawhub.ai/poxenstudio/skills/mybooks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 plus MYBOOKS_HOST, MYBOOKS_USER, and MYBOOKS_PASSWORD; MYBOOKS_SSL_VERIFY is optional for trusted self-signed local deployments.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
