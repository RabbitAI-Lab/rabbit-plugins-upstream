## Description:

Collect subtitles, captions, or transcript text for a known YouTube video ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify jobs for YouTube subtitle, caption, or transcript collection when they already know the target video ID. The skill can wait for the asynchronous task and return the collected result by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Dataify and may consume account credits when transcript collection is requested.

Mitigation: Install and run it only with a user-owned DATAIFY_API_TOKEN, and review the target video ID and scope before submission.

Risk: Implicit invocation is enabled, so ambiguous Dataify transcript requests could trigger a collection flow.

Mitigation: Ask for clarification when the target or intent is unclear, especially before submitting multiple video IDs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-transcript-by-id)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify API token login](https://dashboard.dataify.com/login?utm_source=skill)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with command examples and JSON task/result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-owned DATAIFY_API_TOKEN and a YouTube video ID; may wait for asynchronous task completion.]

## Skill Version(s):

1.3.0 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
