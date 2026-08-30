## Description:

Short Video BGM Studio helps an agent turn a footage or scene description and target length into a confirmed Beatra request for one original instrumental background track for short videos and related media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to brief, confirm, generate, and recover one paid Beatra instrumental BGM task from a scene description and target length for short videos, livestreams, podcast intros or outros, store loops, and slideshow recaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra device token grants shared authority that can spend credits and access multiple media tools beyond music.

Mitigation: Review the authorization before installing, use a Beatra account with appropriate spending limits, keep the token private, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` when automatic replacement is not acceptable, and use `python3 scripts/mcp_client.py update --check` to inspect availability.

Risk: Reference audio or other user media uploaded for generation is sent to Beatra.

Mitigation: Upload only reference audio the user intends to send to Beatra, and do not expose authentication tokens, complete private prompts, or sensitive input content during recovery.

## Reference(s):

- [Short Video BGM Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/short-video-bgm-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/short-video-bgm-studio)
- [BGM workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP payloads; completed tasks may return audio URLs or artifact IDs with duration, MIME type, size, usage, and billing fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One instrumental music generation task is submitted only after confirmation; final billing should be reported from billing.net_charged_credits.]

## Skill Version(s):

0.1.5 (source: server release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
