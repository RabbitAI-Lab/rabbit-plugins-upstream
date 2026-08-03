## Description: <br>
This skill captures images from JieFeng monitoring devices, asks the agent to visually assess trash-bin overflow, and returns structured inspection reports for single-device, batch, and scheduled inspections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Facilities, operations, and environmental-services teams use this skill to configure JieFeng cameras, capture inspection images, and receive structured trash-bin overflow reports. Agents can run one-off inspections, batch inspections, or scheduled inspections when the required credentials, cameras, and dependent skills are available. <br>

### Deployment Geography for Use: <br>
China Mainland, Asia, Europe, and North America <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles camera/API credentials and may store camera passwords in configuration. <br>
Mitigation: Use trusted installations only, restrict file access to the camera configuration, and avoid placing API secrets or camera passwords in shared plaintext locations. <br>
Risk: The skill captures and stores surveillance images that may contain sensitive operational or personal information. <br>
Mitigation: Define retention and deletion rules for captured images before enabling inspections, especially for scheduled or shared reports. <br>
Risk: Scheduled reports can spread camera images or inspection results to unintended recipients. <br>
Mitigation: Confirm the destination channel and recipient scope before creating scheduled tasks, and do not inline secrets in scheduled-task messages. <br>
Risk: A configurable endpoint could send camera requests outside the intended vendor service. <br>
Mitigation: Keep JF_ENDPOINT limited to official JieFeng vendor domains. <br>


## Reference(s): <br>
- [JieFeng Open Platform documentation](https://docs.jftech.com) <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-garbage-inspection) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown inspection reports with JSON command output and captured image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports classify each camera as severe overflow, mild overflow, normal, unable to determine, offline, or failed, and may include local image file references.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
