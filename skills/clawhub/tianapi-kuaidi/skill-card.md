## Description: <br>
查询全球快递物流动态信息，支持自动识别单号，顺丰等需传手机号后四位。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query shipment tracking status and logistics history through TianAPI using a tracking number, optional carrier code, and optional phone suffix when a carrier requires it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shipment tracking numbers, carrier identifiers, and phone suffixes may be sent to TianAPI during lookup. <br>
Mitigation: Use the skill only when sharing those shipment details with TianAPI is acceptable, and provide the phone suffix only when the carrier requires it. <br>
Risk: The TianAPI credential can be exposed if passed directly in command history or committed in a local .env file. <br>
Mitigation: Prefer the TIANAPI_KUAIDI_KEY environment variable and keep any local .env file out of shared artifacts. <br>


## Reference(s): <br>
- [TianAPI Kuaidi API Documentation](https://www.tianapi.com/apiview/152) <br>
- [ClawHub Skill Page](https://clawhub.ai/workxin/skills/tianapi-kuaidi) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/workxin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TIANAPI_KUAIDI_KEY credential; queries send shipment tracking details to TianAPI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
