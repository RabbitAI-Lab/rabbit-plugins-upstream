## Description: <br>
Queries TianAPI company registration data by company name or unified social credit code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to look up TianAPI business registration records by company name or unified social credit code, then present fields such as legal representative, registered capital, company status, address, and business scope. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company names or unified social credit codes are sent to TianAPI, and the API key may be exposed if passed on the command line or committed in a .env file. <br>
Mitigation: Install only when TianAPI disclosure is acceptable; prefer TIANAPI_COMPANY_KEY for credential configuration, avoid command-line keys, and do not commit .env files containing the API key. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-company-info) <br>
- [TianAPI company information API](https://www.tianapi.com/apiview/272) <br>
- [TianAPI companyinfo endpoint](https://apis.tianapi.com/companyinfo/index) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TianAPI key configured with TIANAPI_COMPANY_KEY, .env, or the --key command-line option.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
