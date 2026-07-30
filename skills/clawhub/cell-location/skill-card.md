## Description: <br>
This skill helps agents query approximate 5G cell-tower location information from Juhe Data using MCC, MNC, TAC/LAC, and CI parameters through a disclosed paid Alipay A2M payment flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up an approximate cell-tower location after providing the required MCC, MNC, TAC/LAC, and CI identifiers. It is intended for cell-location checks, simple location parsing, and nearby-service support after the user accepts the paid request flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cell-tower identifiers can reveal an approximate physical location and are sent to apis.juhe.cn for lookup. <br>
Mitigation: Proceed only when the user intentionally provides the identifiers and understands the third-party lookup. <br>
Risk: The lookup is a paid request that depends on an Alipay payment step. <br>
Mitigation: Ask the user to accept the Alipay payment flow before completing paid requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/cell-location) <br>
- [Juhe Data A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>
- [Publisher profile](https://clawhub.ai/user/juhemcp) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires complete cell-tower identifiers and may return a 402 Payment-Needed response that must be passed unchanged to the Alipay payment skill.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
