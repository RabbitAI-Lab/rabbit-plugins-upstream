## Description:

Converts user-provided audio or video URLs into text transcripts through HotBee speechToText.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe audio or video available at a URL, including file URLs, video URLs, or media URLs extracted from parsed social videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media URLs and the HotBee API key are sent to HotBee for speech-to-text processing.

Mitigation: Use the skill only when the user is comfortable sending the media URL and API key to HotBee.

Risk: Live transcription calls may consume HotBee quota.

Mitigation: Confirm quota use before live calls.

Risk: Signed or private media URLs with sensitive query parameters may appear in local command output or logs.

Mitigation: Avoid signed or private media URLs unless the user accepts that exposure.

## Reference(s):

- [Speech To Text API](artifact/references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [HotBee speechToText endpoint](https://www.smsz.xyz/prod-api/tool/speech/speechToText)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and transcript text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided media URLs and the local HOTBEE_API_KEY environment variable.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
