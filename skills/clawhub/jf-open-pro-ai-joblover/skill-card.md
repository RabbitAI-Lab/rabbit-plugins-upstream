## Description: <br>
JFTech Joblover monitors employee duty status, sends on-duty and off-duty notifications, detects abnormal on-duty behavior, and records behavior statistics for workplace inspection workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to configure and query JFTech employee duty monitoring, including duty plans, service status, abnormal-behavior alarms, and behavior statistics. <br>

### Deployment Geography for Use: <br>
China Mainland, Asia, Europe, and North America <br>

## Known Risks and Mitigations: <br>
Risk: Employee monitoring may be inappropriate or unlawful without authorization, notice, and access controls. <br>
Mitigation: Deploy only in environments with a clear legal basis for employee monitoring and restrict access to authorized operators. <br>
Risk: App secrets, authorization tokens, device identifiers, alarm images, and monitoring output may be exposed in terminal output, logs, or screenshots. <br>
Mitigation: Treat credentials and monitoring outputs as sensitive, protect logs and screenshots, and avoid verbose mode unless outputs can be secured. <br>
Risk: The skill can change monitoring state and delete duty plans. <br>
Mitigation: Require operator review before disabling monitoring or deleting duty plans, and limit those actions to trusted users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-ai-joblover) <br>
- [JFTech Open Platform](https://developer.jftech.com) <br>
- [JFTech signature algorithm documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=609261d9bb5049c3a2fc7222adf465fb&lang=zh) <br>
- [JFTech timestamp algorithm documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=8da7ad6119fd41159e2026c71ddb3555&lang=zh) <br>
- [JFTech package card usage documentation](https://docs.jftech.com/docs?menusId=54582398fd8d4248962354e92ac2e47a&siderId=d2c0d9105d9c4b78bc0d2ee3851d2557&lang=zh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts return formatted text or JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JFTech account, device, package, app credentials, authorization token, and device/user identifiers.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter metadata.version is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
