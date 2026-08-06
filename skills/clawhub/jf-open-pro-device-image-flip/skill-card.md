## Description: <br>
Controls and queries horizontal mirror and vertical flip settings for JFTech camera images through JFTech OpenAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect or change image orientation for bound, online JFTech cameras, especially when cameras are mounted upside down or mirrored. <br>

### Deployment Geography for Use: <br>
Mainland China, Asia, Europe, and North America via the listed JFTech regional API endpoints. <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses JFTech API credentials and a device token to access camera configuration. <br>
Mitigation: Provide only the minimum device scope available, keep credentials in the operator environment or secret store, and rotate tokens when they expire or are exposed. <br>
Risk: Set and reset actions can immediately change the live camera image orientation and persist until changed again. <br>
Mitigation: Confirm the target device, channel, and action before applying changes, and query the current configuration before and after updates. <br>
Risk: Changing JF_ENDPOINT can direct requests away from the intended JFTech regional API host. <br>
Mitigation: Use only the official regional JFTech API endpoint for the deployment region. <br>


## Reference(s): <br>
- [JFTech Open Platform Documentation](https://docs.jftech.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/jftech/skills/jf-open-pro-device-image-flip) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses JFTech API credentials and device identifiers supplied by the operator to query or update camera orientation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
