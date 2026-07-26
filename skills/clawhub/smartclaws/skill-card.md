## Description: <br>
Smartclaws guides an agent and owner through SmartClaws setup for publishing and reading IoT telemetry on SKALE, including plugin installation, wallet setup, on-chain identity, role selection, deployment facts, and operating-contract templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent owners use this skill to onboard SmartClaws deployments by configuring the plugin, wallet, roles, deployment facts, and operating contracts for IoT telemetry and device-control workflows on SKALE. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write tools can publish on-chain messages or notify agents, and deployment templates may enable device commands when allowlisted. <br>
Mitigation: Review owner-defined authority, commandable devices, and on-chain logging scope before enabling write tools or adopting AGENTS.md templates. <br>
Risk: Wallet files, private keys, or secrets could be exposed if copied into setup notes or deployment files. <br>
Mitigation: Keep private keys, wallet files, and secrets out of SMARTCLAWS.md and notes; use wallet-info output for addresses only and leave key handling to the owner. <br>
Risk: Incorrect deployment facts can cause the agent to read or write the wrong device, channel, or agent identity. <br>
Mitigation: Record and verify device names, channel addresses, agent ids, and commandability in SMARTCLAWS.md; stop and ask rather than guessing missing addresses. <br>
Risk: On-chain logs may disclose operational decisions or telemetry metadata. <br>
Mitigation: Review what the deployment logs on-chain and limit recorded content to what is acceptable for the intended SmartClaws deployment. <br>


## Reference(s): <br>
- [SmartClaws homepage](https://github.com/skalenetwork/smartclaws) <br>
- [Smartclaws ClawHub page](https://clawhub.ai/eduv09/skills/smartclaws) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell, JSON, YAML, and AGENTS.md template snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes owner-editable SMARTCLAWS.md and AGENTS.md templates; write actions require explicit tool allowlisting and owner-defined authority.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
