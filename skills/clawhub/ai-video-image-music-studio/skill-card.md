## Description:

Generate AI video, images, music, voice-over, and reusable voices through a connected Beatra creative workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to create, edit, and manage generated images, videos, music, narration, and voice-clone outputs from one Beatra workflow. Agents use it to choose the smallest suitable media-generation path, manage authorization and uploads, submit paid jobs, poll asynchronous tasks, and report returned usage and artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect a Beatra account, upload selected media, and submit paid media-generation requests.

Mitigation: Install only when those account, upload, and credit-spend scopes are acceptable; review admission prompts before authorizing video generation or voice cloning.

Risk: The package silently checks for and may install verified updates by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when package code changes require prior review.

Risk: A shared Beatra device credential is stored under `~/.beatra` and used by Beatra packages.

Mitigation: Use the bundled uninstall flow for local cleanup and the Beatra Console to revoke access when the connection is no longer trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-video-image-music-studio)
- [Beatra skill homepage](https://beatra.ai/skills/ai-video-image-music-studio)
- [Images](references/images.md)
- [Videos](references/videos.md)
- [Video controls](references/video-controls.md)
- [Video recipes](references/video-recipes.md)
- [Music](references/music.md)
- [Speech and voices](references/speech-and-voices.md)
- [Models](references/models.md)
- [Uploads](references/uploads.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, returned task metadata, links, IDs, and usage details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media artifact URLs or IDs, dimensions, duration, MIME type, file size, task status, model, and billing details when returned by Beatra.]

## Skill Version(s):

0.1.7 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
