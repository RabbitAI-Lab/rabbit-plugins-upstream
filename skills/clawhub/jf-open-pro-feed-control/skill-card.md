## Description: <br>
Controls JFTech smart pet feeders by checking feeder support, dispensing food on demand, managing feeding schedules, and toggling pet detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate bound, online JFTech smart pet feeder devices through JFTech OpenAPI credentials. It helps agents propose or run device-control commands for one-time feeding, feeding schedule management, pet detection settings, and capability checks. <br>

### Deployment Geography for Use: <br>
China Mainland, Asia, Europe, and North America <br>

## Known Risks and Mitigations: <br>
Risk: The skill can dispense food immediately or change feeding automation on a real pet feeder. <br>
Mitigation: Require explicit user confirmation before feeding, schedule changes, or pet detection changes, and keep portion and schedule changes within device-owner-approved limits. <br>
Risk: Signed device-control requests can be sent to the endpoint named in JF_ENDPOINT. <br>
Mitigation: Use only the documented JFTech regional hosts and reject unexpected endpoint values before running commands. <br>
Risk: JF_APP_SECRET and JF_DEVICE_TOKEN grant access to device-control APIs. <br>
Mitigation: Store credentials as private environment variables, scope them narrowly, rotate expired tokens, and avoid logging or sharing secrets. <br>


## Reference(s): <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>
- [ClawHub skill release page](https://clawhub.ai/jftech/skills/jf-open-pro-feed-control) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, environment variables, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JFTech OpenAPI credentials, a bound online feeder device, a device serial number, a device token, and a trusted regional endpoint.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
