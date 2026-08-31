## Description:

MyBooks lets an agent work with a user's MyBooks personal library to search and manage books, metadata, reading status, per-format reading progress, delivery, uploads, third-party annotations, and MiMo TTS audiobook workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[poxenstudio](https://clawhub.ai/user/poxenstudio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and readers use this skill to let an agent operate a self-hosted MyBooks library: querying catalog and reading stats, editing metadata, sending or uploading books, importing annotations, and managing TTS audiobook tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses MyBooks credentials and session cookies to access a personal library.

Mitigation: Use session-scoped environment variables or a dedicated secret manager, and avoid placing MYBOOKS_USER or MYBOOKS_PASSWORD in shared or global environment files.

Risk: Disabling TLS verification can expose credentials and library data when the MyBooks host is not local or otherwise trusted.

Mitigation: Keep TLS verification enabled for non-local hosts and disable it only for trusted self-signed deployments.

Risk: Book text, ebook files, annotations, TTS API keys, and voice samples can contain sensitive personal or licensed content.

Mitigation: Confirm upload, delivery, annotation import, and TTS destinations before use, and treat book files, extracted text, voice samples, and provider keys as sensitive data.

Risk: Metadata edits, reading-progress updates, note imports, and note-clearing operations can change the user's MyBooks library state.

Mitigation: Preview or query existing records first where supported, confirm user intent for write operations, and use dry-run flows for annotation imports before committing changes.

## Reference(s):

- [MyBooks homepage](https://www.mybooks.top)
- [ClawHub MyBooks skill page](https://clawhub.ai/poxenstudio/skills/mybooks)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and the MYBOOKS_HOST, MYBOOKS_USER, and MYBOOKS_PASSWORD environment variables.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
