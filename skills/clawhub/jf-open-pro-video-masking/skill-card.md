## Description: <br>
Controls JFTech PTZ device one-key video masking by moving the camera to the masking position and disabling video preview and recording to protect privacy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to enable, disable, or check JFTech camera privacy masking for homes, meeting rooms, and scheduled privacy modes. <br>

### Deployment Geography for Use: <br>
China mainland, Asia, Europe, and North America <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends signed device-control requests and device tokens to a hostname configured through JF_ENDPOINT. <br>
Mitigation: Run it only with JF_ENDPOINT set to an official JFTech regional host and prevent untrusted users or scripts from setting its environment variables. <br>
Risk: App secrets and device tokens are required to operate the skill. <br>
Mitigation: Keep credentials scoped to the intended device or account, rotate them regularly, and avoid exposing them in shared shells, logs, or automation. <br>
Risk: Enable and disable actions can change camera position, live preview, and recording state. <br>
Mitigation: Use the skill only on intended online devices that support one-key masking, and confirm operational impact before running enable, disable, or toggle actions. <br>


## Reference(s): <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-video-masking) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jftech) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JFTech credentials, a device token, a device serial number, and a regional API endpoint.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact frontmatter metadata version is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
