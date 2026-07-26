## Description: <br>
核验域名可用性、安全状态以及风险标记，输出域名验证结论、校验失败原因和敏感标签，清理风险域名，优化外贸邮件列表并降低邮件退信概率。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, marketing, recruiting, procurement, and research teams use this skill to validate company domains before CRM cleanup, outbound email campaigns, lead verification, supplier checks, background research, and mailing-list hygiene. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Domain checks and recharge actions can incur charges through an external paid API. <br>
Mitigation: Ask for explicit user approval before paid checks or recharge flows, and use the published price information or price-info command rather than estimating costs. <br>
Risk: The API key may be stored locally at ~/.upkuajing/.env. <br>
Mitigation: Protect the local key file, avoid sharing key contents, and rotate or replace the key if exposure is suspected. <br>
Risk: Recharge flows can return payment URLs. <br>
Mitigation: Verify payment URLs and order details before opening or sharing them with the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/domain-validity-check-zh) <br>
- [Publisher profile](https://clawhub.ai/user/upkuajing) <br>
- [upkuajing homepage](https://www.upkuajing.com) <br>
- [API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Domain validity API reference](references/domain-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; domain-check API calls may incur charges.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
