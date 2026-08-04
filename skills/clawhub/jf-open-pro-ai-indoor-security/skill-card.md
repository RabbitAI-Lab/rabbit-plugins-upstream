## Description: <br>
JFTech indoor security skill for monitoring home scenes, querying alarms and statistics, managing member profiles, and controlling indoor security service state through the JFTech Open Platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators with JFTech Open Platform credentials use this skill to inspect household indoor security state, review abnormal alarms and occupancy statistics, and manage member face profiles for bound online devices with an active indoor security package. <br>

### Deployment Geography for Use: <br>
China, Asia, Europe, and North America <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a JFTech account token to inspect household security data and operate on indoor security settings. <br>
Mitigation: Install only for trusted publishers and keep JFTech credentials scoped, private, and supplied explicitly by the user. <br>
Risk: The skill can disable monitoring or add, update, and delete member face profiles. <br>
Mitigation: Require explicit user confirmation before changing service state or modifying member biometric profiles. <br>
Risk: Several helpers reference the move-card signing parameter inconsistently, which may affect operational reliability. <br>
Mitigation: Verify scripts and signing parameters before relying on the skill for production security workflows. <br>


## Reference(s): <br>
- [JFTech Open Platform](https://developer.jftech.com) <br>
- [Signature Algorithm Documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=609261d9bb5049c3a2fc7222adf465fb&lang=zh) <br>
- [Timestamp Algorithm Documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=8da7ad6119fd41159e2026c71ddb3555&lang=zh) <br>
- [Package Card Usage Documentation](https://docs.jftech.com/docs?menusId=54582398fd8d4248962354e92ac2e47a&siderId=d2c0d9105d9c4b78bc0d2ee3851d2557&lang=zh) <br>
- [ClawHub Skill Page](https://clawhub.ai/jftech/skills/jf-open-pro-ai-indoor-security) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Human-readable command output or JSON API responses, with setup guidance and shell command examples in Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JFTech credentials, device identifiers, an authorization token, and network access to JFTech API endpoints.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
