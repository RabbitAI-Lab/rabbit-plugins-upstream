## Description: <br>
Run one SmartClaws bridge cycle for a single device: read local hardware or API data, validate it against the device contract, publish telemetry on-chain, and apply on-chain commands only in command-enabled modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run a single SmartClaws telemetry bridge cycle for one configured device, with optional command handling only when the owner has enabled and authorized that mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Command-enabled modes could apply on-chain commands to the wrong device or channel if bridge configuration is incorrect. <br>
Mitigation: Keep telemetry-only as the default and verify SMARTCLAWS.md, AGENTS.md, the device contract, the device name or channel, and the incoming command channel before enabling command modes. <br>
Risk: Telemetry publication could publish implausible, simulated, or wrong-device data. <br>
Mitigation: Validate readings against device contract sanity rules, publish for exactly one assigned device, and label simulated payloads clearly when simulation is explicitly requested. <br>
Risk: Bridge runs may expose wallet or key material if logs or diagnostics include secrets. <br>
Mitigation: Do not read or print wallet or key material; use wallet information only for non-secret operational details. <br>


## Reference(s): <br>
- [SmartClaws project homepage](https://github.com/skalenetwork/smartclaws) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration] <br>
**Output Format:** [Markdown procedure with ordered steps and guardrails] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SmartClaws plugin configuration and one device contract; defaults to telemetry-only when bridge mode is absent.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
