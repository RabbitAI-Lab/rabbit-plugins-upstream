## Description: <br>
JFTech Open Platform child-care monitoring skill for checking child-care service status, querying home safety alarms, managing stranger entries, and reviewing child activity statistics for supported JFTech devices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External JFTech device administrators use this skill to operate child-care monitoring workflows, including service status checks, safety alarm review, stranger-library updates, and behavior statistics queries. It requires valid JFTech credentials, an online bound device, and an active child-care service package. <br>

### Deployment Geography for Use: <br>
China, Asia, Europe, and North America, based on the documented JFTech regional endpoints. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles child and home surveillance data, including device identifiers, alarms, behavior statistics, and person-library changes. <br>
Mitigation: Use it only for devices and child-care services you are authorized to administer, and review privacy expectations before sending data to JFTech endpoints. <br>
Risk: The skill requires sensitive credentials such as app secret and authorization token. <br>
Mitigation: Store credentials securely, avoid logging or sharing them, and rotate tokens or secrets if exposure is suspected. <br>
Risk: The skill can enable or disable child-care monitoring and add or remove stranger records. <br>
Mitigation: Manually confirm each enable, disable, add, or remove action before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jftech/skills/jf-open-pro-ai-child-care) <br>
- [JFTech Developer Platform](https://developer.jftech.com) <br>
- [JFTech Signature Algorithm Documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=609261d9bb5049c3a2fc7222adf465fb&lang=zh) <br>
- [JFTech Timestamp Algorithm Documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=8da7ad6119fd41159e2026c71ddb3555&lang=zh) <br>
- [JFTech Package Card Documentation](https://docs.jftech.com/docs?menusId=54582398fd8d4248962354e92ac2e47a&siderId=d2c0d9105d9c4b78bc0d2ee3851d2557&lang=zh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and command-line text with optional JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include child-care service state, alarm summaries, behavior counts or durations, and status messages from authenticated JFTech API calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
