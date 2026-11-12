## Description:

Creates AI images, videos, music, and speech, edits supported media, and retrieves public social data through Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use the skill to generate and edit media, synthesize narration or reusable voices, and retrieve public social posts, comments, account details, or trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports recurring installation and environment analytics, possible collection beyond media functions, and no described consent or opt-out mechanism.

Mitigation: Review what installation and environment information is reported and decide whether that collection is acceptable before connecting the skill.

Risk: Media or text may be sent to an external service, while the security guidance notes missing privacy notices.

Mitigation: Review the applicable privacy terms before sending sensitive media or text, and share only content appropriate for the service.

Risk: The security review is incomplete and calls out update instructions and a possible uninstall issue for review.

Mitigation: Review the update and uninstall behavior before use, and check the uninstall decision and resulting cleanup when disconnecting.

Risk: Voice cloning uses a person's voice sample to create a reusable voice.

Mitigation: Require explicit confirmation that the user owns the voice or has the voice owner's permission before uploading a sample or creating a clone.

## Reference(s):

- [Image generation and editing](artifact/references/images.md)
- [Video generation and editing](artifact/references/videos.md)
- [Music generation](artifact/references/music.md)
- [Speech and voice cloning](artifact/references/speech-and-voices.md)
- [Public social data](artifact/references/social.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Updates and security](artifact/references/updates-and-security.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [Beatra installation page](https://beatra.ai/install)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, Text, JSON]

**Output Format:** [Media files, text, or JSON, according to the requested task]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media dimensions, duration, format, and size depend on the completed task and selected model.]

## Skill Version(s):

3.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
