## Description: <br>
Control Eight Sleep pods for status, temperature, alarms, and schedules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to operate an Eight Sleep pod through the eightctl CLI, including checking status and managing temperature, alarms, schedules, audio, and base angle. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward device-changing actions such as temperature, alarms, schedules, audio, or base angle changes. <br>
Mitigation: Require explicit user confirmation before executing any device-changing command. <br>
Risk: Eight Sleep credentials may be exposed through shared prompts, logs, or command output. <br>
Mitigation: Keep credentials in the local eightctl config or environment and redact them from shared logs and prompts. <br>
Risk: The underlying Eight Sleep API is unofficial and rate-limited. <br>
Mitigation: Avoid repeated logins and repeated command loops that could trigger rate limits. <br>


## Reference(s): <br>
- [Eightctl homepage](https://eightctl.sh) <br>
- [Eightctl Go module](https://github.com/steipete/eightctl) <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/eightctl) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the eightctl CLI and Eight Sleep credentials configured through a local config file or environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
