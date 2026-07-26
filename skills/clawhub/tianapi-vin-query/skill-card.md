## Description: <br>
通过17位车架号（VIN码）查询车辆信息，包括品牌、车型年款、排量、发动机类型及指导价等。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, vehicle data workflows, and agents use this skill to look up vehicle details from a 17-digit VIN through TianAPI and present fields such as brand, model year, displacement, engine type, drivetrain, and MSRP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: VINs and the TianAPI credential are sent to TianAPI when the lookup runs. <br>
Mitigation: Install and use the skill only when sending VINs to TianAPI is acceptable for the workflow. <br>
Risk: Passing an API key directly in commands or storing it in scripts/.env can expose the credential if shell history or local files are shared. <br>
Mitigation: Prefer TIANAPI_VIN_KEY from the environment or a secret manager, and do not commit or share scripts/.env. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-vin-query) <br>
- [TianAPI VIN query documentation](https://www.tianapi.com/apiview/260) <br>
- [TianAPI VIN query endpoint](https://apis.tianapi.com/chavin/index) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TianAPI key provided through TIANAPI_VIN_KEY, a local .env file, or the command line.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
