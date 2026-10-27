## Description:

Guides agents in delivering YouTube video, audio, or clips to user-controlled cloud storage through paid FlashData jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media teams use this skill to configure and submit authorized YouTube video or audio deliveries to their own cloud storage, then retrieve job status and file details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: FlashData receives an API key and cloud-storage credentials to upload media.

Mitigation: Keep secrets out of chat and logs; use short-lived credentials restricted to the intended bucket and prefix.

Risk: Download submissions consume paid FlashData Credits, and a timed-out submission may still have started.

Mitigation: Confirm the destination and budget before submitting; check the existing job or console instead of automatically retrying.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-download-flashdata)
- [FlashData YouTube download documentation](https://flashdata.dev/docs/sources/youtube_download?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-task)
- [FlashData MCP](https://flashdata.dev/mcp)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Storage configuration](references/storage.md)
- [Download request schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Text]

**Output Format:** [Markdown with Python examples and JSON job summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous jobs return a job ID; completed jobs identify media uploaded to the user's cloud storage.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
