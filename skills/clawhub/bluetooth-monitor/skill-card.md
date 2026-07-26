## Description: <br>
蓝牙设备监控 / Bluetooth Device Monitor helps view connected Mac Bluetooth devices and supports pairing, connection, disconnection, battery display, and power-status operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[franky0617](https://clawhub.ai/user/franky0617) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Mac users and support engineers use this skill to inspect connected and paired Bluetooth devices, check device battery information, and prepare commands to connect, disconnect, or change Bluetooth power state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Disconnecting devices or turning Bluetooth off can immediately interrupt Bluetooth peripherals. <br>
Mitigation: Confirm the user has a built-in keyboard or trackpad, wired input device, or another control path before running disconnect or power-off commands. <br>
Risk: The skill depends on blueutil and macOS Bluetooth data sources, so commands may fail or produce incomplete details when prerequisites are missing or older devices do not report battery level. <br>
Mitigation: Check that blueutil is installed and treat unavailable battery values as expected device limitations rather than errors. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/franky0617/skills/bluetooth-monitor) <br>
- [Publisher profile](https://clawhub.ai/user/franky0617) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for macOS Bluetooth workflows and rely on blueutil plus macOS system_profiler data.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
