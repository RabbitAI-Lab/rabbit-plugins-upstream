## Description: <br>
KLYC-PMM is a shell-based persistent memory management skill for AI agents that initializes an identity, backs up and restores text memories with a recovery token, supports cloud search and distillation workflows, and can watch files for ongoing synchronization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sylncn](https://clawhub.ai/user/sylncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to add persistent text memory, recovery, search, and file-watching workflows to OpenClaw, LightClaw, or Claude Code environments. It is most relevant for agents that need long-running memory backup and restore behavior across sessions or hosts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload memory and identity files to a remote cloud service. <br>
Mitigation: Review target files and service endpoints before running init, push, backup, recover, watch, or oneclick workflows; use test data first. <br>
Risk: Daemon and watch workflows can create persistent background monitoring behavior. <br>
Mitigation: Inspect install-daemon.sh and generated systemd service definitions, then enable persistence only in environments where continuous file monitoring is intended. <br>
Risk: Upgrade and recovery workflows may perform paid account actions or mutate remote memory records. <br>
Mitigation: Confirm account, token, tier, and recovery scope before running upgrade, pmm_distill.sh, pmm_backup_files.sh, or recover commands. <br>
Risk: Update workflows download and replace executable scripts. <br>
Mitigation: Review update.sh behavior and verify downloaded script hashes before applying updates in production. <br>


## Reference(s): <br>
- [PMM Full Architecture](references/pmm-full-architecture.md) <br>
- [Examples README](examples/README.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/sylncn/skills/klyc-pmm) <br>
- [KLYC-PMM Online Documentation](https://kunlunyaochi.com/?route=klyc-pmm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands; bundled scripts may create local configuration files, recovery data, and systemd service definitions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; file watching and daemon installation may also require inotify-tools, systemd, and elevated local permissions.] <br>

## Skill Version(s): <br>
8.3.4 (source: evidence.release.version, SKILL.md frontmatter, skill.json, CHANGELOG released 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
