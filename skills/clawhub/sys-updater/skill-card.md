## Description: <br>
Production-safe Ubuntu maintenance orchestrator: runs daily apt security updates, tracks non-security updates across apt/npm/pnpm/brew with quarantine + auto-review, applies only approved updates, rotates logs/state, and generates clear 09:00 MSK Telegram reports (including what was actually installed). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spiceman161](https://clawhub.ai/user/spiceman161) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and system operators use this skill to maintain Ubuntu/OpenClaw hosts by scheduling apt security updates, tracking non-security package updates, reviewing npm/pnpm/brew updates, and generating daily maintenance reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can alter system packages and OpenClaw skills through scheduled maintenance flows. <br>
Mitigation: Review the automation policy before installation, use a dedicated low-privilege account, and explicitly decide whether unattended OpenClaw skill updates are acceptable on the host. <br>
Risk: The skill requires passwordless sudo for apt maintenance commands. <br>
Mitigation: Restrict sudoers entries to the exact documented apt-get and unattended-upgrade commands, validate the sudoers file with visudo, and avoid granting broad sudo permissions. <br>
Risk: The server security review states that dry-run and report paths should not be treated as fully side-effect-free. <br>
Mitigation: Inspect or disable the apt install, autoremove, report-time skill update, and dry-run paths before relying on them in unattended operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/spiceman161/skills/sys-updater) <br>
- [How sys-updater Works](docs/how-it-works.md) <br>
- [Sudoers Setup](docs/sudoers.md) <br>
- [Auto-Review System](docs/AUTO_REVIEW.md) <br>
- [Operations](docs/operations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, cron examples, sudoers snippets, and maintenance report text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce host-specific command sequences and status summaries for apt, npm, pnpm, brew, and OpenClaw skill maintenance.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
