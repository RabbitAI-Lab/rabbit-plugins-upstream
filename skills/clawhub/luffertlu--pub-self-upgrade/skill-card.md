## Description: <br>
Helps an agent upgrade OpenClaw by reviewing release notes, backing up the current install, running an npm-based upgrade, restarting the user systemd service, and reporting rollback status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luffertlu](https://clawhub.ai/user/luffertlu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when they intentionally want an agent-assisted OpenClaw self-upgrade on Linux systems managed by a user-level systemd service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make persistent service-changing upgrades with npm, filesystem, GitHub API, and user-level systemd authority. <br>
Mitigation: Review the script before installing, confirm the service target and backup location, and run it only for an intended OpenClaw self-upgrade. <br>
Risk: Using openclaw@latest or delayed cron upgrades can change the exact target version or timing. <br>
Mitigation: Prefer approving a specific version and use delayed execution only when the timing, target version, and rollback plan are clear. <br>
Risk: Server security evidence marks the release suspicious because its controls are weaker than the safety description claims. <br>
Mitigation: Treat this release as review-required, inspect logs after execution, and verify rollback behavior in the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luffertlu/skills/pub-self-upgrade) <br>
- [OpenClaw release notes API endpoint](https://api.github.com/repos/openclaw/openclaw/releases/tags/v2026.6.5) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, upgrade status summaries, log paths, and rollback guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute filesystem, npm, GitHub API, and user-level systemd operations when used as intended.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and SKILL.md changelog, released 2026-07-19; package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
