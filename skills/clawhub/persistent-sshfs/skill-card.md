## Description: <br>
Bash tool that brings up SSHFS mounts, retries initial key-based SSH connections until they succeed, and uses sshfs reconnect behavior plus optional scheduled re-runs to restore dropped mounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and Linux workstation users use this skill to configure and run persistent SSHFS mount workflows for one or more trusted remote hosts. It is intended for boot, login, cron, or systemd timer setups where initial connection retries and periodic re-runs are useful. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill mounts remote filesystems and depends on the trustworthiness of the SSH hosts configured by the user. <br>
Mitigation: Configure only trusted remote hosts, use intentional key-based SSH access, and review mounted paths before writing data through them. <br>
Risk: The documented raw-master install command can change if the upstream source changes. <br>
Mitigation: Review the script before installation and prefer a pinned or locally reviewed copy for managed environments. <br>
Risk: Scheduled cron or systemd timer re-runs can keep recreating configured mounts after a user expects them to stop. <br>
Mitigation: Disable the cron entry or systemd timer before teardown, then verify and unmount any remaining SSHFS mounts manually. <br>
Risk: Missing or broken SSH key authentication can cause a run to wait indefinitely for a host. <br>
Mitigation: Test key-based SSH access before scheduling the skill and set service timeouts where unattended startup must not block. <br>


## Reference(s): <br>
- [Persistent Sshfs ClawHub page](https://clawhub.ai/psyb0t/skills/persistent-sshfs) <br>
- [Setup reference](references/setup.md) <br>
- [Declared project homepage](https://github.com/psyb0t/persistent-sshfs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and systemd or cron configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a plain-text mount configuration file with one local_dir:user@host:port:remote_dir entry per line.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
