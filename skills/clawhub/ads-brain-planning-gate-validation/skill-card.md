## Description: <br>
规划 Agent 新框架中的门禁与校验通用协议。定义 Capability Gate、Scenario Gate、Business Guard、Payload Validation、Execution Gate、场景化 Guard、skipped 状态、blocked_reason 与 next_action。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lizejia668-code](https://clawhub.ai/user/lizejia668-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Planning-agent developers use this skill as a shared protocol for deciding whether advertising plan creation or optimization flows should continue, ask for clarification, route elsewhere, warn, or block. It defines common gate, guard, validation, skipped-state, blocked-reason, and next-action conventions for related planning pipeline skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A future implementation could connect the protocol to live advertising tools without preserving the intended confirmation, validation, and scoping controls. <br>
Mitigation: Require explicit execution confirmation and payload validation before any live advertising change is made. <br>
Risk: Downstream planning pipelines could apply the protocol inconsistently, especially around skipped guards, blocked reasons, and next actions. <br>
Mitigation: Treat the protocol as a shared contract and test integrations for consistent skipped, blocked, warning, route, and clarification outcomes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lizejia668-code/skills/ads-brain-planning-gate-validation) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown protocol documentation with JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defines control-plane conventions for planning agents; it does not provide executable code.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
