## Description:

Collect YouTube comments for a known video ID, with explicit exclusions for video metadata, transcripts, media downloads, and keyword discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify jobs that collect YouTube comments for one or more known video IDs, then monitor the task and return the collected result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a saved Dataify API TOKEN to submit external collection jobs and retrieve results.

Mitigation: Install only where saved credentials are appropriate, keep DATAIFY_API_TOKEN scoped to the intended user, and review requests before broad or multi-video collection.

Risk: Collection jobs may consume Dataify credits or create cost exposure when run at large scope.

Mitigation: Confirm comment counts, multi-video requests, and credit implications before high-volume use.

Risk: The skill is intended for YouTube comments by known video ID, not media downloads or unrelated YouTube data tasks.

Mitigation: Use it only for the documented comment collection workflow and choose another tool for video metadata, transcripts, keyword discovery, or media downloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-youtube-comment-by-id)
- [Dataify Dashboard Login](https://dashboard.dataify.com/login?utm_source=skill)
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance, shell commands, and JSON task or result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns final collected results by default; returns a task ID and resume command when monitoring times out or no-wait behavior is requested.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
