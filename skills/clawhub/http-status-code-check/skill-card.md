## Description: <br>
查询HTTP状态码、网站可访问性 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaomeng-agi](https://clawhub.ai/user/xiaomeng-agi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit HTTP status code and website accessibility requests to XiaoMeng AGI's paid API and retrieve structured analysis after payment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is labeled as an HTTP status checker, but it routes user input and credentials to a paid third-party analysis API. <br>
Mitigation: Use it only when intentionally sending request text, URLs, endpoint details, order numbers, and credentials to XiaoMeng AGI; prefer a local status-check tool for simple HTTP checks. <br>
Risk: Requests may expose internal URLs, secrets, proprietary data, or long-lived credentials to the provider. <br>
Mitigation: Do not provide sensitive URLs, secrets, proprietary data, or long-lived credentials unless the provider is trusted and its billing and data-handling terms are understood. <br>


## Reference(s): <br>
- [API Reference](references/api-reference.md) <br>
- [XiaoMeng API homepage](https://xiaomeng-api.qisir.com) <br>
- [ClawHub skill page](https://clawhub.ai/xiaomeng-agi/skills/http-status-code-check) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [JSON API responses and terminal text, with documentation describing structured report sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and sends user requests to a paid third-party API; payment completion and credential are required to retrieve results.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
