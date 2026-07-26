## Description: <br>
Synchronize memory, preferences, and skills between multiple Clawdbot instances via SSH/rsync over Tailscale. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[udiedrichsen](https://clawhub.ai/user/udiedrichsen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators who run multiple Clawdbot instances use this skill to configure peers, preview diffs, and synchronize memory, user profile, and optional skill data over SSH/rsync. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sync operations can transfer or overwrite sensitive agent memory and profile data across machines. <br>
Mitigation: Use the skill only between machines you control, run /sync diff before syncing, keep backups, and test with non-sensitive data before enabling routine sync. <br>
Risk: SSH peer trust can be weakened if host keys are not verified before connecting. <br>
Mitigation: Use a dedicated least-privilege SSH account and key, and verify or pin SSH host keys before adding peers. <br>


## Reference(s): <br>
- [Setup Guide](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires rsync, ssh, and jq; sync operations can modify configured workspace memory and profile files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
