## Description: <br>
Verify email validity and format, reduce email bounce rates, and clean contact lists for exporters, recruiters, and B2B sales teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External teams and agents use this skill to validate one or more email addresses through Upkuajing's remote API before outreach, CRM cleanup, recruiting checks, supplier verification, or buyer validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email addresses are sent to Upkuajing's remote API for validation. <br>
Mitigation: Use the skill only for addresses you are permitted to share with Upkuajing, and avoid submitting sensitive lists without appropriate review. <br>
Risk: The skill stores UPKUAJING_API_KEY in a plaintext file under the user's home directory when using its key setup flow. <br>
Mitigation: Prefer environment-variable secret management where possible, restrict filesystem access to the key file, and rotate the key if it may have been exposed. <br>
Risk: API calls may incur fees and the skill includes account and top-up flows. <br>
Mitigation: Confirm pricing and explicit user approval before paid validation, and review account balance or fee output after use. <br>
Risk: The shared request helper performs an automatic version check before API requests. <br>
Mitigation: Review or disable automatic version checking in environments that require strict data minimization or tightly controlled network destinations. <br>


## Reference(s): <br>
- [Email Validity API](references/email-api.md) <br>
- [Upkuajing Homepage](https://www.upkuajing.com) <br>
- [Upkuajing Open Platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; sends email addresses to a paid remote API and returns validity status, reason, total count, and fee information.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
