## Description: <br>
Home Assistant OS SSH maintenance for config files, YAML, custom components, shell troubleshooting, or interactive ha CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextaltair](https://clawhub.ai/user/nextaltair) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Home Assistant operators and maintainers use this skill to decide when SSH access is appropriate for Home Assistant OS maintenance and how to inspect or minimally edit configuration files, YAML, custom components, logs, and ha CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SSH maintenance and direct edits to Home Assistant YAML or .storage files can affect automations, locks, alarms, access control, or physical devices. <br>
Mitigation: Review proposed edits before applying them, start with read-only inspection, back up exact .storage files before direct edits, and ask before changes that affect safety-sensitive or physical-device behavior. <br>
Risk: One-shot SSH sessions may fail for interactive ha CLI log workflows and can lead to incomplete troubleshooting. <br>
Mitigation: Use an interactive PTY-backed SSH session for ha CLI logs or other commands that fail in one-shot mode. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/haos-ssh-maintenance) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with inline shell command examples and file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Focuses on read-first investigation, minimal edits, reload-or-restart guidance, and concise reporting of inspected paths and changes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
