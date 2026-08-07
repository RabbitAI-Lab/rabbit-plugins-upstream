## Description: <br>
Controls JFTech PTZ camera devices for directional movement, zoom and focus, preset management, patrol tours, and return-to-watch-position workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and developers use this skill to configure and run authenticated JFTech PTZ camera controls, including movement, zoom/focus, presets, and patrol routes for supported online devices. <br>

### Deployment Geography for Use: <br>
China, Asia, Europe, and North America via documented JFTech regional API hosts. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move PTZ cameras, delete presets, start patrols, and clear tours when supplied valid credentials. <br>
Mitigation: Install only for authorized operators and require explicit confirmation before movement, preset deletion, tour start, or tour clearing actions. <br>
Risk: Secrets such as JF_APP_SECRET and JF_DEVICE_TOKEN are required for operation. <br>
Mitigation: Store credentials in protected environment variables or a secrets manager and avoid logging or sharing them. <br>
Risk: JF_ENDPOINT can override the API host. <br>
Mitigation: Keep JF_ENDPOINT restricted to the documented JFTech regional hosts. <br>


## Reference(s): <br>
- [JFTech Open Platform Documentation](https://docs.jftech.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/jftech/skills/jf-open-pro-ptz-control) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline bash commands and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JFTech OpenAPI credentials, a device token, and an online PTZ-capable device.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
