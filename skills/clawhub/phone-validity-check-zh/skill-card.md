## Description: <br>
核验电话号码真实有效性、号码类型以及 WhatsApp 注册状态，输出核验结果、号码分类、国家代码和 WhatsApp 启用情况，筛选无效联系方式，提升外贸客户触达效率。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales teams, recruiters, traders, and CRM operators use this skill to check phone-number validity, line type, country code, and WhatsApp availability before outreach, screening, or supplier verification. It helps reduce invalid contacts and improve customer reach by calling the upkuajing phone-validation API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Phone numbers are sent to the upkuajing remote API for validation. <br>
Mitigation: Confirm the user is comfortable sharing the numbers with the provider and minimize submitted data to the numbers needed for the task. <br>
Risk: Validation, recharge, and key-management flows can involve paid API use or account billing actions. <br>
Mitigation: Explain that calls may cost money and wait for explicit user confirmation before running paid operations or creating recharge orders. <br>
Risk: The API key may be stored in plaintext under ~/.upkuajing/.env. <br>
Mitigation: Protect local file permissions, avoid exposing the key in prompts or logs, and rotate the key if it is disclosed. <br>
Risk: If request logging is enabled, local logs may contain phone numbers and API responses. <br>
Mitigation: Keep request logging disabled unless needed and protect or delete any generated logs that contain contact data. <br>


## Reference(s): <br>
- [电话有效性检测 API](artifact/references/phone-api.md) <br>
- [upkuajing homepage](https://www.upkuajing.com) <br>
- [upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/phone-validity-check-zh) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON result summaries with shell command examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; remote API calls may incur account charges.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
