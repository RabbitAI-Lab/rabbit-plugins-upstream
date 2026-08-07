## Description: <br>
This skill queries JFTech device online status for one bound device or batches of device tokens and returns online or offline results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and device operators use this skill to check whether JFTech-bound devices are online, either one device at a time or in batches of up to 500 tokens. It can also surface wake status and WAN IP fields returned by the JFTech API. <br>

### Deployment Geography for Use: <br>
China mainland, Asia, Europe, and North America regional endpoints are documented. <br>

## Known Risks and Mitigations: <br>
Risk: JFTech credentials and device tokens can be sent to a configurable API host. <br>
Mitigation: Keep JF_UUID, JF_APP_KEY, JF_APP_SECRET, and device tokens private, and set JF_ENDPOINT only to the intended official regional host. <br>
Risk: Device status output can reveal WAN IP addresses. <br>
Mitigation: Run the skill only in trusted environments and limit table output sharing to users who are allowed to see device network details. <br>
Risk: The security verdict requires review before deployment. <br>
Mitigation: Review the skill and its ClawHub scan result before installing it in shared or production agent environments. <br>


## Reference(s): <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or table output, with optional JSON for device status results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JFTech API credentials and device tokens; batch queries are processed in groups of up to 500 tokens.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
