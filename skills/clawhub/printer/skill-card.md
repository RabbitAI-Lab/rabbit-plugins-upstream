## Description: <br>
Manage printers via CUPS on macOS, including discovery, printer setup, printing, queue management, status checks, wake commands, and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dhvanilpatel](https://clawhub.ai/user/dhvanilpatel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, IT operators, and macOS users can use this skill to have an agent propose CUPS commands for discovering printers, adding printer queues, printing files, managing jobs, checking status, and troubleshooting common printer issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can change printer defaults, queue state, or submitted jobs. <br>
Mitigation: Before approving commands, verify the exact printer name, file path, job ID, and intended queue action. <br>
Risk: Some actions use sudo, cancel all jobs, disable or reject printers, remove queues, install optional SNMP tools, or set up persistent keep-alive behavior. <br>
Mitigation: Require explicit user approval for administrative, destructive, package-installation, or persistent background actions, and confirm the affected printer or host first. <br>


## Reference(s): <br>
- [ClawHub Printer skill page](https://clawhub.ai/dhvanilpatel/skills/printer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS with CUPS command-line tools; optional SNMP toner checks require net-snmp.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
