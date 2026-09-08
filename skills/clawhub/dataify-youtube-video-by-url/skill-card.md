## Description:

Download or collect a YouTube video media file from a known video URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to submit Dataify YouTube video collection jobs for known YouTube video URLs, monitor the resulting task, and return the final collected result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit token-authenticated remote Dataify collection jobs for YouTube media.

Mitigation: Use it only when you are comfortable sending the target YouTube URLs to Dataify under your account, and confirm each media collection job before submission.

Risk: Waiting for media collection can consume credits, bandwidth, and time.

Mitigation: Review expected cost and scope before running; use no-wait behavior when only a task ID is needed.

Risk: A saved API TOKEN enables future submissions from the local environment.

Mitigation: Store the token only with user confirmation and never print or expose its value.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-video-by-url)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify account login](https://dashboard.dataify.com/login?utm_source=skill)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task/result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Dataify API TOKEN and may submit token-authenticated remote collection jobs.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
