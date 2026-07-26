## Description: <br>
persistent-sshfs helps agents guide users through installing and running a Bash SSHFS helper that retries initial key-based mounts and relies on sshfs reconnect plus scheduled re-runs for persistence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they need guidance for bringing up SSHFS mounts at boot or login, retrying initial key-based SSH authentication, and configuring cron or systemd timers for recurring remount attempts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install flow downloads an executable script from GitHub. <br>
Mitigation: Review the upstream script before installing or running it. <br>
Risk: Configured SSHFS mounts expose remote filesystems locally and use the user's existing SSH keys. <br>
Mitigation: Use only trusted remote hosts and protect SSH keys used for non-interactive authentication. <br>
Risk: Failed key-based SSH authentication can retry indefinitely and cron or systemd settings can leave repeated long-running attempts. <br>
Mitigation: Configure timers, intervals, and service timeouts deliberately, especially for unreliable hosts or networks. <br>
Risk: The helper is not a resident watchdog after mounts succeed. <br>
Mitigation: Use the documented cron or systemd timer pattern to re-run it when fully dropped mounts need recovery. <br>
Risk: Unclean termination can leave SSHFS mounts dangling. <br>
Mitigation: Check active fuse.sshfs mounts and unmount stale mount points manually with fusermount when cleanup did not run. <br>


## Reference(s): <br>
- [Setup](references/setup.md) <br>
- [Upstream project homepage](https://github.com/psyb0t/persistent-sshfs) <br>
- [Install script source](https://raw.githubusercontent.com/psyb0t/persistent-sshfs/master/persistent-sshfs) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/persistent-sshfs) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and systemd or cron configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes mount-file syntax, install steps, runtime behavior, and safety notes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
