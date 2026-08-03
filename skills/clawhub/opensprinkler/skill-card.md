## Description: <br>
Monitor and control an OpenSprinkler irrigation controller, including status checks, manual station and program runs, rain delays, logs, queue pauses, and overall system operation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jnord3](https://clawhub.ai/user/jnord3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Homeowners, facilities teams, and integrators use this skill to let an agent inspect and operate a local OpenSprinkler irrigation controller through its HTTP API. It supports routine irrigation checks and manual control workflows where the user is comfortable granting password-backed access to the controller. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent password-backed local control over watering operations, including starting and stopping stations, pausing schedules, disabling automatic operation, setting rain delays, reading logs, and rebooting the controller. <br>
Mitigation: Install only on a trusted local network and require clear user confirmation before disruptive actions. <br>
Risk: The server security summary notes limited safety gating for operations that affect irrigation and hardware state. <br>
Mitigation: Review the skill before installation and restrict access to users who are authorized to operate the OpenSprinkler controller. <br>


## Reference(s): <br>
- [OpenSprinkler ClawHub Skill Page](https://clawhub.ai/jnord3/skills/opensprinkler) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENSPRINKLER_IP_ADDRESS and OPENSPRINKLER_PASSWORD for local controller access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
