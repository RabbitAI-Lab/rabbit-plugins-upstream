## Description: <br>
Bash tool that brings up SSHFS mounts, retries initial key-based connections until they succeed, and documents cron or systemd re-run patterns for mounts that later drop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and system administrators use this skill to configure SSHFS mount files, install the helper, and set up boot or periodic re-runs for trusted remote filesystems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install flow downloads an upstream shell script. <br>
Mitigation: Inspect the script before installing it, use a trusted source, and prefer a pinned source when operationally possible. <br>
Risk: SSHFS exposes remote files locally and sends local writes back to the remote host. <br>
Mitigation: Configure only trusted hosts and trusted mount points. <br>
Risk: A host with broken or missing key-based authentication can cause the run to wait indefinitely. <br>
Mitigation: Verify key-based SSH access before scheduling the helper and set service timeouts where unattended runs should not hang. <br>


## Reference(s): <br>
- [Setup](references/setup.md) <br>
- [Persistent Sshfs homepage](https://github.com/psyb0t/persistent-sshfs) <br>
- [Persistent Sshfs on ClawHub](https://clawhub.ai/psyb0t/skills/persistent-sshfs) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with shell commands and systemd or cron configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes mount-file syntax, install steps, environment variable guidance, and re-run recipes for persistence.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
