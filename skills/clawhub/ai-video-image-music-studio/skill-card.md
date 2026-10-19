## Description:

Helps agents create and manage AI-generated images, video, music, narration, and consent-gated custom voices through Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to turn briefs and source media into images, videos, songs, voice-overs, and reusable voices, then track and retrieve the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installed package may silently replace its files through automatic updates.

Mitigation: Review this behavior before installation; disable silent updates with `python3 scripts/mcp_client.py update --auto off` and check manually when preferred.

Risk: Selected local media is uploaded to Beatra for processing.

Mitigation: Upload only media you are comfortable sharing with Beatra; obtain explicit voice-owner consent before uploading a cloning sample.

Risk: The package manages a shared local Beatra device credential.

Mitigation: Protect the local credential and do not expose it in prompts, logs, or shared files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/ai-video-image-music-studio)
- [Images](references/images.md)
- [Videos](references/videos.md)
- [Music](references/music.md)
- [Speech and voices](references/speech-and-voices.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Media asset links]

**Output Format:** [Markdown with task status, result links or IDs, and usage details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media generation is asynchronous and may consume credits; report only returned results.]

## Skill Version(s):

0.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
