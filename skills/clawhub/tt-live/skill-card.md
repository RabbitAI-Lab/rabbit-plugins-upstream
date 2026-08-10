## Description:

TikTok LIVE monitor. Check whether a TikTok user is live right now, resolve their current m3u8 stream URL, or spawn a background daemon that polls them over a timer window and emits go_live / go_offline / rename_detected events for the sub-agent to announce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kikikari](https://clawhub.ai/user/kikikari)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to check TikTok LIVE status for a single handle, retrieve the active 360p m3u8 stream URL, or run a timed local watch that emits live, offline, rename, and daemon lifecycle events for an agent to announce.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watch mode starts a background polling process and writes identity, state, event, and log files in the local OpenClaw workspace.

Mitigation: Start watch mode only for TikTok LIVE monitoring the user requested, inspect the printed workspace and log paths, and stop the printed PID when monitoring is no longer wanted.

Risk: Resolved stream URLs are tied to the current live session and may become invalid when a user goes offline or starts a new session.

Mitigation: Treat cached stream URLs as session-scoped data and re-check live status before sharing or using a URL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kikikari/skills/tt-live)
- [Publisher profile](https://clawhub.ai/user/kikikari)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [JSON records, stream URL strings, key=value daemon status lines, append-only event logs, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local workspace state, identity records, event files, and logs; daemon polling has a 5-minute floor and stream URLs are session-bound.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
