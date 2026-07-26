## Description: <br>
Provides a Clawdbot/Moltbot patch that restores TTS auto-replies for Discord voice memos by ensuring the final reply payload reaches the TTS pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koto9x](https://clawhub.ai/user/koto9x) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and bot operators use this skill to review and apply a manual Clawdbot/Moltbot core patch for voice memo TTS auto-replies. It is intended for environments where inbound audio messages should trigger configured TTS responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The patch overwrites core Clawdbot files and may not match every installed Clawdbot version. <br>
Mitigation: Review the patched files against the exact installed version, apply first in a non-production bot, and keep backups for rollback. <br>
Risk: Debug logging can expose private message snippets or credential fragments during real user traffic. <br>
Mitigation: Remove or gate all TTS debug console logs before production use. <br>
Risk: Reply text may be sent to the configured TTS provider during synthesis. <br>
Mitigation: Confirm the configured provider is acceptable for the users and data handled by the bot. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/koto9x/skills/discord-voice-memo-upgrade) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [PATCH.md](artifact/PATCH.md) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown documentation with JavaScript patch files and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Manual patch package; debug logging should be removed or gated before production use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, package.json, CHANGELOG dated 2026-01-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
