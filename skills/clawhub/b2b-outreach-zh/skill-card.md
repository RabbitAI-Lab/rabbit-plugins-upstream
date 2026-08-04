## Description: <br>
端到端 B2B 触达工具集，整合批量冷邮件、全球短信、Google Maps 商户采集与手机号、邮箱、域名校验，用于采集、清洗、触达和监控跨境销售线索。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Exporters, trade companies, purchasing agents, and global sales teams use this skill to collect merchant leads, validate contact details, send email or SMS outreach, and monitor delivery, opens, replies, and failures. Users should only run campaigns when they are authorized to process recipient data and contact recipients under applicable privacy and anti-spam rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recipient emails, phone numbers, and message content are sent to the UpKuaJing OpenAPI service for outreach, validation, search, account, and billing workflows. <br>
Mitigation: Use the skill only when authorized to process and upload that data, and follow applicable privacy and anti-spam laws for the intended recipients and regions. <br>
Risk: Email, SMS, merchant search, and contact validation operations can incur charges. <br>
Mitigation: Confirm pricing and user approval before paid operations; use the documented price information command or pricing page instead of estimating costs. <br>
Risk: The API key may be stored in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Restrict local file access, avoid sharing the key, and rotate the key if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/b2b-outreach-zh) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing developer platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Email Send API](artifact/references/email-send-api.md) <br>
- [SMS Send API](artifact/references/sms-send-api.md) <br>
- [Merchants Search API](artifact/references/merchants-search-api.md) <br>
- [Phone Validity API](artifact/references/validity-phone-api.md) <br>
- [Email Validity API](artifact/references/validity-email-api.md) <br>
- [Domain Validity API](artifact/references/validity-domain-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid operations can submit email, SMS, merchant search, contact validation, account, and billing requests to the UpKuaJing OpenAPI service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
