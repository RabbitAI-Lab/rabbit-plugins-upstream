## Description: <br>
查询公司海关贸易港口列表数据，获取港口的贸易次数、金额和占比，帮助外贸团队分析物流通道使用情况和核心进出口港。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade, logistics, and supply-chain teams use this skill to query company-level customs port distributions and analyze trade counts, amounts, quantity, weight, and share by port. It supports paginated lookup workflows for identifying important import and export ports and reviewing route concentration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes paid API requests to Upkuajing. <br>
Mitigation: Confirm the user understands the charge before each query and use the documented pricing helper or pricing page instead of estimating costs. <br>
Risk: The skill can read or write UPKUAJING_API_KEY in a plaintext dotfile under ~/.upkuajing/.env. <br>
Mitigation: Prefer an environment variable or a secure secret manager, restrict local file permissions, and avoid sharing command output that exposes key material. <br>
Risk: Account information and recharge-order details may be returned when helper commands are used. <br>
Mitigation: Run account and recharge helpers only after explicit user request and avoid exposing payment or account details beyond the intended user. <br>


## Reference(s): <br>
- [公司贸易港口列表 API 参考](artifact/references/customs-company-port-list-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-port-list-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses and concise Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; queries can incur per-call charges.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
