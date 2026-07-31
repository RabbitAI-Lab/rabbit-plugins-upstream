## Description: <br>
Manages JFTech smart alarm device capabilities, motion alarm settings, notification reporting, alarm schedules, alarm message lists, and alarm picture retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to query JFTech smart alarm device capabilities, inspect and change motion detection settings, configure reporting and alarm schedules, and retrieve alarm records or alarm picture URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses alarm credentials and device tokens. <br>
Mitigation: Configure credentials yourself, store JF_APP_SECRET and JF_DEVICE_TOKEN as secrets, and avoid placing them in shared logs or prompts. <br>
Risk: The endpoint can be configured through JF_ENDPOINT. <br>
Mitigation: Set JF_ENDPOINT only to one of the documented JFTech regional API domains before running commands. <br>
Risk: The skill can disable alarms, disable phone reporting, or change alarm schedules on a live device. <br>
Mitigation: Review each requested action and command arguments before executing configuration-changing operations. <br>
Risk: Alarm picture retrieval can expose private alarm media URLs. <br>
Mitigation: Request alarm pictures only for intended time ranges or alarm IDs and treat returned URLs as sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-device-smart-alarm) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include device status summaries, alarm configuration summaries, alarm record identifiers, and alarm picture URLs returned by the configured JFTech endpoint.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
