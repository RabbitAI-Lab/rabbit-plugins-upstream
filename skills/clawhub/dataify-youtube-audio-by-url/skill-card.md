## Description:

Download or collect a YouTube audio file from a known video URL. Do not use for video files, metadata, comments, transcripts, or video discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder jobs that collect YouTube audio from known video URLs, monitor the asynchronous task, and return final collected results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan notes a mismatch between the advertised audio-only scope and subtitle-related options.

Mitigation: Review requested task options before execution and treat subtitle settings as outside the advertised audio-only scope unless the publisher clarifies or removes them.

Risk: The skill sends YouTube URLs and task options to Dataify under the user's API TOKEN.

Mitigation: Use the skill only when sharing those URLs and options with Dataify is acceptable, and keep DATAIFY_API_TOKEN out of chat and logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-audio-by-url)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON task or result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task_id, status, normalized request parameters, and summarized final results.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
