## Description: <br>
查询车载诊断系统（OBD）故障码含义，包含适用车型、故障范围及维修建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up automotive OBD fault-code meanings from TianAPI and present applicable vehicle models, fault scope, Chinese and English explanations, and repair guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OBD codes and the TianAPI key are sent to TianAPI during lookup. <br>
Mitigation: Use the skill only when sharing those values with TianAPI is acceptable, and prefer TIANAPI_OBDCODE_KEY over command-line or URL key examples. <br>
Risk: API keys may be exposed through shell history, URLs, or saved .env files. <br>
Mitigation: Avoid command-line and URL key examples for routine use, protect any scripts/.env file, and do not commit credentials. <br>
Risk: The published helper script appears syntactically broken. <br>
Mitigation: Expect the maintainer to fix the script before relying on it, or use the documented direct API call with appropriate credential handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-obdcode) <br>
- [TianAPI OBD code API documentation](https://www.tianapi.com/apiview/247) <br>
- [TianAPI OBD code API endpoint](https://apis.tianapi.com/obdcode/index) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TianAPI key configured as TIANAPI_OBDCODE_KEY, a scripts/.env entry, or a command-line key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
