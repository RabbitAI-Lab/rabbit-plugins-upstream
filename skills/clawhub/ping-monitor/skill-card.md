## Description: <br>
ICMP health check for hosts, phones, and daemons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to check whether a host, phone, daemon, service, or device is reachable with the standard ping utility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends ping traffic to a user-specified host, which can reach devices, services, or networks outside the user's authority. <br>
Mitigation: Use it only for hosts, services, devices, and networks the user owns or has permission to monitor. <br>


## Reference(s): <br>
- [Ping Monitor ClawHub listing](https://clawhub.ai/xejrax/skills/ping-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the system ping binary and sends network traffic to the named host.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
