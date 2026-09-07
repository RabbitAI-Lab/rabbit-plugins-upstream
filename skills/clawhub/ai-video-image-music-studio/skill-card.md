## Description:

Generate AI video, images, music, and voice-over in one connected creative flow, edit visual results, and keep everything you make easy to find.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, educators, and developers use this skill to create and manage AI-generated images, videos, music, speech, and reusable voice assets through Beatra. It supports planning, authorization, uploads, model discovery, paid generation, asynchronous task recovery, and result delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a broad Beatra account bearer token in a local credential file.

Mitigation: Install only when the user trusts Beatra with account authorization, keep the credential file private, and verify Windows file permissions are limited to the current user.

Risk: Automatic package updates are enabled by default before ordinary Beatra commands.

Mitigation: Review the update behavior before installation and disable silent checks with `python3 scripts/mcp_client.py update --auto off` when tighter change control is required.

Risk: Image, video, music, speech, voice-clone, and prompt-enhancement operations can consume Beatra credits.

Mitigation: Use the skill's admission, estimate, balance, ledger, idempotency, and task-recovery steps so paid work is submitted intentionally and not duplicated.

Risk: Voice cloning can misuse a person's voice without authorization.

Mitigation: Clone a voice only after explicit confirmation that the user owns the voice or has the owner's permission.

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

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON payload guidance, and returned Beatra task or asset details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, generated asset links or IDs, resolved model details, dimensions, duration, MIME type or format, file size, and credit usage when returned by Beatra.]

## Skill Version(s):

0.1.9 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
