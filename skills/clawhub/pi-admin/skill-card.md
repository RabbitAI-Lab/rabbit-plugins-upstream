## Description: <br>
Raspberry Pi system administration. Monitor resources, manage services, perform updates and maintenance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and Raspberry Pi administrators use this skill to inspect host health, network state, Tailscale status, storage, services, and hardware, and to run maintenance tasks such as updates, cleanup, reboot, gateway restart, and reversible Pi optimizations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make root-level system changes, including package updates, package cleanup, log cleanup, service changes, persistent tuning, and reboot. <br>
Mitigation: Install only on the intended Raspberry Pi, review each maintenance command first, prefer --dry-run, and require explicit human approval before sudo, reboot, cleanup, update, or optimization actions. <br>
Risk: The gateway restart workflow uses a hardcoded Clawdis Gateway path and network configuration and can interrupt gateway availability. <br>
Mitigation: Confirm the gateway path, port, and IP assumptions on the target host before restart, and schedule restarts during an acceptable maintenance window. <br>
Risk: Optimization changes can disable Bluetooth, ModemManager, and Avahi and persistently change swappiness. <br>
Mitigation: Run optimize with --dry-run first, confirm those services are not needed, and use the documented --undo path if the optimization affects required host behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thesethrose/skills/pi-admin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text and Markdown guidance with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintenance commands support --dry-run where documented; optimize also supports --undo.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
