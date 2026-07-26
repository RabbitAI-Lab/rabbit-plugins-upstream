## Description: <br>
Use the baud CLI to diagnose and automate serial, UART, COM-port, USB-to-TTL, and firmware-console workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nitmi](https://clawhub.ai/user/nitmi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and hardware engineers use this skill to guide Codex through cautious serial-port diagnostics, boot-log capture, baud CLI workflows, and interpretation of structured serial evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Serial hardware actions may move, heat, erase, flash, reset, or persistently reconfigure connected devices if commands or wiring are wrong. <br>
Mitigation: Confirm the baud-cli package source, connected port identity, device protocol, voltage and wiring safety, and physical action scope before transmitting commands. <br>
Risk: A successful command or ACK can be mistaken for verified hardware state. <br>
Mitigation: Use guarded workflows with read-back assertions, final state checks, and preserved logs before treating hardware behavior as successful. <br>


## Reference(s): <br>
- [Serial Hardware Safety and Diagnosis](references/safety.md) <br>
- [Baud Workflow Authoring and Results](references/workflows.md) <br>
- [ClawHub skill page](https://clawhub.ai/nitmi/skills/baud) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown with inline shell commands and YAML workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference baud JSON, JSONL, logs, exit codes, and preserved hardware evidence when available.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
