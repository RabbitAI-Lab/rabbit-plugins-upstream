## Description:

Host HTML/Markdown pages and share PDF, Word, or PowerPoint docs as ShareOne short links, with support for passwords, watermarks, comments, downloads, and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers, content authors, and agent users use this skill to publish generated pages, documents, or conversation text to ShareOne and manage the resulting links. It also supports updating existing shares, downloading share contents, managing comments, and changing share settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected files or conversation text to ShareOne, which can expose sensitive or unintended content.

Mitigation: Preview sensitive content before publishing, avoid uploading private data unless the user explicitly requests it, and use passwords or watermarks when appropriate.

Risk: The skill can store or print ShareOne API keys, which is risky in shared or logged environments.

Mitigation: Use trusted environments, redact API-key output from logs, prefer temporary keys when possible, and delete stored credentials when they are no longer needed.

Risk: Owner credentials can update, download, administer, or delete shares with limited confirmation.

Mitigation: Confirm destructive actions such as share deletion, keep credentials scoped to the intended account, and review high-impact share changes before execution.

Risk: Persistent page data can store shared visitor-readable data when explicitly enabled.

Mitigation: Enable persistent data storage only on explicit request, keep sensitive values in private browser storage, and avoid placing secrets in shared page data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beep879/skills/shareone)
- [ShareOne Service](https://shareone.app)
- [Persistent Page Data Example](templates/page-storage-dropzone.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands, plus script outputs such as JSON, status tokens, ShareOne URLs, and saved-file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use ShareOne API credentials and may upload, update, download, administer, or delete ShareOne shares depending on the user's request.]

## Skill Version(s):

1.2.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
