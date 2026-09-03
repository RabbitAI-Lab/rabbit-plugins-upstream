## Description:

Generate AI video, images, music, and voice-over in one connected creative flow, edit visual results, and keep every finished piece easy to find.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, educators, and media teams use this skill to create and manage Beatra-generated images, videos, music, speech, reusable voices, uploads, model choices, and asynchronous task results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a broad Beatra device token locally.

Mitigation: Install only if comfortable connecting a Beatra account, keep the credential private, and use the documented uninstall or disconnect flow when removing access.

Risk: Installed package code may silently self-update by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when a fixed installed version is required.

Risk: Billable media generation consumes Beatra credits.

Mitigation: Use the skill's confirmation and estimate steps before video or voice-clone calls, and retry balance recovery only with the same request identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-video-image-music-studio)
- [Beatra skill homepage](https://beatra.ai/skills/ai-video-image-music-studio)
- [Images](references/images.md)
- [Videos](references/videos.md)
- [Video controls](references/video-controls.md)
- [Video recipes](references/video-recipes.md)
- [Music](references/music.md)
- [Speech and voices](references/speech-and-voices.md)
- [Uploads](references/uploads.md)
- [Models](references/models.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text responses with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns task IDs, artifact links, usage, and billing details when Beatra completes generation.]

## Skill Version(s):

0.1.8 (source: evidence.release.version and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
