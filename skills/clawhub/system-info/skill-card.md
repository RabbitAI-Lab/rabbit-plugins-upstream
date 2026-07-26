## Description: <br>
Quick system diagnostics: CPU, memory, disk, uptime <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to request quick local Linux diagnostics for CPU, memory, disk, and uptime while troubleshooting a system. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented system-info command could resolve to an unexpected executable on PATH. <br>
Mitigation: Confirm the system-info executable is the expected trusted command before relying on its diagnostics. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/system-info) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with bash command examples and plain-text diagnostic output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a trusted local system-info command and standard Linux utilities such as free.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
