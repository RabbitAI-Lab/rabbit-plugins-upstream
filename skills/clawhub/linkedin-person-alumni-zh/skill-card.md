## Description: <br>
依托 LinkedIn 数据，按人员 ID 和学校 ID 查询校友列表，用于发掘共同求学背景和潜在商务关系。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External recruiters, sales teams, and B2B lead builders use this skill to query LinkedIn alumni relationships from a known person ID and school ID, then expand prospect lists or trace education-based connections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs paid LinkedIn alumni lookup API calls. <br>
Mitigation: Confirm each paid query before execution and review price or account information when cost context is needed. <br>
Risk: The skill handles a local UPKUAJING_API_KEY value and may store it in ~/.upkuajing/.env. <br>
Mitigation: Store the key deliberately, avoid printing the local environment file, and rotate or remove the key if it is exposed. <br>
Risk: The account recharge flow can return a payment URL. <br>
Mitigation: Review any recharge payment URL before opening it or paying. <br>


## Reference(s): <br>
- [LinkedIn Alumni List API Reference](references/linkedin-person-alumni-list-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-alumni-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API calls return fee metadata.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
