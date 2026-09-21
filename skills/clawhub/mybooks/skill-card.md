## Description:

MyBooks helps an agent manage a personal book library by searching and browsing books, viewing statistics, editing metadata, managing reading state and notes, uploading books, and using MiMo TTS audiobook features through a user-configured MyBooks server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[poxenstudio](https://clawhub.ai/user/poxenstudio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate their own MyBooks library from an agent session, including catalog search, metadata updates, reading progress management, note import, book upload, and TTS audiobook workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses MyBooks credentials and can mutate library data on the configured server.

Mitigation: Install only for trusted MyBooks servers, pass credentials through session-scoped environment variables or a dedicated secret manager, and review mutating actions before execution.

Risk: TTS workflows may send book text, voice samples, or TTS provider credentials through the configured MyBooks server to the selected TTS service.

Mitigation: Use TTS only with trusted servers and providers, avoid real API keys in shared shells or logs, and avoid converting sensitive books or voice samples unless the transfer is acceptable.

Risk: Book and voice-sample upload tools can read local files explicitly named by the user and upload them to MYBOOKS_HOST.

Mitigation: Upload only user-approved ebook, MP3, or WAV paths and confirm the destination host before sending files.

Risk: Plain HTTP can expose credentials or content unless restricted to local or private networks.

Mitigation: Use HTTPS for public hosts; keep plain HTTP limited to localhost or LAN unless the user knowingly enables the documented override.

## Reference(s):

- [MyBooks homepage](https://www.mybooks.top)
- [ClawHub skill page](https://clawhub.ai/poxenstudio/skills/mybooks)
- [ClawHub publisher profile](https://clawhub.ai/user/poxenstudio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 plus MYBOOKS_HOST, MYBOOKS_USER, and MYBOOKS_PASSWORD environment variables.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
