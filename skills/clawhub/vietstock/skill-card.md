## Description: <br>
Automated Vietnamese stock price and index checking on FireAnt.vn for current prices, market indices, trading volumes, and financial metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aholake](https://clawhub.ai/user/aholake) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to retrieve Vietnamese equity and index quotes from FireAnt.vn for quick market checks and symbol comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill opens Google and FireAnt.vn through the OpenClaw browser profile to retrieve market data. <br>
Mitigation: Install and run it only when this browser automation and external-site access are acceptable for the environment. <br>
Risk: Unexpected symbols, arbitrary URLs, or unusual strings may produce unreliable lookup behavior. <br>
Mitigation: Use normal stock symbols or index names as input, as recommended by the security guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aholake/skills/vietstock) <br>
- [Publisher profile](https://clawhub.ai/user/aholake) <br>
- [FireAnt stock and index lookup page](https://fireant.vn/ma-chung-khoan/{SYMBOL}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown] <br>
**Output Format:** [Markdown-formatted text with stock or index price, volume, and key market metrics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts one or more Vietnamese stock symbols or index names; results depend on FireAnt.vn availability and page content.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
