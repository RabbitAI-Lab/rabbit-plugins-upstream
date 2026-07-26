## Description: <br>
Run one SmartClaws master control cycle: read device telemetry on-chain, decide under the owner's guidelines, command a device only when allowed, and log the decision on-chain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
SmartClaws owners and operators use this skill to run a single authorized control cycle for configured devices. It helps an agent read telemetry, decide whether to act under owner policy, publish one allowed command when warranted, and record an auditable decision log. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill can command configured SmartClaws devices and publish durable on-chain logs. <br>
Mitigation: Install it only where AGENTS.md and SMARTCLAWS.md clearly define authorized callers, commandable devices, channels, and policy; keep read-only audit runs distinct from command-capable runs. <br>
Risk: A stale or malformed telemetry reading could lead to an unsafe or incorrect command decision. <br>
Mitigation: Validate telemetry freshness and payload shape against the relevant device contract before acting, and avoid command actions unless the owner's guidelines explicitly allow them. <br>


## Reference(s): <br>
- [SmartClaws project homepage](https://github.com/skalenetwork/smartclaws) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, API calls] <br>
**Output Format:** [Markdown or plain text with structured decision details and transaction hashes when actions are published] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read SmartClaws telemetry, publish at most one authorized device command, and publish a decision.log event through configured plugin tools.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
