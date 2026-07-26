## Description: <br>
根据章节ID查询古籍名著的详情内容，涵盖《论语》《道德经》《山海经》等经典文献。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to retrieve classic Chinese literature chapter details from TianAPI by chapter ID, then present the returned title, author, work name, and content in a readable form. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be exposed if passed directly on the command line, embedded in URLs, or written to a shared .env file. <br>
Mitigation: Prefer TIANAPI_ANCBOOKS_KEY from the environment or a secure secret store; restrict any local .env file permissions and do not commit or share it. <br>
Risk: The skill depends on TianAPI availability, quota, and valid ancient-books chapter IDs. <br>
Mitigation: Check returned error codes and retry transient network failures once before reporting configuration, quota, or lookup issues to the user. <br>


## Reference(s): <br>
- [TianAPI ancient books API](https://www.tianapi.com/apiview/265) <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-ancbooks) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TIANAPI_ANCBOOKS_KEY; the helper script returns a success flag with data or an error message.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
