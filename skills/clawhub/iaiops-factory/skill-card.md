## Description: <br>
Factory edition of iaiops for discrete-manufacturing operations across PLC, CNC, gateway, MQTT/Sparkplug/UNS, and industrial protocol workflows, with read-first diagnostics and management-of-change-gated writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Manufacturing engineers, controls engineers, and operations teams use this skill to inspect and troubleshoot discrete-manufacturing production lines, including PLCs, CNC assets, industrial networks, SCADA/MES gateways, and Unified Namespace data. It supports read-first diagnostics, OEE and downtime analysis, asset inventory, and explicitly gated write workflows that require management-of-change approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide high-impact write operations against industrial control systems. <br>
Mitigation: Keep write tools disabled unless a real management-of-change approval is in place, and require explicit approval before production changes. <br>
Risk: Raw industrial protocols and fieldbus diagnostics may require privileged network access or dedicated interfaces. <br>
Mitigation: Install only where the agent is authorized to inspect industrial systems and use dedicated network interfaces for raw industrial protocols. <br>
Risk: SCADA/MES credentials could expose production data or operational controls if mishandled. <br>
Mitigation: Store SCADA/MES tokens only in the configured secret store and avoid inline credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with tool and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include diagnostic findings, operational recommendations, configuration steps, and gated write plans for industrial systems.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
