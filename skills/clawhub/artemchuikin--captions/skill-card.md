## Description:

Extracts timestamped closed captions from public YouTube videos through TranscriptOut, returning JSON, text, SRT, VTT, or SRV3 formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, accessibility workflows, content reviewers, and language learners use this skill to retrieve YouTube captions for reading, quoting, translating, review, or export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can involve email sign-in codes, API keys, temporary token files, and persistent credential storage.

Mitigation: Prefer creating the key in the official TranscriptOut dashboard, store it in a scoped secret manager or approved environment-secret mechanism, and delete temporary token files after setup.

Risk: Transcript requests send YouTube video identifiers and selected request options to TranscriptOut and may spend account credits.

Mitigation: Confirm the requested video, language, format, and need for metadata before making calls, and avoid bulk transcript retrieval unless the user explicitly asks for it.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API key setup](references/auth-setup.md)
- [Captions on ClawHub](https://clawhub.ai/artemchuikin/skills/captions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands and TranscriptOut responses as JSON, plain text, SRT, VTT, or SRV3.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and network access to api.transcriptout.com; transcript requests consume TranscriptOut credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
