## Description: <br>
JFTech device OSD watermark configuration skill for reading and changing live device overlay settings, including channel title, time title, privacy areas, and related OSD attributes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to query and update JFTech camera OSD settings through documented cloud API calls, including channel title display and OSD configuration checks. It requires valid JFTech app credentials, a bound online device, and a device token. <br>

### Deployment Geography for Use: <br>
China Mainland, Asia, Europe, and North America <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends JFTech app credentials and a device token to a JFTech cloud endpoint to read or change camera OSD settings. <br>
Mitigation: Install and run it only for intended JFTech devices, protect credential environment variables, and keep JF_ENDPOINT set to a documented JFTech regional domain. <br>
Risk: Some documented examples for time-title and privacy-area changes are not implemented by the current script actions. <br>
Mitigation: Check the script-supported actions before relying on those examples, and verify device settings after any configuration change. <br>


## Reference(s): <br>
- [JFTech Open Platform Documentation](https://docs.jftech.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command examples and text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided JFTech credentials and device token to read or change camera OSD settings.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
