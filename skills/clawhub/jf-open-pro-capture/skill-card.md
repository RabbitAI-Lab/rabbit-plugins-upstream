## Description: <br>
JF Open Pro Capture helps agents capture real-time or thumbnail images from one or many JFTech devices, manage device tokens, and optionally download images locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators with JFTech Open Platform credentials use this skill to capture current or thumbnail images from bound, online JFTech camera devices individually or in batches. <br>

### Deployment Geography for Use: <br>
China Mainland, Asia, Europe, and North America, based on the documented JF API regional endpoints. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles JF app secrets, device credentials, device tokens, and image URLs that may expose device access or captured images if shared. <br>
Mitigation: Keep credentials and tokens out of shared environments, restrict logs and shell history, and rotate secrets or tokens when exposure is suspected. <br>
Risk: The configurable API endpoint and image download URL handling can send requests or save images outside expected trust boundaries. <br>
Mitigation: Use only trusted JF API endpoints and save downloaded images only to restricted directories with a defined deletion plan. <br>
Risk: Broad device-list files can expand capture scope across many devices and create unnecessary image collection. <br>
Mitigation: Use the smallest device list needed, protect device-list files, and avoid batch capture unless the task requires it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-capture) <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>
- [JFTech cloud capture pricing](https://aops.jftech.com/#/pricing?lang=zh&tab=MEDIA_PROCESSING) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with bash commands; runtime output can be plain text or JSON containing image URLs and optional downloaded image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Capture image URLs and device tokens are documented as valid for 24 hours; batch capture supports up to 500 devices per device-list file.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact metadata lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
