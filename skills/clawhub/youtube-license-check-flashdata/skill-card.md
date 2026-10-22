## Description:

Checks a YouTube video's Creative Commons license classification through FlashData for use in a separate rights review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and rights reviewers use this skill to record a YouTube video's license-label classification and interpret it without treating the label as permission to train on or reuse the video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send selected video IDs and an API key to FlashData.

Mitigation: Use only for authorized queries and keep the key in protected environment settings, not prompts or files.

Risk: Data queries consume paid FlashData Credits, including potentially timed-out submissions.

Mitigation: Set a budget, check pricing first, and check the existing job before retrying a timed-out request.

Risk: A Creative Commons label may be mistaken for training or reuse permission.

Mitigation: Treat the label as one observation and independently review the license and intended use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/rocosen/skills/youtube-license-check-flashdata)
- [FlashData youtube_trainability documentation](https://flashdata.dev/docs/sources/youtube_trainability?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-task)
- [Sample query](artifact/references/query.json)
- [Query schema](artifact/references/schema.json)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON classification or concise Markdown explanation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Record the video ID and retrieval time with the raw classification; no reuse rights are verified.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
