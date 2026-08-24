## Description:

Create AI images, videos, music, and speech; edit visual results; look up public social data; and manage generated Beatra assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to generate or edit media, synthesize speech, create reusable voices with consent, retrieve public social data, and track task results and credit usage through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package checks for and may apply verified updates by default before ordinary commands.

Mitigation: Review this behavior before deployment and disable silent updates with `python3 scripts/mcp_client.py update --auto off` where controlled change management is required.

Risk: The package keeps a private shared token and installation metadata under ~/.beatra.

Mitigation: Install only on hosts where this shared local credential model is acceptable, and revoke access from the Beatra Console or use the bundled uninstall flow when removing the skill.

Risk: Voice cloning can be misused if the user does not have the voice owner's permission.

Mitigation: Require explicit confirmation that the user owns the voice or has the owner's permission before uploading a sample or calling the voice-clone tool.

Risk: Billable media generation, voice cloning, video prompt enhancement, and public social execution consume Beatra credits.

Mitigation: Keep the paid boundary clear, show required admission details for video and voice cloning, submit each finalized paid request once, and recover with the same request identity when transport is uncertain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/beatra)
- [Beatra install page](https://beatra.ai/install)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Images](references/images.md)
- [Videos](references/videos.md)
- [Video controls](references/video-controls.md)
- [Video recipes](references/video-recipes.md)
- [Music](references/music.md)
- [Speech and voices](references/speech-and-voices.md)
- [Public social data](references/social.md)
- [Uploads](references/uploads.md)
- [Models](references/models.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, artifact links, public social JSON, resolved model details, and credit usage when remote tasks complete.]

## Skill Version(s):

2.7.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
