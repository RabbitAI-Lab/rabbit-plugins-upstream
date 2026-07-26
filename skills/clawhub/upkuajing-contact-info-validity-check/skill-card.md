## Description: <br>
Verify phone numbers, WhatsApp registration status, email addresses, and business domains through the UpKuaJing Open Platform API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, recruiting, export, and CRM operations teams use this skill to clean contact lists before outreach by checking phone, email, WhatsApp, and domain validity. Developers and agents use it to run the packaged validation scripts and return structured API results with fee information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Contact data submitted for validation is sent to UpKuaJing's remote API. <br>
Mitigation: Use the skill only when users accept third-party processing of the contact data being checked. <br>
Risk: Validation requests are paid API calls and may consume account balance. <br>
Mitigation: Confirm fee-bearing operations with the user before executing validation scripts or top-up actions. <br>
Risk: The UPKUAJING_API_KEY is read from the environment or ~/.upkuajing/.env and grants API access. <br>
Mitigation: Protect the API key file, avoid sharing it, and rotate the key if exposure is suspected. <br>
Risk: Optional API logging can retain request and response data locally if enabled. <br>
Mitigation: Keep API logging disabled for sensitive contact lists unless local retention is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-contact-info-validity-check) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing developer platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Phone Validity API](artifact/references/phone-api.md) <br>
- [Email Validity API](artifact/references/email-api.md) <br>
- [Domain Validity API](artifact/references/domain-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results from scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Validation calls return result lists and fee information; successful use requires a UPKUAJING_API_KEY.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
