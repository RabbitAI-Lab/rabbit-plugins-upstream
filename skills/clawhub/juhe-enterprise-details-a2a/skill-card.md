## Description: <br>
Queries Juhe's enterprise information API for detailed company registration records, shareholders, key personnel, branches, change history, and business abnormality records after user payment consent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to perform paid lookups of Chinese enterprise registration details by company name, registration number, or unified social credit code. It is intended for business verification, due diligence, risk review, and company profile checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the queried company name, registration number, or unified social credit code to Juhe's API for each paid lookup. <br>
Mitigation: Confirm user payment consent and disclose that only the enterprise query keyword is transmitted before making the request. <br>
Risk: Third-party enterprise registration data may be delayed, incomplete, or unsuitable as the sole basis for business decisions. <br>
Mitigation: Present the output as reference information and direct users to verify important decisions against official registration sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-details-a2a) <br>
- [Juhe enterprise query API endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API calls, Guidance] <br>
**Output Format:** [Markdown tables and sections generated from the paid API response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a fixed disclaimer that third-party enterprise data is for reference and should be checked against official registration sources.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
