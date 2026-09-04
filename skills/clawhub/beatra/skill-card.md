## Description:

Beatra helps agents create and manage AI images, videos, music, speech, reusable voices, and public social data lookups through a shared Beatra connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route creative media generation, public social data lookup, model discovery, upload preparation, task tracking, and credit reporting through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can silently replace its own installed package files during automatic updates.

Mitigation: In stricter environments, disable automatic updates with `python3 scripts/mcp_client.py update --auto off` and perform explicit update checks before use.

Risk: The skill stores a shared Beatra device authorization in `~/.beatra` and registers a stable installation identity.

Mitigation: Install only on trusted systems, revoke the Beatra device from the Beatra Console when no longer needed, and use the bundled uninstall guidance for cleanup.

Risk: Requested local media uploads and approved creative or public social operations can send data to Beatra and spend Beatra credits.

Mitigation: Review each paid request boundary, require explicit confirmation for video and voice-clone workflows described by the skill, and check wallet or ledger tools when cost matters.

## Reference(s):

- [Beatra ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/beatra)
- [Beatra Installation](https://beatra.ai/install)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Images](references/images.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Bundled MCP Client Diagnostics](references/mcp-connection.md)
- [Models](references/models.md)
- [Music](references/music.md)
- [Public Social Data](references/social.md)
- [Speech and Voices](references/speech-and-voices.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)
- [Uploads](references/uploads.md)
- [Video Controls](references/video-controls.md)
- [Video Recipes](references/video-recipes.md)
- [Videos](references/videos.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with shell command snippets, JSON request payloads, and returned media or social-data references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, usage, billing credits, media artifact links or IDs, dimensions, duration, MIME type, and size when returned.]

## Skill Version(s):

2.7.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
