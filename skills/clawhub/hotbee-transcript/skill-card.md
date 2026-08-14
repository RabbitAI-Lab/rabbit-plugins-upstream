## Description:

Converts user-provided audio or video URLs into text through HotBee speechToText, including file URL transcription, video URL transcription, and transcript extraction from parsed social videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request HotBee transcription for media URLs when they have a HotBee API key and authorization to process the media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media URLs and accessible media content are sent to HotBee for transcription.

Mitigation: Confirm the user is comfortable sending the media to HotBee and only process media the user owns, is authorized to process, or can lawfully access.

Risk: Private signed URLs or API credentials could be exposed if echoed in logs or errors.

Mitigation: Keep HOTBEE_API_KEY in the local environment and avoid printing API keys or private signed media query parameters.

Risk: Live transcription calls may consume HotBee quota.

Mitigation: Confirm intent before a live call unless the user has already approved it.

## Reference(s):

- [Speech To Text API](references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [HotBee transcript ClawHub page](https://clawhub.ai/shanye1402-hash/skills/hotbee-transcript)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and transcribed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses HOTBEE_API_KEY from the local environment and sends authorized media URLs to HotBee.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
