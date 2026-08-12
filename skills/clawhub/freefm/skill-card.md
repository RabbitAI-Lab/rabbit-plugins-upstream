## Description:

Set up and operate the FreeFM Rust app for NetEase Private FM, including its TUI, QR login, read-only preview, append-only sync, diagnostics, and zero-LLM scheduling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuxin-qiao](https://clawhub.ai/user/yuxin-qiao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to install, authenticate, preview, sync, troubleshoot, and schedule FreeFM for their own NetEase Cloud Music Private FM account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate against a user's NetEase Cloud Music account.

Mitigation: Use it only with the user's own account, keep QR login visible and user-driven, and never ask the user to provide cookies, session tokens, MUSIC_U, or QR keys.

Risk: A scheduled sync job can repeatedly modify the user's music library or playlist state.

Mitigation: Run one manual preview and one manual sync successfully before scheduling, review the scheduled job after setup, and verify the first scheduled run.

Risk: Credential or playback data could be exposed through terminal output, logs, or commits.

Mitigation: Do not print, inspect, summarize, upload, or commit credentials, session files, cookies, QR keys, or playback URLs.

## Reference(s):

- [FreeFM ClawHub release](https://clawhub.ai/yuxin-qiao/skills/freefm)
- [FreeFM project homepage](https://github.com/Yuxin-Qiao/FreeFM)
- [FreeFM README](https://github.com/Yuxin-Qiao/FreeFM/blob/main/README.zh-CN.md)
- [Immutable freefm-sync.sh helper](https://raw.githubusercontent.com/Yuxin-Qiao/FreeFM/c7bcf10dce142fd85c84f82173a307e91ea99adc/skills/freefm/scripts/freefm-sync.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports user-driven QR login, manual preview before sync, append-only synchronization, diagnostics, and scheduled command runs without model-backed turns.]

## Skill Version(s):

0.1.0-alpha.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
