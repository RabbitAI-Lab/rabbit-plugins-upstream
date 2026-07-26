## Description: <br>
Verify mobile and landline numbers and WhatsApp registration status so teams can reduce invalid contacts before outreach. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales teams, recruiters, traders, and exporters use this skill to validate phone-number authenticity, identify mobile, landline, invalid, unknown, and WhatsApp-registered statuses, and clean contact lists before outreach. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Phone numbers checked with this skill are sent to Upkuajing's third-party API. <br>
Mitigation: Use the skill only for contact data the user is authorized to validate, and review the provider's data-handling terms before bulk validation. <br>
Risk: The API key is stored locally in ~/.upkuajing/.env. <br>
Mitigation: Keep the file private, avoid sharing logs or screenshots that reveal credentials, and rotate the key if it may have been exposed. <br>
Risk: Phone-validity API calls can incur fees. <br>
Mitigation: Confirm pricing and get explicit user approval before running paid checks, especially for bulk contact lists. <br>
Risk: Sensitive contact lists could be exposed if API logging is enabled. <br>
Mitigation: Keep API logging disabled for sensitive datasets and avoid storing request or response logs containing phone numbers. <br>


## Reference(s): <br>
- [Phone Validity API](references/phone-api.md) <br>
- [Upkuajing Homepage](https://www.upkuajing.com) <br>
- [Upkuajing Open Platform](https://developer.upkuajing.com/) <br>
- [Upkuajing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON results with concise text guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; API calls may incur confirmed fees.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md metadata and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
