## Description: <br>
KLYC-PMM is a bash-based agent memory client for registering an identity, syncing text memories with kunlunyaochi.com, recovering from a token URL, running file watchers, and using X402 WeChat payment upgrades. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sylncn](https://clawhub.ai/user/sylncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to configure persistent text memory workflows for OpenClaw, LightClaw, or Claude Code agents, including push, search, recovery, watch-daemon, and paid upgrade flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates as a networked memory-sync client and may upload identity or memory files to kunlunyaochi.com. <br>
Mitigation: Review watched files and pushed content before use, avoid storing secrets in synced memory files, confirm the configured endpoint, and use explicit workspace paths. <br>
Risk: Installer and upgrade flows can create background persistence and write to broad system paths. <br>
Mitigation: Prefer manual commands and self-test first; avoid running installers as root unless system-wide systemd persistence and updater writes are intended. <br>
Risk: Paid upgrade flows use X402 and WeChat payment handling. <br>
Mitigation: Confirm the payment plugin, amount, service tier, and order ID before retrying paid upgrade commands. <br>
Risk: Watch, recover, and distillation workflows can change local memory files. <br>
Mitigation: Back up MEMORY.md, SOUL.md, and IDENTITY.md before automated recovery or watcher use, and use dry-run mode for distillation previews where supported. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm) <br>
- [PMM full architecture](artifact/references/pmm-full-architecture.md) <br>
- [Pay Skill packaging standard](artifact/references/pay-skill-spec.md) <br>
- [Examples and quickstart](artifact/examples/README.md) <br>
- [KLYC-PMM service page](https://kunlunyaochi.com/?route=services) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate commands that install dependencies, register an identity, upload memory content, configure systemd persistence, update local scripts, or call payment endpoints.] <br>

## Skill Version(s): <br>
9.0.1 (source: frontmatter, skill.json, changelog, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
