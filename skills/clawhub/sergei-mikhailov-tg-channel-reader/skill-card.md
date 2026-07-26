## Description: <br>
Lets an agent read and monitor Telegram channels by fetching posts, captions, link previews, and comments from public or subscribed private channels for digests, summaries, and alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bzsega](https://clawhub.ai/user/bzsega) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external users use this skill to let an agent check Telegram channels, summarize recent posts, monitor unread updates, inspect channel metadata, and include comments when needed. It is intended for channels the authenticated Telegram account can already access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a local Telegram session that can grant broad access to the authenticated account. <br>
Mitigation: Install only when an agent on this machine should read Telegram channels for that account; keep session files local, private, and permissioned 0600. <br>
Risk: Credentials, session backups, saved outputs, unread-state files, and auth progress files may expose sensitive account or channel data. <br>
Mitigation: Avoid syncing or committing those files, store credentials outside project directories, and use private paths for cron jobs or TG_AUTH_PROGRESS. <br>
Risk: The agent can read private channels available to the authenticated account. <br>
Mitigation: Use the skill only for channels the user intentionally authorizes, and review saved digests or exported files before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bzsega/skills/sergei-mikhailov-tg-channel-reader) <br>
- [Telegram API credentials](https://my.telegram.org) <br>
- [OpenClaw Control UI approvals](https://docs.openclaw.ai/web/control-ui) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON or plain text from CLI commands, with optional JSON/text output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes channel metadata, post text, captions, links, link previews, comments, unread-tracking metadata, and structured error fields when applicable.] <br>

## Skill Version(s): <br>
0.11.1 (source: server release metadata, changelog, setup.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
