## Description:

Guides an agent through Beatra workflows for creating and managing images, videos, music, narration, and reusable voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan, request, track, and retrieve Beatra-generated visual and audio media for creative projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media and generated outputs are shared with Beatra.

Mitigation: Use only media you are comfortable sharing with Beatra and review sensitive content before uploading.

Risk: Media generation and voice cloning can spend wallet credits.

Mitigation: Review live estimates and explicitly approve video or voice-clone requests before submission; check charges afterward.

Risk: Voice cloning can misuse another person's voice.

Mitigation: Clone voices only with the voice owner's explicit consent.

Risk: Automatic updates may change local code without a separate approval.

Mitigation: Disable automatic updates if each local code change requires review.

Risk: Removing the last Beatra skill may revoke the shared connection and delete local Beatra state.

Mitigation: Review the disconnect and uninstall behavior before removing the last Beatra skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/ai-video-image-music-studio)
- [Beatra skill homepage](https://beatra.ai/skills/ai-video-image-music-studio)
- [Images](references/images.md)
- [Videos](references/videos.md)
- [Music](references/music.md)
- [Speech and voices](references/speech-and-voices.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with media links and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task status, model details, media links, and credit usage returned by Beatra.]

## Skill Version(s):

0.2.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
