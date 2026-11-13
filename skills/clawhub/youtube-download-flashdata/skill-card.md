## Description:

Download YouTube video, audio or a clip to your cloud storage with FlashData. Use for YouTube-to-S3 delivery, MP4 or MP3 exports and media ingestion through asynchronous jobs. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media teams use this skill to request YouTube video, audio, or clip downloads and deliver the resulting files to storage they control. It also provides setup and job-status guidance for these asynchronous deliveries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storage credentials are sent to FlashData for uploads and may appear in MCP tool history.

Mitigation: Use narrowly scoped credentials, keep them in a private secret file, and do not expose them in prompts, logs, or returned summaries.

Risk: A timed-out paid submission may already have been charged, so its outcome can be unknown.

Mitigation: Check the returned job or FlashData Jobs before considering another submission; do not retry automatically.

Risk: The security analysis was partial and could not resolve three local path references.

Mitigation: Review the unresolved references and skill behavior before installation.

## Reference(s):

- [FlashData YouTube download documentation](https://flashdata.dev/docs/sources/youtube_download)
- [Storage setup](references/storage.md)
- [FlashData MCP](https://flashdata.dev/mcp)
- [FlashData pricing](https://flashdata.dev/pricing)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with Python examples, shell commands, configuration guidance, and JSON job details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous delivery instructions; job status and storage manifest details depend on the submitted request.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
