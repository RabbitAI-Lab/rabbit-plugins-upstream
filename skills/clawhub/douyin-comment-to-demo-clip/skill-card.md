## Description:

Turn Douyin comment objections into one comment talking clip per still. This douyin comment demo studio writes a speakable demo talking clip from each seller-picked objection, then animates a 2 to 15s objection demo clip. Use it for comment demo video and a douyin objection video that stay one photo, one clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and their agents use this skill to turn public Douyin comment objections and authorized still images into planned quote-to-demo slots, then into approved speech and short talking demo clips. It guides approval, billing, recovery, and delivery for one 2-15 second clip per still without posting replies or stitching clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra Device Token that can spend credits, upload selected media, generate and manage assets, read task state, and store local state under ~/.beatra.

Mitigation: Install only when that shared authorization is acceptable, keep the token out of chat, logs, command arguments, and environment variables, and run the bundled authorization and uninstall helpers for connection changes.

Risk: Billable lookup, voice, speech, and video operations can consume credits, and retries after uncertain transport failures could duplicate work if request identity changes.

Mitigation: Show the documented approval card before each paid stage, use one opaque client_request_id per unchanged request, poll existing tasks before replay, and report returned billing.net_charged_credits.

Risk: Automatic package updates are enabled by default and can replace package-owned files silently.

Mitigation: Review the release before installation and disable silent checks with python3 scripts/mcp_client.py update --auto off when automatic replacement is not acceptable.

Risk: The workflow can involve likeness, voice cloning, local media uploads, and public social comment lookup.

Mitigation: Require explicit rights and approval for stills, cloned voices, comment lookup, speech, and video as separate stages, and use pasted comments when Douyin lookup is unavailable or not approved.

## Reference(s):

- [Douyin comment-to-demo workflow](references/workflow.md)
- [Douyin comment lookup](references/comment-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP payloads; approved remote tasks may return generated media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces separate 2-15 second clips per approved still; does not stitch clips.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
