## Description: <br>
根据物品名称查询垃圾分类信息，支持模糊搜索和精确搜索。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up garbage classification results by item name and receive disposal suggestions from TianAPI data. It supports fuzzy or precise queries through a Python helper script or direct API access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The query item name and API key are sent to TianAPI. <br>
Mitigation: Avoid querying sensitive item names and use a dedicated TianAPI key with appropriate access limits. <br>
Risk: API keys may be exposed if passed on the command line or embedded in copied URLs. <br>
Mitigation: Prefer TIANAPI_LAJIFENLEI_KEY as an environment variable and avoid storing credentials in shell history or shared documentation. <br>
Risk: Some documented examples may not match the current script flags, and advertised JSON mode appears incomplete. <br>
Mitigation: Use the implemented --key and --word flags, verify script output before automation, and review examples before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-lajifenlei) <br>
- [TianAPI garbage classification API documentation](https://www.tianapi.com/apiview/97) <br>
- [TianAPI garbage classification endpoint](https://apis.tianapi.com/lajifenlei/index) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and text or JSON-like query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TIANAPI_LAJIFENLEI_KEY credential; queries send the item name and API key to TianAPI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
