## Description:

Helps agents deliver authorized YouTube videos, audio, or clips to user-controlled cloud storage through paid FlashData jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media teams use this skill to request authorized YouTube media exports, choose formats or clip bounds, and retrieve the uploaded file location from their own cloud storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: FlashData receives the API key and destination storage credentials to upload media.

Mitigation: Use a scoped API key and narrowly scoped, preferably temporary, write-only storage credentials; keep secrets and signed URLs out of chat and logs.

Risk: Download requests consume paid Credits and may involve media without download rights.

Mitigation: Confirm the user's authorization and expected cost before submitting a job; do not automatically resubmit a timed-out request.

## Reference(s):

- [FlashData YouTube download documentation](https://flashdata.dev/docs/sources/youtube_download?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-task)
- [Storage setup](references/storage.md)
- [ClawHub skill listing](https://clawhub.ai/rocosen/skills/youtube-download-flashdata)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and job-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A completed job can provide a cloud-storage file location, size, and optional metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
