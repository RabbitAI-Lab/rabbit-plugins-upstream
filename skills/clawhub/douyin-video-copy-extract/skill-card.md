## Description:

Extracts Douyin video details, original descriptions, and spoken-word transcripts from video links, share text, or aweme IDs using SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People working with Douyin videos use this skill to obtain the video's description and spoken transcript as readable, copyable text, or to check an existing transcription job.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended command executes an unpinned npm package while an API key is available in the environment.

Mitigation: Run it only if you trust SocialDataX and the npm resolution path; prefer a pinned, reviewed package version or a managed MCP tool, and provide the API key only in an approved environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-video-copy-extract)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes video details, original description, transcript, copyable and concise versions, and job status; pending jobs include a job ID and continuation command.]

## Skill Version(s):

0.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
