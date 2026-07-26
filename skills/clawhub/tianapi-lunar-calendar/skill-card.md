## Description: <br>
查询中国老黄历，获取指定日期的宜忌、冲煞、吉时、胎神等传统民俗信息。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and users use this skill to retrieve Chinese lunar-calendar and almanac details from TianAPI for a Gregorian or lunar date, then present daily traditions such as appropriate and avoided activities, clash directions, auspicious positions, and related fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends lookup dates and a TianAPI key to TianAPI when fetching lunar-calendar data. <br>
Mitigation: Install only if that data sharing is acceptable, prefer the TIANAPI_LUNAR_CALENDAR_KEY environment variable, and avoid putting the key in command lines, URLs, logs, or screenshots. <br>
Risk: A TianAPI key stored in scripts/.env or shell history can be exposed if the workspace, logs, or screenshots are shared. <br>
Mitigation: Do not commit scripts/.env, keep local credential files out of shared artifacts, and rotate the key if it is exposed. <br>


## Reference(s): <br>
- [TianAPI Chinese Lunar Calendar API](https://www.tianapi.com/apiview/45) <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-lunar-calendar) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and formatted text or JSON results from the TianAPI lookup script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TIANAPI_LUNAR_CALENDAR_KEY; supports Gregorian dates and lunar-date lookups through the bundled script or direct TianAPI calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
